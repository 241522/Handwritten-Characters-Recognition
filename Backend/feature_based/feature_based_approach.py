#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pathlib

import cv2
import numpy
import numpy as np
import os


# In[2]:
import pathlib as pathlib

import PIL.Image

sift = cv2.SIFT_create()


# In[3]:


def findDescriptors(images):
    descriptors_list = []
    for img in images:
        key_points, descriptor = sift.detectAndCompute(img, None)
        descriptors_list.append(descriptor)
    return descriptors_list


# In[4]:


def findLabel(img, descriptors_list, threshold = 15):
    test_key_points, test_descriptor = sift.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    match_list = []
    finalValue = -1
    try:
        for descriptor in descriptors_list:
            matches = bf.knnMatch(descriptor, test_descriptor, k = 2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])

            match_list.append(len(good))
        print(match_list)
    except:
        print("WARNING, knn match EXCEPTION")
        pass
    
    if len(match_list) != 0:
        if max(match_list) > threshold:
            finalValue = match_list.index(max(match_list))
            
    return finalValue


# In[5]:


def resize(img):
    if img.shape[0] > 50 and img.shape[1] > 50:
        return img
    
    scale_percent = 220 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    return img


# In[6]:


prefix = pathlib.Path(__file__).parent.joinpath('1/ImagesTest')
path = pathlib.Path(__file__).parent.joinpath('1/ImagesBase')

images = []
class_names = []
my_list = os.listdir(path)

print('Total classes detected', len(my_list))

for cl in sorted(my_list):
    current_img = cv2.imread(f'{path}/{cl}', 0)
    current_img = resize(current_img)
    images.append(current_img)
    class_names.append(os.path.splitext(cl)[0])

print(class_names)


# In[7]:


descriptors_list = findDescriptors(images)

print(len(descriptors_list))


# In[8]:


def detectCharacter(file):

    pil_image = PIL.Image.open(file)
    opencvImage = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_BGR2GRAY)
    test_img = resize(opencvImage)
    
    indx = findLabel(test_img, descriptors_list)
    
    result = "NOT FOUND"
    if indx != -1:
        result = class_names[indx]
    cn= class_names
    print("result: ", result)
    
    return result


# In[9]

