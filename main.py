import pandas as pd
from characteristics import get_characteristics
from prep import prep_data

df = pd.read_csv("Student_Performance.csv")
get_characteristics(df)
X_train, X_test, y_train, y_test = prep_data(df)

