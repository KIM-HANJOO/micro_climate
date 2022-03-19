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
# brief plot of samples 
# -----------------------------------------------

os.chdir(sample_info)
info = read_excel('samples_32.xlsx')
print(info.head())
print(info.columns)

fig = plt.figure(figsize = (7, 7))

target_station_info = ['높이', '위도', '경도']
target_measure_info = ['미세먼지', '초미세먼지', '온도', '상대습도', '풍향풍속']

## for columns in target_station_info, non of the columns had null values

#df_station_info = pd.DataFrame(columns = target_station_info)
#df_measure_info = pd.DataFrame(columns = target_measure_info)
#
#for col in target_station_info :
#    df_station_info.loc[0, col] = info.loc[:, col].isnull().sum()
#
#print(df_station_info)


## check whether each stations can measure each info or not

for target_col in target_measure_info :
    print(target_col)
    print(info[target_col].unique())

    







