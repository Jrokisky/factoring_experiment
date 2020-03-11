from main import gen_semiprimes, find_factor
from collections import Counter

#print(Counter([len(str(x)) for x in gen_semiprimes()]))

nums = gen_semiprimes(return_factors=True)[:4]  # Using 4 nums for testing.

with open('./results_trial_division.txt','w') as f:
	for n in nums:
		res = find_factor(n[0], 'trial_division')
		f.write(','.join([str(n[0]),str(n[1]),str(n[2]),str(res[0]),str(res[1])])+'\n')

with open('./results_pollards_rho.txt','w') as f:
	for n in nums:
		res = find_factor(n[0], 'pollards_rho')
		f.write(','.join([str(n[0]),str(n[1]),str(n[2]),str(res[0]),str(res[1])])+'\n')

# https://stackoverflow.com/questions/22481854/plot-mean-and-standard-deviation
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html