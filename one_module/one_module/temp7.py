# -----------------------------------------------
# make date list and date_dict, inverse_dict
# -----------------------------------------------

# date from 2020.04.01 to 2021.12.31
date_dict, inverse_dict, real_date_list = all_date()


def round_hour(dt) :
    # convert string (202004010100) to datetime format
    dt = date_to_datetime(dt)

    # split datetime
    year = dt.year
    month = dt.month
    day = dt.day

    hour = dt.hour
    minute = dt.minute


    # ruturn rounded datetime
    if dt.minute < 30 :
        return datetime.datetime(year = year, month = month, day = day, hour = hour)

    else :
        return datetime.datetime(year = year, month = month, day = day, hour = hour + 1)

# -----------------------------------------------
# make date list and date_dict, inverse_dict
# -----------------------------------------------

# check all stations if there is any wrong formats

a = input('check stations if any have any wrong formats(y/n)')

if a == 'y' :
    for excel_num, excel in enumerate(os.listdir(sample_avail)) :
        os.chdir(sample_avail)
        temp = read_excel(excel)
        for index in range(temp.shape[0]) :
            if not check_avail(temp.loc[index, '등록일자']) :
                print(f"{excel}\t{index}\t{temp.loc[index, '등록일자']}")
        print(f'{excel_num + 1} / 32')



a = input('make minutual - timedelta dataframe and plot(y/n)')


if a == 'y' :

    
    real_date_list_num = list(range(len(real_date_list)))
    interval_all = pd.DataFrame(columns = real_date_list_num)
    
    sample_list = []

    for excel_num, excel in enumerate(os.listdir(sample_avail)) :
        if excel_num < 1 :
            os.chdir(sample_avail)
            temp = read_excel(excel)
            
            for index in range(temp.shape[0]) :
                if str(temp.loc[index, '등록일자']) != 'nan' :
                    start_date = temp.loc[index, '등록일자']
                    start_date = round_hour(start_date)
                    break
            
            start_number = -1
            start_date = datetime_to_date(start_date)
            for number, date in enumerate(real_date_list) :
                if str(start_date) == str(date) :
                    start_number = number
                    break
            
#        if start_number == -1 :
#            print('%%%\n' * 1000)
                    

            interval = interval_from_df(temp)
            interval_start = 0

            for col in interval_all :
                if int(col) < start_number :
                    interval_all.loc[excel_num, col] = -1
                else :
                    if interval_start < len(interval) :
                        interval_all.loc[excel_num, col] = interval[interval_start]
                        interval_start += 1
                    else :
                        interval_all.loc[excel_num ,col] = -1

            print(excel_num)
            print(interval_all)


# -----------------------------------------------
# plot temperature information (barplot)
# -----------------------------------------------

    
    fig = plt.figure(figsize = (14, 7))

    interval_col = interval_all.columns.astype(int)

#    x = []
#    for number in range(len(interval_all)) :
#        x.append(1)
    for excel in range(interval_all.shape[0]) :
        for col in interval_all.columns :
            val = int(interval_all.loc[excel, col])
            if (val != -1) : #& (val != 0) & (val != 60) & (val % 60 != 0) :
                
                print(col, interval_all.loc[excel, col])
                plt.plot([col, col + 1], [interval_all.loc[excel, col], interval_all.loc[excel, col]], color = 'blue', linewidth = 3)



    plt.title('minute_interval\none sample stations')

    plt.ylabel('minute')
#    plt.ylim(0, 300)
#    grid_list = [0, 60, 120, 180, 240, 300]
#    plt.yticks(grid_list)
    plt.grid()
    os.chdir(sample_plot)
    plt.savefig('scattered_timedelta_rounded.png', dpi = 400)
    dlt.savefig(sample_plot, 'scattered_timedelta_rounded.png', 400)

        


