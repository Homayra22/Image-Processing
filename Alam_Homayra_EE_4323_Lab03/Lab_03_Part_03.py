#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:00:03 2021

@author: homayra
"""


import numpy as np
import cv2
import histogram_plotter
import matplotlib.pyplot as plt

image1=cv2.imread("cell.jpeg",0)
equ=cv2.equalizeHist(image1)
clahe=cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
clahe_img=clahe.apply(image1)

histogram_plotter.his_img(image1)
histogram_plotter.his_img(equ)
histogram_plotter.his_img(clahe)

cv2.imshow("Original Image",image1)
cv2.imshow("Hist_equ",equ)
cv2.imshow("CLAHEequ",clahe_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
