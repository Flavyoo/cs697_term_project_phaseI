"""
Wrapper class to save names of images files
"""
import cv2 as cv

class ImageWrapper:
    def __init__(self, img_file_name, path):
        self.image = cv.imread(path)
        self._name = img_file_name

    def __str__(self):
        return self._name
