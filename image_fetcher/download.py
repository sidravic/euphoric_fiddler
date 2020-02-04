from fastai.vision import download_images, verify_images
from fastai.vision import pathlib
import os
import time

def download(product_path):
    try:
        urls_path = product_path/'urls.txt'
        download_images(urls_path, dest=product_path, max_workers=3, timeout=30)
    except Exception as e:
        print(f'Error raised {e}')
        print(traceback.print_exc())


def verify(product_path):
    verify_images(product_path, delete=True, img_format='jpg', max_workers=4)


def download_all_images(base_dir):
    pathlib.PosixPath(base_dir)
    for dirpath, _dirnames, files in os.walk(base_dir):
        product_path = pathlib.PosixPath(dirpath)
        print(f'Downloading from {product_path.__str__()}')

        if product_path.name == 'internal_v3':
            continue

        if len(files) > 2:
            print(f'Already processed folder {product_path.__str__()}. Moving on!')
            continue

        time.sleep(2)
        download(product_path)
        verify(product_path)




# product_path = pathlib.Path('/home/sidravic/downloaded_images/internal_v3/0f8f52d8-b78f-4904-b5e1-3e65136209b0')
# download(product_path)
# verify(product_path)


download_all_images('/home/sidravic/downloaded_images/internal_v3')