# -----------------------------------------------
# unite transmission time format
# -----------------------------------------------

# type of formats

# 2021-10-03 5:03
# 2021-10-03 23:03:10 PM


# drop nan values in ['등록일자']

a = input('drop nan times (y/n)')

if a == 'y' :
    num_all = len(os.listdir(sample_time))
    for num_excel, excel in enumerate(os.listdir(sample_time)) :

        os.chdir(sample_time)
        temp = read_excel(excel)

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
    import outlier as out
    target_info_list = ['풍속', '풍향', '기온', '상대습도', '초미세먼지', '미세먼지']

    for target_info in target_info_list :

        df_outliers = pd.DataFrame(columns = ['excel', 'total_size', 'null', 'z-score', 'IQR', 'method(min)', 'in-range(min)', 'in-range(max)'])
        num_outliers = 0

        num_all = len(os.listdir(sample_only_time))
        for num_excel, excel in enumerate(os.listdir(sample_only_time)) :
            os.chdir(sample_only_time)
            temp = read_excel(excel)

            if temp.shape[0] == 0 :
                df_outliers.loc[num_outliers, :] = [excel, 0, 'no_index', 'no_index', 'no_index', 'no_index', 'no_index', 'no_index']
                num_outliers += 1

            else :

                null_num = temp[target_info].isnull().sum()
                
                if null_num == temp.shape[0] :
                    df_outliers.loc[num_outliers, :] = [excel, temp.shape[0], null_num, 0, 0, 'none', 0, 0]
                    num_outliers += 1


                else :
                    target = temp[target_info].dropna().tolist()
                    zscore_non, zscore = out.z_score(target, 2)
                    iqr_non, iqr = out.out_box(target, 1.5)

                    z_num = len(zscore)
                    iqr_num = len(iqr)

                    left_num_min = temp.shape[0] - null_num - min(z_num, iqr_num)
                    left_num_max = temp.shape[0] - null_num - max(z_num, iqr_num)

                    if min(z_num, iqr_num) == z_num :
                        method_used = 'z_score'
                    else :
                        method_used = 'iqr'
                        

                    df_outliers.loc[num_outliers, :] = [excel, temp.shape[0], null_num, z_num, iqr_num, method_used, left_num_min, left_num_max]
                    num_outliers += 1
            print(f'{num_excel} / {num_all}')

        os.chdir(os.path.join(sample_plot, 'null_outliers_check'))
        df_outliers.to_excel(f'{target_info}_null_outliers_check.xlsx')
        print(df_outliers)

