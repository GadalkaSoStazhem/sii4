import pandas as pd
import matplotlib.pyplot as plt
from characteristics import mean_vals, st_deviation
import numpy
import random
def nan_check(df):
    missed = df.isna().sum().sum()
    if missed > 0:
        print("Количество пропущенных значений: ")
        for col in df.columns:
            if type(df[col].to_dict()[0]) == int or type(df[col].to_dict()[0]) == float:
                df[col].fillna(df[col].mean(), inplace = True)
            else:
                df[col].fillna(df[col].mode().iloc[0], inplace = True)
    else:
        print("Пропущенных значений нет")

def cat_features (df):
    flag = 0
    for col in df.columns:
        if type(df[col].to_dict()[0]) == str:
            flag = 1
            cat_col = pd.get_dummies(df[col],  drop_first=True, dtype=int)
            to_add = pd.DataFrame(data = cat_col.values, columns=[df[col].name])
            df = df.drop(df[col].name, axis = 1)
            df_good = pd.concat([df, to_add], axis = 1)


    if flag == 0:
        return df
    else:
        return df_good

def define_distrib(df):
    plt.figure(figsize=(20, 10))
    for i, col in enumerate(df.columns):
        plt.subplot(2, 3, i + 1)
        df[col].plot(kind='hist')
        plt.title(df[col].name)
    plt.tight_layout()
    plt.show()

def splitter (df, test_size, random_state):
    shape = df.shape #колонки отдельно!!!
    X = df.drop('Performance Index', axis = 1)
    y = df['Performance Index']
    ids = numpy.array(range(shape[0]))
    random.seed(random_state)
    random.shuffle(ids)

    test = round(shape[0] * test_size)

    test_ids = ids[0:test]
    tr_ids = ids[test:shape[0]]

    X_train = pd.DataFrame(X.values[tr_ids, :], columns=X.columns)
    X_test = pd.DataFrame(X.values[test_ids, :], columns=X.columns)
    y_train = pd.DataFrame(y.values[tr_ids], columns=['Performance Index'])
    y_test = pd.DataFrame(y.values[test_ids], columns=['Performance Index'])
    return X_train, X_test, y_train, y_test


def std_scaler(df):
    cnt = 0
    shape = df.shape
    means = mean_vals(df, shape[0])
    devs = st_deviation(df, means, shape[0])
    for col in df.columns:
        df[col] = (df[col] - means[cnt]) / devs[cnt]
        cnt += 1


def prep_data(df):
    nan_check(df)
    cat_features(df)
    df_good = cat_features(df)
    #define_distrib(df_good)
    X_train, X_test, y_train, y_test = splitter(df_good, 0.3, 42)
    std_scaler(X_train)
    std_scaler(X_test)
    return X_train, X_test, y_train, y_test

