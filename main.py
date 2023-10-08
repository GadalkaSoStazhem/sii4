import pandas as pd
from characteristics import get_characteristics
from prep import prep_data
from lin_reg import make_lin_reg
from choose_features import *
from bonus_task import *
df = pd.read_csv("Student_Performance.csv")
get_characteristics(df)

df_1 = features_one(df)
df_2 = features_two(df)
df_3 = features_three(df)

print("Первый набор признаков:")
X_train, X_test, y_train, y_test = prep_data(df_1)
print("Признаки: ", X_train.columns, " зависимые данные: ", y_train.columns)
make_lin_reg(X_train, X_test, y_train, y_test)

print("Второй набор признаков:")
X_train, X_test, y_train, y_test = prep_data(df_2)
print("Признаки: ", X_train.columns, " зависимые данные: ", y_train.columns)
make_lin_reg(X_train, X_test, y_train, y_test)

print("Третий набор признаков:")
X_train, X_test, y_train, y_test = prep_data(df_3)
print("Признаки: ", X_train.columns, " зависимые данные: ", y_train.columns)
make_lin_reg(X_train, X_test, y_train, y_test)
#show_corr_marix(X_train)

print("Новый набор признаков:")
new_df = create_feature(df)
X_train, X_test, y_train, y_test = prep_data(new_df)
print("Признаки: ", X_train.columns, " зависимые данные: ", y_train.columns)
make_lin_reg(X_train, X_test, y_train, y_test)

