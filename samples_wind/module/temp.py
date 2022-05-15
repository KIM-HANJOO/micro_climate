# -----------------------------------------------
# temp function
# -----------------------------------------------

def get_day(df, day) :

    day_list = []

    for index in range(df.shape[0]) :
        date = str(df.loc[index, '보정_시간'])
        if day in date :
            day_list.append(index)

    target_df = df.loc[day_list, :].copy()
    target_df.reset_index(drop = True, inplace = True)

    drop_index = []
    for index in range(target_df.shape[0]) :
        if target_df.loc[index, 'hour_available'] == 'X' :
            drop_index.append(index)

    target_df.drop(drop_index, inplace = True)
    target_df.reset_index(drop = True, inplace = True)


    target_edt = target_df.shape[0]
    print(target_df)

    # add ommitted time to target_df

    add_target_date = []
    for hour in range(24) :
        hour_str = double_size(str(hour))
        target_asc = day + hour_str + '00'

        hour_check = 0
        for index in range(target_df.shape[0]) :
            if target_asc in str(target_df.loc[index, '보정_시간']) :
                hour_check = 1

        if hour_check == 0 :
            add_target_date.append(target_asc)
    
    print(len(add_target_date))
    for day in add_target_date :
        target_df.loc[target_edt, '보정_시간'] = day
        target_edt += 1

    for index in range(target_df.shape[0]) :
        target_df.loc[index, '보정_시간'] = str(int(target_df.loc[index, '보정_시간']))

    target_df.sort_values(by = ['보정_시간'], inplace = True, ignore_index = True)

    return target_df

