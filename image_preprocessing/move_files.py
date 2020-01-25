import os
from os import path
import shutil 


def move_file(src_file_path, destination_file_path):
    print(f'Moving {src_file_path} --> {destination_file_path}')
    return os.rename(src_file_path, destination_file_path)


def create_folder(full_folder_path):       
    if not path.exists(full_folder_path):
        return os.mkdir(full_folder_path)
    
    return None


def copy_file(src_file_path, destination_file_path):
    print(f'Copying {src_file_path} --> {destination_file_path}')
    return shutil.copyfile(src_file_path, destination_file_path)
