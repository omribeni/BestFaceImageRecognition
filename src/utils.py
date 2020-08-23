import base64
import os
import json

import PIL
from PIL import Image
from werkzeug.exceptions import BadRequest


class Utils(object):


    @classmethod
    def get_image_resolution(cls, path):
        # calculate image resolution
        image = PIL.Image.open(path)
        width, height = image.size
        return width,height

    @classmethod
    def validate_image_file(cls, path):
        pass

    @classmethod
    def parse_json_images_data(cls, data):
        json_data = json.loads(data.decode('utf-8'))
        image_paths = json_data.get('data')
        if image_paths:
            images = []
            for img in image_paths:
                img_path = img.get('path')
                if not img_path:
                    raise BadRequest('no path of image')
                cls.validate_image_file(img_path)
                images.append(img_path)
            return images
        else:
            return None