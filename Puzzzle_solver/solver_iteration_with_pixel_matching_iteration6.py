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
import side_extractor_final_sept13
from side_extractor_final_sept13 import load_images_from_folder
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
matching_pixels = {}
pixel_matching_list = []

def read_image(image):
    global img_width
    #print(image)
    #image = cv2.imread("Piece_4.png", cv2.IMREAD_COLOR)
    crop_img = image[200:800, 400:1200]
    #print(crop_img)
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
    #print(len(final1_list))

def pixel_extraction_left(img , element1):
    global left_side_pixel_value , list_of_sides_white
    list_left =[]
    left_side_pixel_value = []
    #print(element1)
    list_left = list_of_sides_white[element1][0]
    #print(list_of_sides_white[element1][0])
    #print(img)
    for x in list_left:
        y1 = x[0]
        y2 = x[1]
        #print(y1)
        left_side_pixel_value.append(img[y2 , y1])
    return left_side_pixel_value

    
    
    
def pixel_extraction_right(img , element1):
    global right_side_pixel_value , list_of_sides_white
    list_right =[]
    list_right = list_of_sides_white[element1][2]
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
    global left_side_pixel_value , pixel_matching_list
    global list_of_sides_white , list_of_pixels , average_of_pixels , matching_pixels
    list_of_sides = side_extractor_final_sept13.main()
    file2 = []
    
    global img
    for i in list_of_sides:
        file2.append(i)
    #print("file2: " , file2)
        
    #print(list_of_sides)
    #print(list_of_sides['Piece_4.png'])
    images, file1 = load_images_from_folder("Puzzle_pieces/White/Test")
    #print("file1: " , file1)
    for i in range(len(file1)):
        list_of_sides_white = keys_swap(file2[i], file1[i], list_of_sides)
    #print(list_of_sides_white)
    #print("list of sides: " , list_of_sides_white['Piece_1.png'])
    count = 0
    for image in images:
        img = read_image(image)
        #print(img)
        element = var_return(list_of_sides_white)
        #print(element)
        elm = file1[count]
        #elm = "'%s'" %(element[count])
        #print(elm)
        left_side_pixel_value = pixel_extraction_left(img , elm)
        left_side_pixel_value = np.array(left_side_pixel_value)
        mean_left_side = np.mean(left_side_pixel_value , axis=0)
        #mean_left_side = mean_left_side.astype(float)
        mean_left_side = mean_left_side[~np.isnan(mean_left_side)]
        top_side_pixel_value = pixel_extraction_top(img , elm)
        top_side_pixel_value = np.array(top_side_pixel_value)
        mean_top_side = np.mean(top_side_pixel_value , axis=0)
        #mean_top_side = mean_top_side.astype(float)
        mean_top_side = mean_top_side[~np.isnan(mean_top_side)]
        
        right_side_pixel_value = pixel_extraction_right(img , elm)
        right_side_pixel_value = np.array(right_side_pixel_value)
        mean_right_side = np.mean(right_side_pixel_value , axis=0)
        #mean_right_side =mean_right_side.astype(float)
        mean_right_side = mean_right_side[~np.isnan(mean_right_side)]
        bottom_side_pixel_value = pixel_extraction_bottom(img , elm)
        bottom_side_pixel_value = np.array(bottom_side_pixel_value)
        mean_bottom_side = np.mean(bottom_side_pixel_value , axis=0)
        #mean_bottom_side= mean_bottom_side.astype(float)
        mean_bottom_side = mean_bottom_side[~np.isnan(mean_bottom_side)]
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
    #print(average_of_pixels)
    #average_of_pixels = 
    
    
    for item in average_of_pixels.items():
        #print(item[0][1])
        
        pixel_matching_list.append(item)
    #print('pixel matching list' , pixel_matching_list)
    count = 0
    for j in range(len(pixel_matching_list)):
        #print(count)
        #print(pixel_matching_list[j][0])
        #A=[]
        A = [pixel_matching_list[j][1][0], pixel_matching_list[j][1][1] , pixel_matching_list[j][1][2] , pixel_matching_list[j][1][3] ]
        
         

        #print('A' , A)
        #A = A.tolist()
        #print(A[1][0])
        for i in range(0,len(pixel_matching_list)):
            #print(pixel_matching_list[i][0])
            W = [np.array(0.1 * np.array(pixel_matching_list[i][1][0])) , np.array(0.1 * np.array(pixel_matching_list[i][1][1])) , np.array(0.1 * np.array(pixel_matching_list[i][1][2])) , np.array(0.1 * np.array(pixel_matching_list[i][1][3]))]
            D = [np.subtract((pixel_matching_list[i][1][0]) , W[0]) , np.subtract((pixel_matching_list[i][1][1]) , W[1]) ,  np.subtract((pixel_matching_list[i][1][2]) , W[2])  , np.subtract((pixel_matching_list[i][1][3]) , W[3]) ]
            
            E = [np.add((pixel_matching_list[i][1][0]) , W[0]) , np.add((pixel_matching_list[i][1][1]) , W[1]) ,  np.add((pixel_matching_list[i][1][2]) , W[2])  , np.add((pixel_matching_list[i][1][3]) , W[3]) ]
            
            #if len(pixel_matching_list[i][1][0]) == 0 or len(pixel_matching_list[i+1][1][0]) == 0 :
                #continue
            #else:
                #print('D' , D)
                #print('A' , A)
            #print(len(D))
            #print(len(A))
             
            for k in range(0 , len(A) , 1):
                print(pixel_matching_list[j][0])
                #print('k' , k)
                list_name1 = k
                #print(k)
                for m in range(0 , len(D) , 1):
                    print(pixel_matching_list[i][0])
                    #print('m' , m)
                    list_name = m
                    D[m][0] = round(D[m][0] , 2)
                    A[k][0] = round(A[k][0] , 2)
                    E[m][0] = round(E[m][0] , 2)
                    D[m][1] = round(D[m][1] , 2)
                    A[k][1] = round(A[k][1] , 2)
                    E[m][1] = round(E[m][1] , 2)
                    D[m][2] = round(D[m][2] , 2)
                    A[k][2] = round(A[k][2] , 2)
                    E[m][2] = round(E[m][2] , 2)
                    #print(("D[%s][0]"  %(m), D[m][0])  + ("A[%s][0]"  %(k), A[k][0])  + ("E[%s][0]"  %(m), E[m][0]))
                    #print(("D[%s][1]"  %(m), D[m][1])  + ("A[%s][1]"  %(k), A[k][1])  + ("E[%s][1]"  %(m), E[m][1]))
                    #print(("D[%s][2]"  %(m), D[m][2])  + ("A[%s][2]"  %(k), A[k][2])  + ("E[%s][2]"  %(m), E[m][2]))
                    
                    if ((D[m][0] <= A[k][0] <= E[m][0]) and (D[m][1] <= A[k][1] <= E[m][1]) and (D[m][2] <= A[k][2] <= E[m][2])):
                        #print('1')
                        matching_pixels.update({count:{pixel_matching_list[j][0]: A[k] , 'matching_side1' : list_name1 , pixel_matching_list[i][0] : pixel_matching_list[i][1][m] , 'matching_side' : list_name}})
                        count = count +1
                        #print(matching_pixels)
                    else:
                        print('pixel' + '' + ('%s'  %(pixel_matching_list[j][0])) + ' ,' + ('%s'  %(list_name1)) + ' ' + 'and' + ('%s'  %(pixel_matching_list[i][0])) + ' ,'  + ('%s'  %(list_name)) + ' ' + 'does not match' )
                        continue
        #count = count +1
        #print(count)
                       
            
        
    
    print(matching_pixels)
    #if np.subtract(tuple(pixel_matching_list[i][1][0]) , N) <= tuple(pixel_matching_list([i+1][1][0]) <= np.add(tuple(pixel_matching_list([i][1][0])),N): #and np.subtract(tuple(pixel_matching_list(i[1][0][1])) , N[1] ) <= tuple(int((i+1)[1][0][1])) <= np.add(tuple(int(i[1][0][1])) , N[1] ) and np.subtract(tuple(int(i[1][0][2])) , N[2]) <= tuple(int((i+1)[1][0][2])) <= np.add(tuple(int(i[1][0][2])) , N[2] ):

                
                
if __name__== "__main__" :
        main()