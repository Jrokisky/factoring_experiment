import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Set the font size in the plots.
plt.rcParams.update({'font.size': 18})

# Read in the experimental results.
df_td = pd.read_csv('./results_trial_division.txt')
df_pr = pd.read_csv('./results_pollards_rho.txt')

# Compute input size in number of digits.
df_td['input_size'] = [len(str(e)) for e in df_td['n'].values]
df_pr['input_size'] = [len(str(e)) for e in df_pr['n'].values]

# Group by input size.
grouped_td = df_td.groupby('input_size')
grouped_pr = df_pr.groupby('input_size')

# Observed running times graph.
plt.figure(figsize=(14,10))
plt.errorbar(grouped_td.mean()[1:-1].index, grouped_td.mean()[1:-1]['run_pr'], grouped_td.std()[1:-1]['run_pr'], 
             linestyle='None', marker='^')
plt.errorbar(grouped_pr.mean()[1:-1].index, grouped_pr.mean()[1:-1]['run_pr'], grouped_pr.std()[1:-1]['run_pr'], 
             linestyle='None', marker='s')
plt.yscale('log')
plt.title('Time')
plt.xlabel('Input Size (digits)')
plt.ylabel('Log Scaled Observed Mean and Standard Deviation (seconds)')
plt.legend(['Trial Division','Pollard\'s Rho'])
plt.savefig('time.png')

# Observed space usage graph.
plt.figure(figsize=(14,10))
plt.errorbar(grouped_td.mean()[1:-1].index, grouped_td.mean()[1:-1]['peak'], grouped_td.std()[1:-1]['peak'], 
             linestyle='None', marker='^')
plt.errorbar(grouped_pr.mean()[1:-1].index, grouped_pr.mean()[1:-1]['peak'], grouped_pr.std()[1:-1]['peak'], 
             linestyle='None', marker='s')
plt.title('Space')
plt.xlabel('Input Size (digits)')
plt.ylabel('Observed Mean and Standard Deviation (bytes)')
plt.legend(['Trial Division','Pollard\'s Rho'])
plt.savefig('space.png')

# Trial division time regression analysis.
def f(x, p):
    return p * x**(1/2)
p_opt, p_cov = curve_fit(f, df_td['n'], df_td['run_pr'])
print('Trial division time optimal parameter:',p_opt)

# Trial division space regression analysis.
def f(x, p):
    return p
p_opt, p_cov = curve_fit(f, df_td['n'], df_td['peak'])
print('Trial division space optimal parameter:',p_opt)

# Pollard's Rho time regression analysis.
def f(x, p):
    return p * x**(1/4)
p_opt, p_cov = curve_fit(f, df_pr['n'], df_pr['run_pr'])
print('Pollard\'s Rho time optimal parameter:',p_opt)

# Pollard's Rho space regression analysis.
def f(x, p):
    return p
p_opt, p_cov = curve_fit(f, df_pr['n'], df_pr['peak'])
print('Pollard\'s Rho space optimal parameter:',p_opt)
