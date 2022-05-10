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
# plot available datas
# -----------------------------------------------

a = input('plot available dates (y/n)')

if a == 'y' :
    os.chdir(sample_plot)
    info_date_ava = read_excel('date_availability_forsampels.xlsx')#.loc[21 : 31, :]
    info_date_ava.reset_index(drop = True, inplace = True)
    info_date_ava.drop([9], axis = 0, inplace = True)
    info_date_ava.reset_index(drop = True, inplace = True)
    info_date_ava.reset_index(drop = True, inplace = True)

    index_num = np.arange(info_date_ava.shape[0])

    perc = []
    perc_flt = []
    for index in range(info_date_ava.shape[0]) :
        all_date = info_date_ava.loc[index, 'all_date']
        ava_date = info_date_ava.loc[index, 'available']
        
        temp_perc = round((ava_date / all_date) * 100, 2)

        perc.append(f'{round((ava_date / all_date) * 100, 2)}%')
        perc_flt.append(round((ava_date / all_date) * 100, 2))



    fig = plt.figure(figsize = (7, 10))
    p1 = plt.bar(index_num, info_date_ava.loc[:, 'available'], color = 'b', alpha = 0.7, label  ='available')
    p2 = plt.bar(index_num, info_date_ava.loc[:, 'non-available'], color = 'r', alpha = 0.7, bottom = info_date_ava.loc[:, 'available'], label = 'non-available')
    plt.legend()
    plt.title(f'dates\naverage = {round(ave(perc_flt), 2)}%')
    plt.xticks(index_num, perc, rotation = 60)

    os.chdir(sample_plot)

    dlt.savefig(sample_plot, 'date_available_all.png', 400)
    print(info_date_ava)



# -----------------------------------------------
#  function for plotting stacked barplot
# -----------------------------------------------



def barplot_stack(df, xticks, stack_list, stack_label, color_list, save_name, title, plot_dir) :
    fig = plt.figure(figsize = (9, 9))

    df = df.loc[:, stack_list]
    index_num = np.arange(df.shape[0])

    for st_num, stack in enumerate(stack_list) :
        if st_num == 0 :
#            print(index_num, df.loc[:, stack], color_list[st_num], stack_label[st_num])
            p1 = plt.bar(index_num, df.loc[:, stack], color = color_list[st_num], alpha = 0.7, label = stack_label[st_num])
            last_stack = np.array(df.loc[:, stack])
        else :
            p2 = plt.bar(index_num, df.loc[:, stack], color = color_list[st_num], alpha = 0.7, label = stack_label[st_num], bottom = last_stack)
            last_stack += np.array(df.loc[:, stack])

            print(np.array(df.loc[:, stack]))
        print(last_stack)

    plt.legend()
    plt.title(title)
    #plt.ylim(0, 3700)
    plt.xticks(index_num, xticks, rotation = 60)
    os.chdir(plot_dir)
    plt.savefig(save_name, dpi = 400)

    dlt.savefig(plot_dir, save_name, 400)


# -----------------------------------------------
#  make barplot for each informations (containing null-values, iqr, z-scores)
# -----------------------------------------------


def kor_to_eng(string) :
    list1 = ['풍향', '풍속', '미세먼지', '기온', '초미세먼지', '상대습도']
    list2 = ['wind_angle', 'wind_speed', 'fine_dust', 'temperature', 'ultra_fine_dust', 'relative_humidity']

    for item_index, item in enumerate(list1) :
        if item in string :
            print(f'{string} replaced to {string.replace(item, list2[item_index])}\n')

            return string.replace(item, list2[item_index]) 

a = input('make plots for independent variables for sample stations? (y/n)')

if a == 'y' :
    list1 = ['풍향', '풍속', '미세먼지', '기온', '초미세먼지', '상대습도']
    ndf = pd.DataFrame(columns = list1)
    
    check_dir = os.path.join(sample_plot, 'null_outliers_check')
    for excel in os.listdir(check_dir) :
        info_name = excel[ : excel.index('_')]

        os.chdir(check_dir)
        temp = read_excel(excel)#.loc[21 : 31, :]

        temp.reset_index(drop = True, inplace = True)
        temp.drop([9], axis = 0, inplace = True)
        temp.reset_index(drop = True, inplace = True)

        org_sum = int(temp.loc[:, 'total_size'].sum())
        null_sum = int(temp.loc[:, 'null'].sum())

        for item in list1 :
            if item in excel :
                ndf.loc[0, item] = round(((org_sum - null_sum) / org_sum) * 100, 4)
                ndf.loc[1, item] = org_sum
                ndf.loc[2, item] = null_sum
                ndf.loc[3, item] = org_sum - null_sum


        #original temp.columns = ['excel', 'total-size', 'null', 'iqr', 'method'\
        #                ,'in-range']

        temp.columns = ['excel', 'total_size', 'null', 'used', 'used_method'\
                        ,'in-range']


        #xticks = temp.loc[:, 'used_method'].tolist()
        xticks_tar = temp.loc[:, 'excel'].tolist()
        xticks = []
        for item in xticks_tar :
            xticks.append(item.replace('.xlsx', ''))

        stack_list = ['in-range', 'null', 'used']
        stack_label = ['available', 'null', 'outliers']
        color_list = ['blue', 'red', 'green']
        save_name = f'{info_name}_barplot_sample_stations'
        save_name = kor_to_eng(save_name)
        print(save_name)
        title = f'{info_name}\nall sample stations'
        plot_dir = os.path.join(sample_plot, 'plot_information')
        dich.newfolder(plot_dir)

        os.chdir(plot_dir)
        target_col = ['excel', 'total_size', 'null', 'used', 'used_method', 'in-range']
        temp.loc[:, target_col].to_excel(f'{info_name}_info_dataframe.xlsx')

        fig = plt.figure(figsize = (9, 9))

        temp = temp.loc[:, stack_list]
        index_num = np.arange(temp.shape[0])

        p_available = plt.bar(index_num, temp.loc[:, 'in-range'], \
                color = color_list[0], alpha = 0.7, label = stack_label[0])
        p_null = plt.bar(index_num, temp.loc[:, 'null'], \
                color = color_list[1], alpha = 0.7, label = stack_label[1], \
                bottom = temp.loc[:, 'in-range'])

        used_bottom = []
        for index in range(temp.shape[0]) :
            used_bottom.append(temp.loc[index, 'in-range'] + temp.loc[index, 'null'])

        p_outliers = plt.bar(index_num, temp.loc[:, 'used'], \
                color = color_list[2], alpha = 0.7, label = stack_label[2], \
                bottom = used_bottom)

        plt.legend()
        plt.title(title)
        #plt.ylim(0, 3700)
        plt.xticks(index_num, xticks, rotation = 60)
        dlt.savefig(plot_dir, save_name, 400)

        barplot_stack(temp, xticks, stack_list, stack_label, color_list, save_name, title, plot_dir) 
        print(f'{save_name} ended')

print(ndf)
ndf.index = ['percentage', 'total', 'null', 'total-null']
ndf.to_excel('available_numbers.xlsx')








