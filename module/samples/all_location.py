import os
import sys
from pathlib import Path
import os.path

preprocess_dir = Path(os.getcwd())
module_dir = preprocess_dir.parent
main_dir = module_dir.parent
datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')

sys.path.append(module_dir)
sys.path.append(self_module)
sys.path.append(preprocess_dir)

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
# plot locations of all stations
# -----------------------------------------------

os.chdir(main_dir)
info_v = read_excel('info_2019.xlsx')
info_o = read_excel('info_2020.xlsx')
info_wind = read_excel('info_wind.xlsx')

print(info_wind['풍향풍속'].unique())
wind_index = []
for index in range(info_wind.shape[0]) :
    if info_wind.loc[index, '풍향풍속'] == 'O' :
        wind_index.append(index)

print(info_wind.loc[wind_index, :])
print(len(wind_index))
        
wind_only = info_wind.loc[wind_index, :]
wind_only.to_excel('wind_only.xlsx')

print(info_wind.columns)
location = info_wind.loc[:, '시리얼번호' : '위도']
print(location.head())

location.to_excel('location.xlsx')


