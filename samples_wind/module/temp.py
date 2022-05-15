#        # pull summer / winter days
#        summer_index = []
#        winter_index = []
#        for num_index, index in enumerate(range(df.shape[0])) :
#            
#            if str(df.loc[index, '보정_시간'])[ : 8] == summer_day :
#                summer_index.append(index)
#
#            if str(df.loc[index, '보정_시간'])[ : 8] == winter_day :
#                winter_index.append(index)
#
#        summer_temp = df.loc[summer_index, : ]
#        winter_temp = df.loc[winter_index, : ]
#
#        summer_avail = summer_temp[summer_temp['hour_available'] == 'O']
#        winter_avail = winter_temp[winter_temp['hour_available'] == 'O']
#
#        summer_avail.reset_index(drop = True, inplace = True)
#        winter_avail.reset_index(drop = True, inplace = True)
#
#        for index in range(summer_avail.shape[0]) :
#            print(summer_avail.loc[index, '보정_시간'])
#            summer_df.loc[str(summer_avail.loc[index, '보정_시간']), excel] = str(summer_avail.loc[index, target])
#
#
#        for index in range(winter_avail.shape[0]) :
#            winter_df.loc[str(winter_avail.loc[index, '보정_시간']), excel] = str(winter_avail.loc[index, target])
#
#        print(f'{target}\t{num_excel}\t{excel}')
#
#
#    # save dataframe
#    os.chdir(zoom_plot)
#
#    summer_df.to_excel(f'{target}_summer_df.xlsx')
#    winter_df.to_excel(f'{target}_winter_df.xlsx')
