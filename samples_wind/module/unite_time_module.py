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


def unite_para_time(excel) :

    for column in excel.columns : 
        if '전송시간' in column :
            time_sent = column

        elif '등록일자' in column :
            time_saved = column

    for num_index, index in enumerate(range(excel.shape[0])) :
        if num_index < 3 :
            excel.loc[index, time_sent] = unite_para_time_unit(excel.loc[index, time_sent])
            
            excel.loc[index, time_saved] = unite_para_time_unit(excel.loc[index, time_sent])
            print(f'{index} done', end = '\r')

    return excel

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

# -----------------------------------------------
# unite_para_time for all found formats
# -----------------------------------------------

def unite_time(string) :

    string = str(string)
    string_old = string

    split_list = []

    # <<<<<<<<<<<<<<<<<<<<<<<<<<
    # for format "2020-4-1 13:00"
    # >>>>>>>>>>>>>>>>>>>>>>>>>>

    if ':' in string :
        if '-' in string :
            if ('PM' not in string) & ('AM' not in string) :
               print("format 2020-4-1 1:00")
                
                string_left = string

                # convert '2020.4.'
                for itera in range(2) :
                    target_string = '-'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if len(temp_left) == 1 :
                        temp_left = '0' + temp_left

                    split_list.append(temp_left)
                    string_left = temp_right
                
                # convert '1 '
                for itera in range(1) :
                    target_string = ' '
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right
                    
                # convert '1:'
                for itera in range(1) :
                    target_string = ':'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right

                # for left ('00')
                split_list.append(double_size(string_left))

                print(f'{string_old}\t->\t{"".join(split_list)}')

            elif ('PM' in string) | ('AM' in string) :
#               print("format 2020.4.1 1:00 PM")
                
                string_left = string

                # convert '2020.4.' (year, month)
                for itera in range(2) :
                    target_string = '-'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if len(temp_left) == 1 :
                        temp_left = '0' + temp_left

                    split_list.append(temp_left)
                    string_left = temp_right
                
                # convert '1 ' (day)
                for itera in range(1) :
                    target_string = ' '
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right
                    
                # convert '1:' (hour)
                for itera in range(1) :
                    target_string = ':'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if 'PM' in string :
                        if temp_left != '12' :
                            temp_left = str(int(temp_left) + 12)

                    elif 'AM' in string :
                        if temp_left == '12' :
                            temp_left = '00'


                    split_list.append(double_size(temp_left))
                    string_left = temp_right

                # for left ('00')
                split_list.append(double_size(string_left[ : string_left.index(' ')))

                print(f'{string_old}\t->\t{"".join(split_list)}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<
    # for format "2020.4.1 13:00"
    # >>>>>>>>>>>>>>>>>>>>>>>>>>

        elif '.' in string :
            if ('PM' not in string) & ('AM' not in string) :
               print("format 2020.4.1 1:00")
                
                string_left = string

                # convert '2020.4.'
                for itera in range(2) :
                    target_string = '.'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if len(temp_left) == 1 :
                        temp_left = '0' + temp_left

                    split_list.append(temp_left)
                    string_left = temp_right
                
                # convert '1 '
                for itera in range(1) :
                    target_string = ' '
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right
                    
                # convert '1:'
                for itera in range(1) :
                    target_string = ':'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right

                # for left ('00')
                split_list.append(double_size(string_left))

                print(f'{string_old}\t->\t{"".join(split_list)}')
    # <<<<<<<<<<<<<<<<<<<<<<<<<<
    # for format "2020.4.1 1:00 PM"
    # >>>>>>>>>>>>>>>>>>>>>>>>>>
            elif ('PM' in string) | ('AM' in string) :
#               print("format 2020.4.1 1:00 PM")
                
                string_left = string

                # convert '2020.4.' (year, month)
                for itera in range(2) :
                    target_string = '.'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if len(temp_left) == 1 :
                        temp_left = '0' + temp_left

                    split_list.append(temp_left)
                    string_left = temp_right
                
                # convert '1 ' (day)
                for itera in range(1) :
                    target_string = ' '
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right
                    
                # convert '1:' (hour)
                for itera in range(1) :
                    target_string = ':'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if 'PM' in string :
                        if temp_left != '12' :
                            temp_left = str(int(temp_left) + 12)

                    elif 'AM' in string :
                        if temp_left == '12' :
                            temp_left = '00'


                    split_list.append(double_size(temp_left))
                    string_left = temp_right

                # for left ('00')
                split_list.append(double_size(string_left[ : string_left.index(' ')))

                print(f'{string_old}\t->\t{"".join(split_list)}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<
    # for format "2020/04/01 1:00"
    # >>>>>>>>>>>>>>>>>>>>>>>>>>
        elif '/' in string :
               print("format 2020/4/1 1:00")
                
                string_left = string

                # convert '2020.4.'
                for itera in range(2) :
                    target_string = '/'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if len(temp_left) == 1 :
                        temp_left = '0' + temp_left

                    split_list.append(temp_left)
                    string_left = temp_right
                
                # convert '1 '
                for itera in range(1) :
                    target_string = ' '
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right
                    
                # convert '1:'
                for itera in range(1) :
                    target_string = ':'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right

                # for left ('00')
                split_list.append(double_size(string_left))

                print(f'{string_old}\t->\t{"".join(split_list)}')

            elif ('PM' in string) | ('AM' in string) :
#               print("format 2020.4.1 1:00 PM")
                
                string_left = string

                # convert '2020.4.' (year, month)
                for itera in range(2) :
                    target_string = '/'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if len(temp_left) == 1 :
                        temp_left = '0' + temp_left

                    split_list.append(temp_left)
                    string_left = temp_right
                
                # convert '1 ' (day)
                for itera in range(1) :
                    target_string = ' '
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    split_list.append(double_size(temp_left))
                    string_left = temp_right
                    
                # convert '1:' (hour)
                for itera in range(1) :
                    target_string = ':'
                    temp_left = string_left[ : string_left.index(target_string)]
                    temp_right = string_left[ string_left.index(target_string) + 1 :]

                    if 'PM' in string :
                        if temp_left != '12' :
                            temp_left = str(int(temp_left) + 12)

                    elif 'AM' in string :
                        if temp_left == '12' :
                            temp_left = '00'


                    split_list.append(double_size(temp_left))
                    string_left = temp_right

                # for left ('00')
                split_list.append(double_size(string_left[ : string_left.index(' ')))

                print(f'{string_old}\t->\t{"".join(split_list)}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<
    # for format "202004010100"
    # >>>>>>>>>>>>>>>>>>>>>>>>>>
        else :
           print("format 202004010100")
            return string




    return ''.join(split_list)
