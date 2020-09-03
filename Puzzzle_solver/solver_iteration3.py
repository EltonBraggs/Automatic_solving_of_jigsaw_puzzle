# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:38:17 2020

@author: Elton , Bhuvan
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
total_pixel_value_left = {}
total_pixel_value_right = {}
total_pixel_value_top = {}
total_pixel_value_bottom = {}
list_of_pixels ={}
average_of_pixels = {}
#element = None
key = None
list_of_sides_white= {}
element = []
img = None

def read_image(image):
    global img_width
    #print(image)
    #image = cv2.imread("Piece_4.png", cv2.IMREAD_COLOR)
    crop_img = image[200:800, 400:1200]
    print(crop_img)
    #plt.imshow(crop_img)
    img =cv2.resize(crop_img  , (512, 256))
    plt.imshow(img)
    return img
    
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

def pixel_extraction_left(img , element1):
    global left_side_pixel_value , list_of_sides_white
    list_left =[]
    left_side_pixel_value = []
    print(element1)
    list_left = list_of_sides_white[element1][0]
    #print(list_of_sides_white[element1][0])
    print(img)
    for x in list_left:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        left_side_pixel_value.append(img[y2 , y1])
    return left_side_pixel_value

    
    
    
def pixel_extraction_right(img , element1):
    global right_side_pixel_value , list_of_sides_white
    list_right =[]
    list_left = list_of_sides_white[element1][2]
    right_side_pixel_value = []
    for x in list_right:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        right_side_pixel_value.append(img[y2 , y1])
    return right_side_pixel_value

def pixel_extraction_top(img , element1):
    global top_side_pixel_value , list_of_sides_white
    list_top =[]
    #print(element1)
    list_top = list_of_sides_white[element1][1]
    top_side_pixel_value = []
    for x in list_top:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        top_side_pixel_value.append(img[y2 , y1])
    return top_side_pixel_value

def pixel_extraction_bottom(img, element1):
    global bottom_side_pixel_value , list_of_sides_white
    list_bottom =[]
    list_bottom = list_of_sides_white[element1][3]
    bottom_side_pixel_value = []
    for x in list_bottom:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        bottom_side_pixel_value.append(img[y2 , y1])
    return bottom_side_pixel_value

def var_return(list_of_sides_white):
    global  element
    for key in list_of_sides_white.keys():
        element.append(key)
    return element
        
def main():
    global element
    global left_side_pixel_value
    global list_of_sides_white , list_of_pixels , average_of_pixels
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
        print(img)
        element = var_return(list_of_sides_white)
        #print(element)
        elm = file1[count]
        #elm = "'%s'" %(element[count])
        #print(elm)
        left_side_pixel_value = pixel_extraction_left(img , elm)
        left_side_pixel_value = np.array(left_side_pixel_value)
        mean_left_side = np.mean(left_side_pixel_value , axis=0) 
        top_side_pixel_value = pixel_extraction_top(img , elm)
        top_side_pixel_value = np.array(top_side_pixel_value)
        mean_top_side = np.mean(top_side_pixel_value , axis=0) 
        
        right_side_pixel_value = pixel_extraction_right(img , elm)
        right_side_pixel_value = np.array(right_side_pixel_value)
        mean_right_side = np.mean(right_side_pixel_value , axis=0) 
        bottom_side_pixel_value = pixel_extraction_bottom(img , elm)
        bottom_side_pixel_value = np.array(bottom_side_pixel_value)
        mean_bottom_side = np.mean(bottom_side_pixel_value , axis=0) 
        #print(left_side_pixel_value)
        #print("%s : %s " % (elm, left_side_pixel_value))
        total = [left_side_pixel_value , top_side_pixel_value , right_side_pixel_value, bottom_side_pixel_value]
        list_of_pixels.update({elm:total})
        total_pixel_average = [mean_left_side , mean_top_side , mean_right_side , mean_bottom_side]
        average_of_pixels.update({elm:total_pixel_average})
        #print(top_side_pixel_value)
        #print(right_side_pixel_value)
        #print(bottom_side_pixel_value)
        count = count +1
    #print(list_of_pixels)
    print(average_of_pixels)
    #print(list_of_pixels['Piece_8.png'][0])
    
    
    
            
        
        
     
    
if __name__== "__main__" :
        main()