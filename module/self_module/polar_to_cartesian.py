import os
import sys
import get_dir
from pathlib import Path
import os.path
from PIL import Image, ImageDraw

preprocess_dir = Path(os.getcwd())
module_dir = preprocess.parent
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

import statistics

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

def ave(list1) :
	return sum(list1) / len(list1)

# -----------------------------------------------
# convert from polar coordinate to cartesian coordinate
# -----------------------------------------------

def three_sixty_to_radius(angle) :
    # convert 360 degreed to radian
    return angle * (2 * np.pi / 360)

def polar_to_cartesian(theta, radius) :
    return [radius * np.cos(theta), radius * np.sin(theta)]

def vector_sum(v1, v2) :
    # v1, v2 in 2 lengthed-list form
    return v1 + v2

def polar_to_cartesian_implicit_position(datum, polar_r_theta) :
    # datum, polar params in 2 lengthed-list form
    # r - theta order for polar_r_theta
    return datum + polar_to_cartesian(polar_r_theta[0], polar_r_theta[1])

def normal_of_vector_2d(pos1, pos2) :
    vector = pos1 - pos2
    n_vector_1 = [(-1) * vector[1], vector[0]]
    n_vector_2 = -1 * n_vector_1

    n_vector_1 = n_vector_1 / np.sqrt(pow(n_vector_1[0], 2) + pow(n_vector_1[1], 2))
    n_vector_2 = n_vector_2 / np.sqrt(pow(n_vector_2[0], 2) + pow(n_vector_2[1], 2))
    
    return n_vector_1, n_vector_2


# -----------------------------------------------
# plot module made up with PIL
# -----------------------------------------------

def boxplot_info(list1) :
    
    Q1 = np.percentile(list1, 25)
    Q3 = np.percentile(list1, 75)
    median = statistics.median(list1)

    IQR = Q3 - Q1

    min_outliers = [x for x in list1 if x < Q1 - 1.5 * IQR]
    max_outliers = [x for x in list1 if x < Q3 + 1.5 * IQR]

    if min(list1) < Q1 - 1.5 * IQR :
        minimum = Q1 - 1.5 * IQR
    else :
        minimum = min(list1)

    if max(list1) > Q3 + 1.5 * IQR :
        maximum = QQ3 + 1.5 * IQR
    else :
        maximum = max(list1)

    outliers = min_outliers + max_outliers

    return Q1, median, Q3, minimum, maximum, outliers

def boxplot_info_cartesian(list1, angle, magnitude_ratio) :
    Q1, median, Q3, minimum, maximum, outliers = boxplot_info(list1 * magnitude_ratio)
    Q1_c = polar_to_cartesian(anlge, Q1)
    Q3_c = polar_to_cartesian(anlge, Q1)
    median_c = polar_to_cartesian(anlge, median)
    minimum_c = polar_to_cartesian(anlge, minimum)
    maximum_c = polar_to_cartesian(anlge, maximum)

    outliers_c = np.empty((len(outliers), 2))

    for item_number, item in enumerate(outliers) :
        item_c = polar_to_cartesian(anlge, item)
        outliers_c[item_number] = item_c

    return Q1_c, median_c, Q3_c, minimum_c, maximnum_c, outliers_c

def boxplot_info_cartesian_implicit_position(list1, datum, angle, magnitude_ratio) :
    Q1, median, Q3, minimum, maximum, outliers = boxplot_info(list1 * magnitude_ratio)
    Q1_c = polar_to_cartesian_implicit_position(datum, [anlge, Q1])
    Q3_c = polar_to_cartesian_implicit_position(datum, [anlge, Q1])
    median_c = polar_to_cartesian_implicit_position(datum, [anlge, median])
    minimum_c = polar_to_cartesian_implicit_position(datum, [anlge, minimum])
    maximum_c = polar_to_cartesian_implicit_position(datum, [anlge, maximum])

    outliers_c = np.empty((len(outliers), 2))

    for item_number, item in enumerate(outliers) :
        item_c = polar_to_cartesian_implicit_position(datum, [anlge, item])
        outliers_c[item_number] = item_c

    return Q1_c, median_c, Q3_c, minimum_c, maximnum_c, outliers_c

def make_template(size) :
    # size in 2 lengthed-list form
    image = Image.new(mode = 'P', size = tuple(size), color = 'white')
    draw = ImageDraw.Draw(image)

    return image, draw

def make_template_center_datum(size) :
    image, draw = make_template(size)
    return image, draw, size / 2

def draw_line(draw, pos1, pos2, color, width) :
    xy = []
    xy.append(tuple(pos1))
    xy.append(tuple(pos2))

    draw.line(xy, fill = color, width = width)

def draw_normal_line(draw, pos1, pos2, color, width, length) :
    # normal vector of pos1 - pos2, draw at pos1 
    n1, n2 = normal_of_vector_2d(pos1, pos2)

    draw_line(draw, pos1 + 0.5 * length * n1, pos1 + 0.5 * length * n2, color, width)

def draw_rectangle(draw, pos1, pos2, color, linewidth, boxwidth) :
    xy = []
    xy.append(tuple(pos1))
    xy.append(tuple(pos2))

    n_1, n_2 = normal_of_vector_2d(pos1, pos2)

    boxpos1 = pos1 + boxwidth * n_1 / 2
    boxpos2 = pos1 + boxwidth * n_2 / 2
    boxpos3 = pos2 + boxwidth * n_1 / 2
    boxpos4 = pos2 + boxwidth * n_2 / 2

    shape = [tuple(boxpos1), tuple(boxpos2), tuple(boxpos4), tuple(boxpos3)]

    draw.rectangle(shape, outline = color)


# -----------------------------------------------
# for plotting wind multi-boxplot
# -----------------------------------------------

def draw_grid(draw, datum_point, magnitude_ratio, interval) :


def draw_boxplot(draw, datum_point, magnitude_ratio, angle, list1) :
    # make each info items in cartesian form
    Q1, median, Q3, minimum, maximum, outliers = boxplot_info_cartesian_implicit_position(list1, datum_point, angle, magnitude_ratio)

    box_width = 1

    # standard vector (angle, size = 1)
    standard_vector = polar_to_cartesian_implicit_position(angle, 1)

    # draw rectangle (boxplot) for Q1, Q3
    draw_rectangle(draw, Q1, Q3, 'black', 1, box_width)

    # draw line from Q1 to minimum, Q3 to maximum
    draw_line(draw, minimum, Q1, 'black', 1)
    draw_line(draw, Q3, maximum, 'black', 1)

    # draw normal line for minimum, maximum, median
    draw_nomral_line(draw, minimum, standard_vector, 'black', 1, box_width)
    draw_nomral_line(draw, maximum, standard_vector, 'black', 1, box_width)
    draw_nomral_line(draw, median, standard_vector, 'black', 1, box_width)

    # draw outliers as circle 
    for index in range(outliers.shape[0]) :
        temp_point = outliers[index]
        temp_point_x = temp_point[0]
        temp_point_y = temp_point[1]
        radius = box_width * 0.5

        circle_points = (temp_point_x - radius, temp_point_y + radius, temp_point_x + radius, temp_point_y - radius)
        draw.elipse(circle_points, outline = (0, 0, 0))


