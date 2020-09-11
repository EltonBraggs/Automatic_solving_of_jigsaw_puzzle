# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:27:05 2020

@author: Elton
"""


import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.ndimage.filters as filters
import scipy.ndimage as ndimage

img = None
corners_list = []
tile_center = ()

def load_images_from_folder(folder):
    images = []
    files =[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            files.append(filename)
    return images, files

def read_image(image):
    #image = cv2.imread("Piece_4.png", cv2.IMREAD_COLOR)
    crop_img = image[200:800, 400:1200]
    #plt.imshow(crop_img)
    img =cv2.resize(crop_img  , (512, 256))
    plt.imshow(img)
    
    

    return img

def threshold_image(img):
    gray = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
    blurred_frame = cv2.GaussianBlur(gray, (3, 3), 0)
    ret,thresh = cv2.threshold(blurred_frame,127,255,cv2.THRESH_BINARY)
    plt.imshow(thresh)
    #hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    return thresh



def corner_detection(thresh, img):
    global corners_list
    corners = cv2.goodFeaturesToTrack(thresh,300,0.01,5)
    corners = np.int0(corners)
    ##print(corners)
    corners_list=[]
    img_with_corners = img.copy()
    ##print(corners.ravel())
    for i in corners:
        x,y = i.ravel()
        corners_list.append([x,y])
        img_with_corners = cv2.circle(img_with_corners,(x,y),3,255,-1)
    plt.imshow(img_with_corners),plt.show()
    #cv2.namedWindow('corners', cv2.WINDOW_NORMAL)
    #cv2.imshow('corners', img_with_corners)
    plt.imshow(img_with_corners)
    #key = cv2.waitKey(10000)
    #cv2.destroyAllWindows()
    #print(corners_list)
    #print(len(corners_list))
    return corners_list , corners

def rectangular_box(corners, img):
    global tile_center 
    rect = cv2.minAreaRect(corners)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    img_with_box = img.copy()
    img_with_box = cv2.drawContours(img_with_box,[box],0,(0,0,255),2)
    #print(box)
    #cv2.namedWindow("img_with_box" , cv2.WINDOW_NORMAL)
    #cv2.imshow("img_with_box", img_with_box)
    #key = cv2.waitKey(10000)
    #cv2.destroyAllWindows()
    plt.imshow(img_with_box)
    #Finding the center point of the rectangle
    center_x =int((box[1][0] + box[3][0])/2)
    center_y =int((box[1][1] + box[3][1])/2)
    #print(center_x)
    #print(center_y)
    img_center = cv2.circle(img_with_box, (center_x, center_y) , 3, (255,255,255),1)
    plt.imshow(img_center)
    tile_center= (center_x , center_y)
    tile_center = tuple(np.round(tile_center).astype(np.int))
    #print(tile_center)


    line1Y1 = box[0][1]
    line1X1 = box[0][0]
    line1Y2 = box[3][1]
    line1X2 = box[3][0]
    
    line2Y1 = 0
    line2X1 = 0
    line2Y2 = 0
    line2X2 = 512
    angle1 = math.atan2(line1Y1-line1Y2,line1X1-line1X2)
    angle2 = math.atan2(line2Y1-line2Y2,line2X1-line2X2)
    angleDegrees = (angle1-angle2) * 360 / (2*math.pi)
    print(angleDegrees)
    if angleDegrees <0:
        angleDegrees = 90 +angleDegrees 
    print(angleDegrees)
    img_rotated = ndimage.rotate(img, (angleDegrees))
    plt.imshow(img, cmap=plt.cm.gray)
    return img_rotated


def main():
    count = 0
    images, file = load_images_from_folder("Puzzle_pieces/Black")
    for image in images:
        img = read_image(image)
        thresh = threshold_image(img)
        corners_list , corners = corner_detection(thresh , img)
        img_rotated = rectangular_box(corners, img)
        plt.imshow(img_rotated)
        cv2.namedWindow("img_rotated" , cv2.WINDOW_NORMAL)
        cv2.imshow("img_rotated", img_rotated)
        cv2.waitKey(10000)
        cv2.destroyAllWindows()

if __name__== "__main__" :
        main()       