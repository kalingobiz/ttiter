# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 02:27:46 2020

@author: kalingolive
"""

import pandas as pd
import cv2 as cv
import basic
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
#data = pd.read_csv("list.csv")
#y = np.array(data)

files="ghjg"
#size2=basic.size
def shrink(x):
    image=basic.adjustim3(x)
    image = image.take(range(0, basic.finalsizex), axis=0).take(range(0, basic.finalsizey), axis=1)
    # image = cv.resize(image, (32, 32), interpolation=cv.INTER_CUBIC)
    #image = np.double(np.round((1.2 * np.log(image))))
    s = np.empty([basic.size, 2], dtype=int)
    s2 = np.empty([basic.size, 2], dtype=int)
    c = 0
    c2 = 0
    o = np.zeros((60, 80), dtype=int)
    o2 = np.zeros((60, 80), dtype=int)
    '''for a in range(image.shape[0]):
        for b in range(image.shape[1]):
            if image[a][b] == 1:
                image[a][b] = 1
            else:
                image[a][b] = 0'''
    k = 0
    k2 = 0
    for r2 in range(image.shape[1]):
        #print(image[r])
        if np.max(image[:,r2]) == 0:
            
            c2 = c2 + 1
        else:
            s2[k2][0] = r2
            k2 = k2 + 1
            c2 = 0
    #print(s2[0][0])    
    for r in range(image.shape[0]):
        #print(image[r])
        if np.max(image[r]) == 0:
            
            c = c + 1
        else:
            s[k][0] = r
            k = k + 1
            c = 0
     
    #print("first",s2[0][0])
    image2 = image.take(range(s[0][0], basic.finalsizex - c), axis=0).take(range(s2[0][0], basic.finalsizey-c2), axis=1)
    # print(60-image2.shape[0])
    #o = np.append(image2, np.int8(np.zeros((basic.size - image2.shape[0]) * basic.size))).reshape(basic.size, basic.size)
    # v = v
    # o = v
    image2 = cv.resize(image2, (basic.finalsizex, basic.finalsizey), interpolation=cv.INTER_NEAREST)
    # o = cv.dilate(o, kernel, iterations=1)
    # o = cv.erode(o, kernel, iterations=1)
    #o = o.take(range(0, basic.finalsizex), axis=0).take(range(30, 120), axis=1)
    #o = cv.resize(o, (16, 16), interpolation=cv.INTER_CUBIC)

    return image2

