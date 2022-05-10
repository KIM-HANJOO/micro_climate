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
sample_time = os.path.join(sample_robby, 'time')
sample_only_time = os.path.join(sample_robby, 'only_available_time')

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
import outlier as out

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


def leap_year(year) :
    check = 0
    if (int(year) % 4 == 0) :
        if int(year) % 100 != 0 :
            if int(year) % 400 == 0 :
                check = 1
                
    if check == 1 :
        return True
    else :
        return False


def double_size(string) :
    if len(string) == 1 :
        return '0' + string
    else :
        return string
    
class NotAvailableError(Exception) :
    def __init__(self) :
        super().__init__('not available!') 


def date_avail(string) :

    available = 0 # 0 means available

    if string[4 : 6] == '00' :
        available = 1

    if string[6 : 8] == '00' :
        available = 1

    if available == 0 :
        return True
    else :
        return False

def sub_zero(string) :
    string = str(string)
    string = string.replace(',', '')
    if '0-' in string :
        return float(string[string.index('-') :])
    else :
        return float(string)

# -----------------------------------------------
# drop nan values in '등록일자'
# -----------------------------------------------


target_col = ['등록일자']
a = input(f'drop nan values in times (y/n)')

if a == 'y' :
    num_all = len(os.listdir(sample_time))
    for num_excel, excel in enumerate(os.listdir(sample_time)) :

        os.chdir(sample_time)
        temp = read_excel(excel)

        drop_index = []
        for index in range(temp.shape[0]) :
            if not pd.isna(temp.loc[index, '등록일자']) :
                print(temp.loc[index, '등록일자'])
                if not date_avail(str(temp.loc[index, '등록일자'])) :
                    print(f"register\tdropped\t{temp.loc[index, '등록일자']}")
                    temp.loc[index, '등록일자'] = np.nan


                if not date_avail(str(temp.loc[index, '전송시간'])) :
                    print(f"transmission\tdropped\t{temp.loc[index, '전송시간']}")
                    temp.loc[index, '전송시간'] = np.nan

            temp.loc[index, '기온'] = sub_zero(temp.loc[index, '기온'])

        temp.dropna(subset = ['등록일자'], inplace = True)
        temp.reset_index(drop = True, inplace = True)

        os.chdir(sample_only_time)
        temp.to_excel(excel)
        print(f'{num_excel + 1} / {num_all}\t{round(((num_excel + 1) / num_all) * 100, 2)}%')


# -----------------------------------------------
# check null values | outliers 
# -----------------------------------------------




# check null values percentages for each information

a = input('check null and outliers?(y/n)')

if a == 'y' :
    target_info_list = ['기온', '상대습도', '초미세먼지', '미세먼지'] #'풍속', '풍향'

    for target_info in target_info_list :

        df_outliers = pd.DataFrame(columns = ['excel', 'total_size', 'null', 'IQR', 'method', 'in-range'])
        num_outliers = 0

        num_all = len(os.listdir(sample_only_time))
        for num_excel, excel in enumerate(os.listdir(sample_only_time)) :
            os.chdir(sample_only_time)
            temp = read_excel(excel)
            if target_info == '기온' :
                for index in range(temp.shape[0]) :
                    temp.loc[index, '기온'] = sub_zero(temp.loc[index, '기온'])

            if temp.shape[0] == 0 :
                df_outliers.loc[num_outliers, :] = [excel, 0, 'no_index', 'no_index', 'no_index', 'no_index']
                num_outliers += 1

            else :

                null_num = temp[target_info].isnull().sum()
                
                if null_num == temp.shape[0] :
                    df_outliers.loc[num_outliers, :] = [excel, temp.shape[0], null_num, 0, 0, 'none', 0, 0]
                    num_outliers += 1


                else :
                    target = temp[target_info].dropna().tolist()
                    iqr_non, iqr = out.out_box(target, 1.5)

                    iqr_num = len(iqr)

                    left_num = temp.shape[0] - null_num - iqr_num

                    method_used = 'iqr'
                        

                    df_outliers.loc[num_outliers, :] = [excel, temp.shape[0], null_num, iqr_num, method_used, left_num]
                    num_outliers += 1
            print(f'{num_excel} / {num_all}')

        os.chdir(os.path.join(sample_plot, 'null_outliers_check'))
        df_outliers.to_excel(f'{target_info}_null_outliers_check.xlsx')
        print(df_outliers)

