# -----------------------------------------------
# plot independent informations for each stations
# -----------------------------------------------


#   < directory paths >
samples_module_dir = Path(os.getcwd())
sample_robby = samples_module_dir.parent
sample_data = os.path.join(sample_robby, 'data')
sample_info = os.path.join(sample_robby, 'info')
sample_plot = os.path.join(sample_robby, 'plot')
sample_typo = os.path.join(sample_robby, 'typo')
sample_avail = os.path.join(sample_robby, 'only_available_time')
sample_plot = os.path.join(sample_plot, 'barplot_info')


main_dir = sample_robby.parent
module_dir = os.path.join(main_dir, 'module')

datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
info_dir = os.path.join(main_dir, 'info_data')


# -----------------------------------------------
# define function to link dates
# -----------------------------------------------

def date_to_number(regi_date) :
    start_date = datetime.datetime(2020, 1, 1, 00)
    now_date = datetime.datetime(int(regi_date[ : 4]), int(regi_date[4 : 6]), \
            int(regi_date[6 : 8]), int(regi_date[8, 10]))
    pass

def all_date() :
    start_date = datetime.datetime(2020, 1, 1, 00)
    end_date = datetime.datetime(2021, 12, 31, 23)
    temp_date = start_date
    index_num = 0

    date = []
    index = []

    date_dict = dict()
    inverse_dict = dict()

    while temp_date < end_date :
        temp_string = str(temp_date.year) + double_size(str(temp_date.month)) + \
                double_size(str(temp_date.day)) + double_size(str(temp_date.hour))\
                + '00'
        date.append(temp_string)
        index.append(index_num)

        date_dict[temp_string] = index_num
        inverse_dict[index_num] = temp_string
        
        index_num += 1
        temp_date = temp_date + datetime.timedelta(hours = 1)



    return date_dict, inverse_dict


date_dict, inverse_dict = all_date()




excepted = 0

df = pd.DataFrame(columns = ['excel', 'date', 'hour', 'temperature', 'wind_angle', 'wind_speed', 'fine_dust'])
df_num = 0

for excel_num, excel in enumerate(os.listdir(sample_avail)) :
    os.chdir(sample_avail)
    temp = read_excel(excel)
    if (temp.shape[0] != 0) :
        #print(temp.columns)
        #print(temp.loc[: , ['????????????', '??????']])

        for index in range(temp.shape[0]) :
            real_date = str(temp.loc[index, '????????????'])[4 : 8] + ' ' + str(temp.loc[index, '????????????'])[8 : 10] + '???'
            temp_date = str(temp.loc[index, '????????????'])[ : 10] + '00'

            if temp_date in date_dict.keys() :
                temp_num = date_dict[temp_date]

            temp_temp = float(str(temp.loc[index,'??????']).replace(',', ''))
            temp_wa = float(temp.loc[index, '??????'])
            temp_ws = float(temp.loc[index, '??????'])
            temp_fd = float(temp.loc[index, '????????????'])

            if (temp_temp > -15) & (temp_temp < 50) :
                if (temp_wa > -1) & (temp_wa < 361) :
                    if (temp_ws > -1) & (temp_ws < 10) :
                        if temp_fd != 'nan' :

                            df.loc[df_num, :] = [excel, real_date, temp_num, temp_temp, temp_wa, temp_ws, temp_fd]
                            df_num += 1
                            check = 1
            if check == 0 :
                excepted += 1


    print(f'{excel_num + 1}, {len(os.listdir(sample_avail))}')
print(df)

df.sort_values(by = ['hour'], inplace = True, ignore_index = True)


all_hour = df.loc[:, 'hour'].tolist()
real_date = df.loc[:, 'date'].tolist()
all_temperate = df.loc[:, 'temperature'].tolist()
all_wa = df.loc[:, 'wind_angle'].tolist()
all_ws = df.loc[:, 'wind_speed'].tolist()
all_fd = df.loc[:, 'fine_dust'].tolist()

print(min(all_hour))
min_date = inverse_dict[min(all_hour)]
max_date = inverse_dict[max(all_hour)]

fig = plt.figure(figsize = (10, 7))

plt.scatter(all_hour, all_temperate)
#plt.xlim(0, 8760)
#plt.xticks(all_hour, real_date, rotation = 90)
plt.grid()
os.chdir(sample_plot)
plt.title(f'temperature\n{min_date} to {max_date}')
plt.savefig('temp_temperature_all.png', dpi = 400)
dlt.savefig(sample_plot, 'temp_temperature_all', 400)
plt.clf()


df = pd.DataFrame(columns = ['angle', 'speed'])
df.loc[:, 'angle'] = all_wa
df.loc[:, 'speed'] = all_ws
df.sort_values(by = ['angle'], inplace = True, ignore_index = True)

for item in df.loc[:, 'angle'].unique() :
    temp_speed = df[df['angle'] == item].loc[:, 'speed'].tolist()
    plt.boxplot(temp_speed, positions = [item])

#plt.scatter(all_wa, all_ws)
plt.title('wind angle & speed\nx : angle, y : speed')
#plt.grid()
dlt.savefig(sample_plot, 'temp_was_boxplot', 400)
plt.clf()



plt.scatter(all_hour, all_wa)
#plt.xlim(0, 8760)
#plt.xticks(all_hour, real_date, rotation = 90)
plt.grid()
plt.title(f'wind angle\n{min_date} to {max_date}')
dlt.savefig(sample_plot, 'temp_wa_all', 400)
plt.clf()

plt.scatter(all_hour, all_ws)
#plt.xlim(0, 8760)
#plt.xticks(all_hour, real_date, rotation = 90)
plt.grid()
plt.title(f'wind speed\n{min_date} to {max_date}')
dlt.savefig(sample_plot, 'temp_ws_all', 400)
plt.clf()

plt.scatter(all_hour, all_fd)
#plt.xlim(0, 8760)
#plt.xticks(all_hour, real_date, rotation = 90)
plt.grid()
plt.title(f'fine dust\n{min_date} to {max_date}')
dlt.savefig(sample_plot, 'temp_fd_all', 400)
plt.clf()
    




# -----------------------------------------------
# plot wind
# -----------------------------------------------


# -----------------------------------------------
# plot temp
# -----------------------------------------------


# -----------------------------------------------
# plot fine_dust
# -----------------------------------------------
print(df)
print(excepted)

#target_num = len(df.loc[:, 'hour'].unique().tolist())
#
#for num_item, item in enumerate(df.loc[:, 'hour'].unique()) :
#    temp = df[df['hour'] == item].loc[:, 'temperature'].tolist()
#    for temp_item in temp :
#        plt.scatterplot(item, temp_item)
#    #plt.boxplot(temp, positions = [item])
#    print(num_item, '\t', target_num)
