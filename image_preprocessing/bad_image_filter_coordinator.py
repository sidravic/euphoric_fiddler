import os
from os import path
from image_preprocessing import image_check
from image_preprocessing import move_files as mf
import logging


class Coordinator:
    def __init__(self, image_dir='/home/sidravic/downloaded_images/v1', bad_images_dir='/home/sidravic/corrupt_images/v1'):
        self.image_dir = image_dir
        self.bad_images_dir = bad_images_dir

    def invoke(self):
        for dirpath, dirnames, files in os.walk(self.image_dir):
            print(f'Files found in {dirpath} are:')      
            for file in files:            
                full_file_path = dirpath + '/' + file                
                is_valid = image_check.ValidImageCheck(full_file_path).validate()
                
                if not is_valid:
                    directory_name = dirpath.split('/')[-1]
                    self.move_image(full_file_path, dirpath)


    def move_image(self, full_file_path, dirpath):
        directory_name = dirpath.split('/')[-1]
        file_name = full_file_path.split('/')[-1]
        full_folder_path = self.bad_images_dir + '/' + directory_name
        new_file_path = full_folder_path + '/' + file_name 
        
        mf.create_folder(full_folder_path)
        mf.move_file(full_file_path, new_file_path)        
        
    


Coordinator().invoke()


