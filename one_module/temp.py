
    fig = plt.figure(figsize = (14, 7))


    for num_col, col in enumerate(df.columns) :
        if col != 'excel' :
            plt.boxplot(df.loc[:, col].tolist(), positions = [num_col])
            print(f'{col} shown')

    plt.title('minute_interval\nall sample stations')

    plt.savefig('timedelta_minute.png', dpi = 400)
