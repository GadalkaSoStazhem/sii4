import math

import pandas as pd

def shape (df):
    print(df.shape)
    return df.shape

def get_num_cols(df):
    data = {}
    df_num = pd.DataFrame(data)
    for col in df.columns:
        if df[col].dtype == int or df[col].dtype == float:
            df_num[df[col].name] = df[col].values
    return df_num

def mean_vals(df, rows):
    means = []
    print("Средние значения по колонкам: ")
    for col in df.columns:
        print(df[col].name, ": ", df[col].sum() / rows)
        means.append(df[col].sum() / rows)
    return means

def standard_dev(df, means, n):
    for col in df.columns:
        






def min_max(df):
    print("Минимальные и максимальные значения столбцов")
    for i in df.columns:
        if df[i].dtype == int or df[i].dtype == float:
            print(df[i].name, ": Минимум: ", df[i].min(), " Максимум: ", df[i].max())
        else:
            print("В колонке ", df[i].name, " содержатся нечисловые значения")

