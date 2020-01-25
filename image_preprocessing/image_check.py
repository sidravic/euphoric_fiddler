import os
from PIL import Image


class ValidImageCheck:
    def __init__(self, image_path):
        self.image_path = image_path
        self.loaded_image = None

    def validate(self):
        return self.is_valid_image() and self.is_jpeg()

    def is_valid_image(self):
        try:
            self.loaded_image = Image.open(self.image_path)
            return True
        except OSError as os_error:
            return False

    def is_jpeg(self):
        return self.loaded_image.format == 'JPEG'




