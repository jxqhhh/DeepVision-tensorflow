# File: common.py
# Author: Qian Ge <geqian1001@gmail.com>

import os

import numpy as np


def get_file_list(file_dir, file_ext):
    assert file_ext in ['.mat', '.png', '.jpg', '.jpeg']
    re_list = []
    return np.array([os.path.join(root, name)
        for root, dirs, files in os.walk(file_dir) 
        for name in files if name.lower().endswith(file_ext)])
    # for root, dirs, files in os.walk(file_dir):
    #     for name in files:
    #         if name.lower().endswith(file_ext):
    #             re_list.append(os.path.join(root, name))
    # return np.array(re_list)

def get_folder_list(folder_dir):
    return np.array([os.path.join(folder_dir, folder) 
                    for folder in os.listdir(folder_dir) 
                    if os.path.join(folder_dir, folder)]) 

def get_folder_names(folder_dir):
    return np.array([name for name in os.listdir(folder_dir) 
                    if os.path.join(folder_dir, name)])    

def input_val_range(in_mat):
    # TODO to be modified    
    max_val = np.amax(in_mat)
    min_val = np.amin(in_mat)
    if max_val > 1:
        max_in_val = 255.0
        half_in_val = 128.0
    elif min_val >= 0:
        max_in_val = 1.0
        half_in_val = 0.5
    else:
        max_in_val = 1.0
        half_in_val = 0
    return max_in_val, half_in_val

def tanh_normalization(data, half_in_val):
    return (data*1.0 - half_in_val)/half_in_val

