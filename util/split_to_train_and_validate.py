from image_preprocessing.move_files import copy_file, create_folder
import os
import random

training_set_path = '/home/sidravic/downloaded_images/s3/train'
validation_set_path = '/home/sidravic/downloaded_images/s3/validate'


def split_folder(folder_path, files):
    random.shuffle(files)
    total_files = len(files)
    validation_set_count = int(total_files * (20/100))
    print(f'Total: {total_files}, Train Set: {total_files - validation_set_count}, Validation Set: {validation_set_count}')

    product_folder_name = folder_path.split('/')[-1]
    training_product_path = training_set_path + '/' + product_folder_name
    validation_product_path = validation_set_path + '/' + product_folder_name

    create_folder(training_product_path)
    create_folder(validation_product_path)

    validation_files = files[0:(validation_set_count - 1)]
    training_files = files[(validation_set_count - 1):]

    for file in validation_files:
        src_file_path = folder_path + '/' + file
        destination_file_path = validation_product_path + '/' + file
        copy_file(src_file_path, destination_file_path)

    for file in training_files:
        src_file_path = folder_path + '/' + file
        destination_file_path = training_product_path + '/' + file
        copy_file(src_file_path, destination_file_path)

    return

def create_train_and_validate(directory):
    for dirpath, dirnames, files in os.walk(directory):
        if len(dirnames) == 0:
            print('*' * 100)
            print(f'Processing path: {dirpath}: files: {len(files)}')
            split_folder(dirpath, files)


create_train_and_validate('/home/sidravic/downloaded_images/internal/')