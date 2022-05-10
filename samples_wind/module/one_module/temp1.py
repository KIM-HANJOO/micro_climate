# -----------------------------------------------
# check data times if they are omitted or not 
# -----------------------------------------------

a = input('check data times for omitted infos (y/n)')

if a == 'y' :
    os.chdir(sample_data)
    print(os.listdir(sample_data))


    data_date = pd.DataFrame(columns = ['excel', 'columns_num', 'columns'])
    num_date = 0


    for excel in os.listdir(sample_data) :
        os.chdir(sample_data)
        temp = read_excel(excel)


        print(len(temp.columns))
        data_date.loc[num_date, :] = [excel, len(temp.columns), str(temp.columns)]
        num_date += 1

    os.chdir(sample_plot)
    data_date.to_excel('date_info.xlsx')

    print('done and saved')


# -----------------------------------------------
# typo correcting dictionary
# -----------------------------------------------

merge_columns = dict()

merge_columns['기관명'] = ['기관명', '기관 명']
merge_columns['모델명'] = ['모델명', '모델 명']
merge_columns['시리얼'] = ['시리얼']
merge_columns['전송시간'] = ['전송 시간', '전송시간']
merge_columns['등록일자'] = ['등록일자', '등록 일자']
merge_columns['돌풍풍향'] = ['돌풍 풍향(°)', '돌풍풍향(°)']
merge_columns['돌풍풍속'] = ['돌풍 풍속(m/s)', '돌풍풍속(m/s)']
merge_columns['풍향'] = ['풍향(°)', '풍향 (°)']
merge_columns['풍속'] = ['풍속(m/s)', '풍속 (m/s)']
merge_columns['기온'] = ['기온(℃)', '기온(℃) ', '기온 (℃)', ' 기온(℃) ']
merge_columns['상대습도'] = ['상대습도(%)', '상대습도 (%)', '상대습도( %)']
merge_columns['초미세먼지'] = ['초미세먼지(㎍/㎥)', '초미세먼지 (㎍/㎥)']
merge_columns['미세먼지'] = ['미세먼지(㎍/㎥)', '미세먼지 (㎍/㎥)']
merge_columns['초미세먼지보정'] = ['초미세먼지 보정(㎍/㎥)', '초미세먼지 보정 (㎍/㎥)']
merge_columns['미세먼지보정'] = ['미세먼지 보정(㎍/㎥)', '미세먼지 보정 (㎍/㎥)']

save_columns = list(merge_columns.keys())

save_target = []
for key in merge_columns.keys() :
    for item in merge_columns[key] :
        save_target.append(item)


# -----------------------------------------------
# apply to sample datas
# -----------------------------------------------

print(save_columns)
print(save_target)

print(len(save_columns))
print(len(save_target))

a = input('apply typo correcting to sample datas? (y/n)')

if a == 'y' :
    all_excel = len(os.listdir(sample_data))
    for num_excel, excel in enumerate(os.listdir(sample_data)) :
        os.chdir(sample_data)
        temp = read_excel(excel)

        save = []
        kill = []

        for col in temp.columns :
            check = 0
            for key in save_columns : 
                if col in merge_columns[key] :
                    check = 1
                    break
            
            if check == 1 :
                save.append(col)
            else :
                kill.append(col)

        print(save)
        print(kill)

        print(temp.columns)
        for col in temp.columns :
            if col in save :
                check = 0
                for key in save_columns : 
                    if col in merge_columns[key] :
                        column_change = key
                        check = 1

                if check == 0 :
                    print(f'{col}\tnot matched')

                else :
                    print(f'{col}\t{column_change}')
                    for index in range(temp.shape[0]) :
                        if not pd.isna(temp.loc[index, col]) :
                            temp.loc[index, column_change] = temp.loc[index, col]
                        else :
                            print(f'{index} | {col}, nan')

            
            
            kill_columns = []
            for col in temp.columns :
                if col not in save_columns :
                    kill_columns.append(col)

            temp.drop(kill_columns, axis = 1, inplace = True)
            temp.reset_index(drop = True, inplace = True)
            

            os.chdir(sample_typo)
            temp.to_excel(excel)

            print(f'{num_excel} / {all_excel}\t{round((num_excel / all_excel) * 100, 2)}%\t{len(temp.columns)}')


                


# -----------------------------------------------
# check typo corrected sample datas
# -----------------------------------------------

a = input('check sample datas after typo correcting (y/n)')

if a == 'y' :
    os.chdir(sample_typo)
    print(os.listdir(sample_typo))


    data_date = pd.DataFrame(columns = ['excel', 'columns_num', 'columns'])
    num_date = 0


    for excel in os.listdir(sample_typo) :
        os.chdir(sample_typo)
        temp = read_excel(excel)


        print(len(temp.columns))
        data_date.loc[num_date, :] = [excel, len(temp.columns), str(temp.columns)]
        num_date += 1

    os.chdir(sample_plot)
    data_date.to_excel('date_info_aftertypo.xlsx')

    print('done and saved')




