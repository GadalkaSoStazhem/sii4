def create_feature(df):
    df_copy = df.copy()
    #общее количество потраченного на учебу времении
    df_copy['Study Time'] = df_copy['Hours Studied'] + df_copy['Sample Question Papers Practiced']
    return df_copy