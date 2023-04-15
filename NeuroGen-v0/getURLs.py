#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 17:20:06 2022

@author: saeedeh
"""
import glob
import os
import pandas as pd
from os import walk

inv=False;


img_dir="/home/saeedeh/Desktop/Projects/github/sensoryValence-onlineStudy/NeuroGen-v0"

prefix='inv'
mypath=os.path.join(img_dir,'neg-'+prefix)
neg_img = next(walk(mypath), (None, None, []))[2]

mypath=os.path.join(img_dir,'pos-'+prefix)
pos_img = next(walk(mypath), (None, None, []))[2]


pos_pre='raw.githubusercontent.com/saeedeh/sensoryValence-onlineStudy/main/NeuroGen-v0/pos-'+prefix+'/'
pos_urls=[pos_pre+s for s in pos_img]

neg_pre='raw.githubusercontent.com/saeedeh/sensoryValence-onlineStudy/main/NeuroGen-v0/neg-'+prefix+'/'
neg_urls=[neg_pre+s for s in neg_img]


## Save all
dict1={'url': pos_urls, 'fname':pos_img, 'val_type': 'pos'}
dict2={'url': neg_urls, 'fname':neg_img, 'val_type': 'neg'}
df=pd.DataFrame(dict1).append(pd.DataFrame(dict2))
df.to_csv('URLs/'+prefix+'_urls.csv')


## Split into N
N=2
import random
random.seed(10)
def split(a, n):
    k, m = divmod(len(a), n)
    res= [a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]
    return res
import os
def shuffle_together(test_list1, test_list2):
    temp = list(zip(test_list1, test_list2))
    random.shuffle(temp)
    res1, res2 = zip(*temp)
# res1 and res2 come out as tuples, and so must be converted to lists.
    return list(res1), list(res2)

#os.chdir(os.path.dirname(os.path.abspath(__file__)))

## Shuffle
pos_urls1,pos_img1 = shuffle_together(pos_urls, pos_img)
neg_urls1,neg_img1 = shuffle_together(neg_urls, neg_img)

## split
pos_chunks = split(pos_urls1, N)
neg_chunks = split(neg_urls1, N)

posImg_chunks = split(pos_img1, N)
negImg_chunks = split(neg_img1, N)


for i in range(N):
    outFile=os.path.join(os.getcwd(),'URLs',prefix+'_split'+str(N)+'chunk'+str(i+1)+'.csv' )
    dict1={'url': pos_chunks[i], 'fname':posImg_chunks[i], 'val_type': 'pos'}
    dict2={'url': neg_chunks[i], 'fname':negImg_chunks[i], 'val_type': 'neg'}
    df=pd.DataFrame(dict1).append(pd.DataFrame(dict2))
    df.to_csv(outFile)



