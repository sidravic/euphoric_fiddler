import os
from os import path
import numpy as np
import json


def create_folder(full_folder_path):
    if not path.exists(full_folder_path):
        os.mkdir(full_folder_path)
        print(f'Creating folder: {full_folder_path}')
    else:
        print(f'Folder exists: {full_folder_path}')

    return None


def save_image_urls(full_folder_path, image_urls):
    print(f'{full_folder_path}')
    print(f'{image_urls}')

    urls_file_path = f'{full_folder_path}/urls.txt'
    urls_file = open(urls_file_path, 'ab')
    np.savetxt(urls_file, image_urls, delimiter='\n', encoding='utf-8', fmt='%s')
    urls_file.close()
    return


def save_metadata(full_folder_path, product_name, brand_name, _image_urls):
    metadata_file_path = f'{full_folder_path}/metadata.json'
    metadata = {
        'product_name': product_name,
        'brand_name': brand_name
    }

    with open(metadata_file_path, 'w') as metadata_file:
        json.dump(metadata, metadata_file, ensure_ascii=False, indent=4)

    return


class ImageUrlFileGenerator():
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def generate_url_txt_file(self, product_id, image_urls, product_name, brand_name):
        print(f'ProductID: {product_id}')

        full_folder_path = self.__get_full_folder_path(product_id)
        create_folder(full_folder_path)
        save_image_urls(full_folder_path, image_urls)
        save_metadata(full_folder_path, product_name, brand_name, image_urls)

        return None

    def __get_full_folder_path(self, product_id):
        return f'{self.base_dir}/{product_id}'
