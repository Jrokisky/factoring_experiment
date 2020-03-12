import pandas as pd

df_td = pd.read_csv('./results_trial_division.txt')
print(df_td.head())

df_pr = pd.read_csv('./results_pollards_rho.txt')
print(df_pr.head())

# https://stackoverflow.com/questions/22481854/plot-mean-and-standard-deviation
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html