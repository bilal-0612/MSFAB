#!/usr/bin/env python

import pickle as pkl

import numpy
from tqdm import tqdm
  
from PIL import Image    
import cv2 
import os
    

paths= ["train/img" ]
labels = ["train/caption.txt"]


outFile = 'offline-train-new.pkl' 
outlabel= 'test-caption-new.txt'
oupFp_feature = open(outFile, 'wb')  
file_label = open(outlabel,'w')
features = {}
channels = 1
sentNum = 0



for image_path in tqdm(paths):
    for i in os.listdir(image_path):
        #print(i)
        key = str(i.split('.')[0])
        if os.path.exists(image_path + '/' + key + '.png' ):
            image_file = image_path + '/' + key + '.png' 
        else:
            image_file = image_path + '/' + key + '.bmp' 
        #print(image_file)
        im = cv2.imread(image_file)

        if im is not None:
            mat = numpy.zeros([channels, im.shape[0], im.shape[1]], dtype='uint8')  
            for channel in range(channels):
                mat[channel, :, :] = im[:,:,0] # 3 channel -> 1 channel
            sentNum = sentNum + 1
            features[key] = mat



for filename in labels:
    idx = 0  
    for line in open(filename):  
        file_label.writelines(line)  
        idx +=1
        
    
file_label.close()

print('load images done. sentence number ', sentNum)

pkl.dump(features, oupFp_feature)
print('save file done')
oupFp_feature.close()







