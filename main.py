import pandas as pd
from characteristics import *

df = pd.read_csv("Student_Performance.csv")
df_shape = shape(df)
df_nums = get_num_cols(df)
means = mean_vals(df_nums, df_shape[0])
standard_dev(df_nums, means)
min_max(df_nums)

