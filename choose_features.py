import seaborn as sns
import matplotlib.pyplot as plt
def show_corr_marix(X_train):
    corred = X_train.corr().round(2)
    sns.heatmap(corred, annot = True)
    plt.show()

def features_one(df):
    df_new = df.drop('Extracurricular Activities', axis = 1)
    return df_new

def features_two(df):
    df_new = df.drop('Hours Studied', axis = 1)
    return df_new

def features_three(df):
    df_new = df.drop('Sample Question Papers Practiced', axis = 1)
    return df_new
