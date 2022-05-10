import os
import sys
from pathlib import Path
import os.path

#   < directory paths >
samples_module_dir = Path(os.getcwd())
sample_robby = samples_module_dir.parent
sample_data = os.path.join(sample_robby, 'data')
sample_info = os.path.join(sample_robby, 'info')
sample_plot = os.path.join(sample_robby, 'plot')

main_dir = sample_robby.parent
module_dir = os.path.join(main_dir, 'module')

datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
info_dir = os.path.join(main_dir, 'info_data')
preprocessed_dir = os.path.join(main_dir, 'preprocessed')


#   add dirs to sys.path

sys.path.append(module_dir)
sys.path.append(self_module)


#   import packages

import directory_change as dich
import discordlib_pyplot as dlt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "/mnt/c/Users/joo09/Documents/Github/fonts/D2Coding.ttf"
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

import glob
import math
import random
import scipy.stats
import shutil
import time


'''
note

basic functions
'''

cwdir = os.getcwd()

def read_excel(excel) :
    df = pd.read_excel(excel)
    if 'Unnamed: 0' in df.columns :
        df.drop('Unnamed: 0', axis = 1, inplace = True)

    if 'Unnamed: 0.1' in df.columns :
        df.drop('Unnamed: 0.1', axis = 1, inplace = True)

    return df


def read_csv(excel) :
    #df = pd.read_csv(excel, encoding = "utf-16")
    #df = pd.read_csv(excel, encoding = "ISO-8859-1")
    df = pd.read_csv(excel, encoding = "cp949")
    
    return df

def ave(list1) :
	return sum(list1) / len(list1)

# -----------------------------------------------
# move sample stations from datas_dir to sample_data 
# -----------------------------------------------

serials_dir = os.path.join(preprocessed_dir, 'merged')

os.chdir(sample_info)
info = read_excel('samples_32.xlsx')

sample_serials = info.loc[:, '시리얼번호'].tolist()

os.chdir(serials_dir)
all_samples = len(sample_serials)
non_list = []
for st_num, station in enumerate(sample_serials) :
    excel_name = f'{station}.xlsx'

    if excel_name in os.listdir(serials_dir) :
        dich.copyfile(serials_dir, sample_data,  excel_name)
        print(f'{st_num} / {all_samples}\t{round((st_num/all_samples) * 100, 2)}%')

    else :
        print(f'{excel_name} not in directory')
        non_list.append(excel_name)

print('sample datas all moved to a new house')

print(non_list)
print(len(non_list), all_samples)

