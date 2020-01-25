import os
import time
from datetime import datetime as dt
import image_preprocessing.empty_tag_check as tag_check
from collections import OrderedDict

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

AZURE_CLASSIFIER_KEY = os.environ['AZURE_CUSTOM_VISION_CLASSIFIER_KEY']
AZURE_CUSTOM_VISION_CLASSIFIER_ENDPOINT = os.environ['AZURE_CUSTOM_VISION_CLASSIFIER_ENDPOINT']
AZURE_PREDICTION_RESOURCE_ID=os.environ['AZURE_CUSTOM_VISION_PREDICTION_RESOURCE_ID']

trainer = CustomVisionTrainingClient(AZURE_CLASSIFIER_KEY, AZURE_CUSTOM_VISION_CLASSIFIER_ENDPOINT)


def create_project():
    project = trainer.create_project('Development Classifier 1', classification_type='Multiclass')
    return project


def create_tag(project, tag_name):
    tag = trainer.create_tag(project.id, tag_name)
    return tag


def upload_images_from_directory(project, directory_name):
    for dirpath, _dirnames, files in os.walk(directory_name):
        print(f'Files in {dirpath}')
        upload_list = []
        
        tag_name = dirpath.split('/')[-1]
        tag = create_tag(project, tag_name)
        
        for file in files:
            opened_files = []           
            full_file_name = dirpath + '/' + file
            print(f'     - {file} - tag_name: {tag_name} ')            
            
            if file in opened_files:
                print(f' Already processed: {file}')
                continue

            with open(full_file_name, 'rb') as image_contents:
                image_file_entry = ImageFileCreateEntry(name=file, contents=image_contents.read(), tag_ids=[tag.id])
                upload_list.append(image_file_entry)
                opened_files.append(file)
        
        upload_result = trainer.create_images_from_files(project.id, images=upload_list)
        
        if not upload_result.is_batch_successful:
            for image in upload_result.images:
                print(f'Image Status: {image.status}')

    
def upload_images(project, base_dir_name='/home/sidravic/downloaded_images/v1'):
    dirs = tag_check.find_empty_dir(base_dir_name)
    empty_dirs = dirs['empty_directories']
    images_per_directory = dirs['files_per_directory']
    sorted_images_per_directory = OrderedDict(sorted(images_per_directory.items(), key=lambda x: x[1], reverse=True))

    considered_product_dirs = list(sorted_images_per_directory.items())[:50]

    index = 0
    for directory, no_of_files in considered_product_dirs:
        print(f'{index}: {directory} - {no_of_files}')
        full_directory_name = base_dir_name + '/' + directory
        index += 1
        upload_images_from_directory(project, full_directory_name)

    print(considered_product_dirs)
    return


def train_project(project_id):
    iteration = trainer.train_project(project_id)

    while iteration.status != 'Completed':
        iteration = trainer.get_iteration(project_id, iteration.id)
        print(f' IterationId: {iteration.id} - Training Status: {iteration.status}')
        time.sleep(1)
        
    return iteration.id


def publish_iteration(project_id, iteration_id, prediction_resource_id=AZURE_PREDICTION_RESOURCE_ID):
    published_iteration_name = f'development-classifier-interation-${int(dt.now().timestamp())}'
    trainer.publish_iteration(project_id, iteration_id, published_iteration_name, prediction_resource_id)
    print(f'Trained and published - project_id: {project_id} '
          f'IterationId: {iteration_id}, iteration_name: {published_iteration_name}')
    return


def train_and_publish():
    project = create_project()
    upload_images(project, '/home/sidravic/downloaded_images/internal_v2')
    iteration_id = train_project(project.id)
    publish_iteration(project.id, iteration_id)
    return


#train_and_publish()
publish_iteration('d1b72a4d-a142-41c4-8e59-fa80ae3e7a17', 'a77bdf03-3eee-45ff-953f-415108797eb0')


