import cv2
import os
import image_preprocessing.move_files as mf


class FaceCheck:
    def __init__(self, image_dir=None, destination_dir=None):
        self.image_dir = image_dir        
        self.destination_dir = destination_dir
        self.cascade_classifier = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def invoke(self):
        for dirpath, dirnames, files in os.walk(self.image_dir):
            print(f'Files found in {dirpath} are:')
            for file in files:
                full_file_path = dirpath + '/' + file
                [num_of_faces, has_face] = self.has_faces(full_file_path)
                if has_face:
                    print(f'{file}: Has Face: {has_face}, No: {num_of_faces}')

                if has_face:
                    directory_name = dirpath.split('/')[-1]
                    destination_folder_path = self.destination_dir + '/' + directory_name
                    destination_file_path = destination_folder_path + '/' + file
                    mf.create_folder(destination_folder_path)
                    mf.move_file(full_file_path, destination_file_path)

    def has_faces(self, image_path):
        try:
            image = cv2.imread(image_path)
            gray_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.cascade_classifier.detectMultiScale(
                gray_scale_image,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(30, 30)
            )

            num_of_faces = len(faces)            
            return [num_of_faces, not (num_of_faces == 0)]
        except RuntimeError as e:
            print(f'{e}')


FaceCheck('/home/sidravic/downloaded_images/internal', '/home/sidravic/downloaded_images_faces/v1').invoke()