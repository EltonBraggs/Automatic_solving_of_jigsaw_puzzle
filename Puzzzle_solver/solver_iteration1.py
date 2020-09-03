# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:38:17 2020

@author: Elton
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import side_extractor_final_aug24
from side_extractor_final_aug24 import load_images_from_folder
#from side_extractor_final_aug24 import read_image

left_side_pixel_value = []
top_side_pixel_value = []
right_side_pixel_value = []
bottom_side_pixel_value = []
#element = None
key = None
list_of_sides_white= {}
element = []
img = None

def read_image(image):
    #print(image)
    #image = cv2.imread("Piece_4.png", cv2.IMREAD_COLOR)
    crop_img = image[200:800, 400:1200]
    #plt.imshow(crop_img)
    img =cv2.resize(crop_img  , (512, 256))
    plt.imshow(img)
    
def keys_swap(orig_key, new_key, d):
    d[new_key] = d.pop(orig_key)
    return d

def extra_functions():
    final_list = []
    for i in list_of_sides_white:
        (final_list.append(list_of_sides_white[i]))
        #for j in i
        #for j in i:
    #print("first_picture", final_list[0]) 
    #print(len(final_list[0]))
    #print(len(final_list))
    final1_list = []
    for i in final_list:
        for j in i:
            final1_list.append(j)
    #print(len(final_list[0]))
    print(len(final1_list))

def pixel_extraction_left(img , list_of_sides_white , element1):
    global left_side_pixel_value
    list_left =[]
    print(element1)
    list_left = list_of_sides_white[element1][0]
    #print('1')
    for x in list_left:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        left_side_pixel_value.append(img[y2 , y1])
    
    
    
def pixel_extraction_right(img , list_of_sides_white , element1):
    global right_side_pixel_value
    list_right =[]
    list_left = list_of_sides_white[element1][2]
    for x in list_right:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        right_side_pixel_value.append(img[y2 , y1])

def pixel_extraction_top(img , list_of_sides_white , element1):
    global top_side_pixel_value
    list_top =[]
    print(element1)
    list_top = list_of_sides_white[element1][1]
    for x in list_top:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        top_side_pixel_value.append(img[y2 , y1])

def pixel_extraction_bottom(img, list_of_sides_white , element1):
    global bottom_side_pixel_value
    list_bottom =[]
    list_bottom = list_of_sides_white[element1][3]
    for x in list_bottom:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        bottom_side_pixel_value.append(img[y2 , y1])

def var_return(list_of_sides_white):
    global  element
    for key in list_of_sides_white.keys():
        element.append(key)
    return element
        
def main():
    global element
    global left_side_pixel_value
    global list_of_sides_white
    list_of_sides = side_extractor_final_aug24.main()
    file2 = []
    global img
    for i in list_of_sides:
        file2.append(i)
    #print("file2: " , file2)
        
    #print(list_of_sides)
    #print(list_of_sides['Piece_4.png'])
    images, file1 = load_images_from_folder("Puzzle_pieces/White")
    #print("file1: " , file1)
    for i in range(len(file1)):
        list_of_sides_white = keys_swap(file2[i], file1[i], list_of_sides)
    #print(list_of_sides_white)
    #print("list of sides: " , list_of_sides_white['Piece_1.png'])
    count = 0
    for image in images:
        img = read_image(image)
        element = var_return(list_of_sides_white)
        print(element)
        #elm = '%s' % element[count]
        elm = '%s' %(element[count])
        print(elm)
        left_side_pixel_value = pixel_extraction_left(img , list_of_sides_white , elm) 
        top_side_pixel_value = pixel_extraction_top(img , list_of_sides_white , elm)
        right_side_pixel_value = pixel_extraction_right(img , list_of_sides_white , elm)
        bottom_side_pixel_value = pixel_extraction_bottom(img , list_of_sides_white , elm)
        count = count +1
    print(left_side_pixel_value)
    
    
            
        
        
     
    
if __name__== "__main__" :
        main()