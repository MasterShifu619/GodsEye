from PIL import Image, ImageOps
from keras.models import Model, load_model
import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import cv2
# import numpy as np
# import argparse
import os
# import csv
# import time
# from random import randint

model = load_model(r'C:/Users/Bipin Gowda/PycharmProjects/GodsEye/model2.h5')
IMG_SIZE=50

def add_border(name, border, color=0):
    img = Image.open('C:/Users/Bipin Gowda/PycharmProjects/GodsEye/output/'+name)
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=color)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    return bimg

def img_classify(img,iname):
    #img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (IMG_SIZE,IMG_SIZE))
    pred = model.predict(gray.reshape(1, IMG_SIZE, IMG_SIZE, 1))
    if pred[0][0] > pred[0][1]:
        bimg=add_border(iname,border=50,color='green')
    else:
        bimg=add_border(iname,border=50,color='red')
        bimg.save('C:/Users/Bipin Gowda/PycharmProjects/GodsEye/api/media/output_frames/' + iname)
    os.remove('C:/Users/Bipin Gowda/PycharmProjects/GodsEye/output/'+iname)
    bimg.save('C:/Users/Bipin Gowda/PycharmProjects/GodsEye/output/'+iname)