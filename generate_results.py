from main import gen_semiprimes, find_factor
from collections import Counter
from tqdm import tqdm

nums = gen_semiprimes(return_factors=True)

with open('./results_trial_division.txt','w') as f:
	f.write(','.join(['n','p1','p2','pr_factor','run_pr','peak'])+'\n')

with open('./results_pollards_rho.txt','w') as f:
	f.write(','.join(['n','p1','p2','pr_factor','run_pr','peak'])+'\n')

for n in tqdm(nums):

	with open('./results_trial_division.txt','a') as f:
		res = find_factor(n[0], 'trial_division', verbose=False)
		f.write(','.join([str(n[0]),str(n[1]),str(n[2]),str(res[0]),str(res[1]),str(res[2])])+'\n')

	with open('./results_pollards_rho.txt','a') as f:
		res = find_factor(n[0], 'pollards_rho', verbose=False)
		f.write(','.join([str(n[0]),str(n[1]),str(n[2]),str(res[0]),str(res[1]),str(res[2])])+'\n')

#print(Counter([len(str(x)) for x in gen_semiprimes()]))
