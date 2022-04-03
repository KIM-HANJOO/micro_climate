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
sample_typo = os.path.join(sample_robby, 'typo')

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
# import location plotting 
# -----------------------------------------------

import geopandas as gpd
from shapely.geometry import Point, Polygon, LineString

def plot_location(location, plot_dir) :
    os.chdir(os.path.join(main_dir, 'shape_file', 'EMD_202101'))
    emd = gpd.read_file('TL_SCCO_EMD.shx')

    location.columns = ['경도', '위도']
    seoul_emd = emd[emd['EMD_CD'].str.startswith('11')]

    location['geometry'] = location.apply(lambda row : Point([row['경도'], row['위도']]), axis = 1)
    location = gpd.GeoDataFrame(location, geometry = 'geometry')
    location.crs = {'init' : 'epsg:4326'}
    location = location.to_crs({'init' : 'epsg:5179'})
            

    save_name = 'plot_location_samples32'
    figsize_set = (9, 9)
    title = 'samples, 32 (latest)'
    mark_size = 15
    mark_color = 'red'

    fig = plt.figure(figsize = figsize_set)
    ax = fig.add_subplot(1, 1, 1)

    seoul_emd.boundary.plot(ax = ax, color = 'black', linewidth = 0.3)
    location.plot(ax = ax, color = mark_color, markersize = mark_size)
    plt.title(title)


    a = input('save and send to discord.bot? (y/n)')

    if a == 'y' :
        os.chdir(plot_dir)
        dlt.savefig(plot_dir, f'{save_name}.png', 400)
        plt.savefig(f'{save_name}.png', dpi = 400, pad_inches = 0, bbox_inches = 'tight')

os.chdir(samples_module_dir)
print(os.listdir(samples_module_dir))
#emd = gpd.read_file('TL_SCCO_EMD.shx')
os.chdir(sample_info)
info_32 = read_excel('samples_32.xlsx')
info_32 = info_32.loc[:, ['경도', '위도']]

print(info_32)

plot_location(info_32, sample_plot)
