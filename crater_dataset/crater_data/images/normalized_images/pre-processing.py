"""
Flavio Andrade
4-6-18

This program normalizes the size of the images to be fed into the neural
network. Crater and non-crater images are in different sizes and are then
resized into 200 x 200 pixels with added padding.
"""
import cv2 as cv
from imagewrapper import ImageWrapper
import os


BLUE = [255, 0, 0]
NEW_SIZE = 200
# REPLACE SRC1, DEST1, SRC2, and DEST2 with your absolute path to the directories

SRC1  = "/Users/flavioandrade/Desktop/Homework/480_Big_Data/Project/cs697_term_project_phaseI/crater_dataset/crater_data/images/tile3_24/crater"
DEST1 = "/Users/flavioandrade/Desktop/Homework/480_Big_Data/Project/cs697_term_project_phaseI/crater_dataset/crater_data/images/normalized_images/crater/"

SRC2  = "/Users/flavioandrade/Desktop/Homework/480_Big_Data/Project/cs697_term_project_phaseI/crater_dataset/crater_data/images/tile3_24/non-crater"
DEST2 = "/Users/flavioandrade/Desktop/Homework/480_Big_Data/Project/cs697_term_project_phaseI/crater_dataset/crater_data/images/normalized_images/non-crater/"

def paddingMakeborder(file_name, path):
    image = ImageWrapper(file_name, path)
    img_dim = image.image.shape
    height, width = img_dim[0], img_dim[1]
    wp = (NEW_SIZE - width) / 2   # padding for the width
    hp = (NEW_SIZE - height) / 2  # padding for the height
    # new image
    constant = cv.copyMakeBorder(image.image,hp,hp,wp,wp,cv.BORDER_CONSTANT,value=BLUE)
    normalized = (constant, 'normalized_' + str(image))
    return normalized


def readImages(src, dest):
    files = os.listdir(src)
    for image_file in files:
        normalized = paddingMakeborder(image_file, src + '/' + image_file)
        cv.imwrite(dest + normalized[1], normalized[0])


if __name__ == '__main__':
    readImages(SRC1, DEST1)
    readImages(SRC2, DEST2)
