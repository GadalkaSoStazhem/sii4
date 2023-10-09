import pandas as pd
import numpy as np

def get_coeffs (X, y, n, m):
    values = np.empty((n, m + 1))
    ys = np.empty((n, 1),dtype=int)
    arr = np.array(y[y.columns[0]].values)
    ys[:, 0] = arr
    values[:, 0] = np.array([1] * n)
    cnt = 1
    for col in X.columns:
        values[:, cnt] = np.array(X[col].values)
        cnt += 1
    transp_vals = np.transpose(values)
    mult_matr = np.matmul(transp_vals, values)
    rev_matr = np.linalg.inv(mult_matr)
    mult_matr = np.matmul(rev_matr, transp_vals)
    res = np.matmul(mult_matr, ys)
    B = np.transpose(res)
    #b_coffs = np.linalg.inv(values.T @ values) @ values.T @ ys
    #print(b_coffs)
    return B[0]

def lin_reg_predict(X, B):
    e = B[0]
    coeffs = B[1:len(B)]
    mult_matr = np.matmul(X, coeffs)
    res = mult_matr + e
    return res

def r2_metric(y_true, y_pred):
    mean_y = sum(y_true) / len(y_true)
    rss = np.sum((t_y - p_y) ** 2 for t_y, p_y in zip(y_true, y_pred)) #residual sum of squares
    tss = sum((t_y - mean_y) ** 2 for t_y in y_true) #total sum of squares
    r_2 = 1 - (rss / tss)
    return r_2

def make_lin_reg(X_train, X_test, y_train, y_test):
    n, m = X_train.shape[0], X_train.shape[1]
    B = get_coeffs(X_train, y_train, X_train.shape[0], X_train.shape[1])
    y_pred = lin_reg_predict(X_test, B)
    r_2 = r2_metric(y_test.values, y_pred.values)
    print("R^2: ", r_2)

