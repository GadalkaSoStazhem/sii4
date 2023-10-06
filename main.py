import pandas as pd
from characteristics import get_characteristics

df = pd.read_csv("Student_Performance.csv")
get_characteristics(df)

