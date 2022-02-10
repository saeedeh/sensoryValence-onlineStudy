#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 17:20:06 2022

@author: saeedeh
"""
import glob
import os
img_dir="/home/saeedeh/Desktop/Projects/github/sensoryValence-onlineStudy/stimuli"
neg_images = glob.glob(os.path.join(img_dir,'neg-img', '*.jpg'))
pos_images = glob.glob(os.path.join(img_dir,'pos-img', '*.jpg'))