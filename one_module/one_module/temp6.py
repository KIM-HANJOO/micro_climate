# -----------------------------------------------
# make date list and date_dict, inverse_dict
# -----------------------------------------------

# date from 2020.04.01 to 2021.12.31
date_dict, inverse_dict, real_date_list = all_date()


# -----------------------------------------------
# make function for time convert
# -----------------------------------------------

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
        return dt - datetime.timedelta(minutes = dt.minute)
        #return datetime.datetime(year = year, month = month, day = day, hour = hour, minute = 0)

    else :
        return dt + datetime.timedelta(hours = 1) - datetime.timedelta(minutes = dt.minute)

#        if hour == 23 :
#            if day < 30 :
#                return datetime.datetime(year = year, month = month, day = day  + 1, hour = 0, minute = 0)
#        else :
#            return datetime.datetime(year = year, month = month, day = day, hour = hour + 1, minute = 0)
#


def round_data(df) :
    #time_jam range (from 0 <= time_interval <= jam_top)
    jam_top = 0


    add_columns = ['overlap', 'time_jam', 'minute_interval', '보정_시간', 'hour_available']
    for add in add_columns :
        df[add] = None

    total_size = df.shape[0]
    interval = interval_from_df(df)
    df.loc[:, 'minute_interval'] = interval

    nan = 0
    for index in range(df.shape[0]) :
        if str(df.loc[index, '등록일자']) != 'nan' :
            print(df.loc[index, '등록일자'])
            print(round_hour(df.loc[index, '등록일자']))
            df.loc[index, '보정_시간'] = datetime_to_date(round_hour(df.loc[index, '등록일자']))
            print('\t', df.loc[index, '보정_시간'])
            if df.loc[index, 'minute_interval'] <= jam_top :
                df.loc[index, 'time_jam'] = 'O'
            else :
                df.loc[index, 'time_jam'] = 'X'

        else :
            nan += 1

    jammed = 0
    overlapped = 0

    drop_index = []
    for index in range(df.shape[0]) :
        if df.loc[index, 'time_jam'] == 'O' :
            drop_index.append(index)
            jammed += 1
            #print(index, '\t', df.loc[index, 'jam'])
        else :
            if str(df.loc[index, '등록일자']) == 'nan' :
                drop_index.append(index)
                df.loc[index, 'overlap'] = 'X'

            else :

                if index > 0 :
                    if df.loc[index, '보정_시간'] == df.loc[index - 1, '보정_시간'] :
                        drop_index.append(index)
                        overlapped += 1
                        df.loc[index, 'overlap'] = 'O'
                    else :
                        df.loc[index, 'overlap'] = 'X'
                        #print(index, '\t', df.loc[index, '보정_시간'], df.loc[index - 1, '보정_시간'])


    for index in range(df.shape[0]) :
        if (df.loc[index, 'time_jam'] == 'O') | (df.loc[index, 'overlap'] == 'O') :
            df.loc[index, 'hour_available'] = 'X'

        else :
            df.loc[index, 'hour_available'] = 'O'

    
    
    df.reset_index(drop = True, inplace = True)

    return df, jammed, overlapped, nan




# -----------------------------------------------
# plot 
# -----------------------------------------------

a = input('round data (y/n)')

sample_round = os.path.join(sample_robby, 'rounded')

if a == 'y' :
    df = pd.DataFrame(columns = ['excel', 'org_date', 'time-jam', 'overlapped rounded time', 'nan times', 'dropped_date', 'percentage'])
    df_num = 0

    for excel_num, excel in enumerate(os.listdir(sample_avail)) :
        if excel_num > -1:
            os.chdir(sample_avail)
            temp = read_excel(excel)
            total_size = temp.shape[0]

            temp2, jammed, overlapped, nan = round_data(temp)
            os.chdir(sample_round)
            temp2.to_excel(excel)

            df.loc[df_num, :] = [excel, total_size, jammed, overlapped, nan, temp2.shape[0], round((temp2.shape[0] / total_size) * 100, 2)]
            df_num += 1

            print(excel_num, '\n')

    os.chdir(sample_robby)
    df.to_excel('rounded_info_1.xlsx')
            


