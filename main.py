import random as r
import argparse
import timeit as t


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--digits', type=int, default=24, help='Number of digits in integer to factor')
    parser.add_argument('--method', type=str, default='both', help='Factoring Method: both, trial_division or pollards_rho')
    args = parser.parse_args()

    if args.method not in ['trial_division', 'pollards_rho', 'both']:
        parser.print_help()
        raise SystemExit()

    num = gen_rand_int(args.digits)
    print("Number to factor:")
    print(str(num))

    if args.method == 'trial_division' or args.method == 'both':
        start_td = t.default_timer()
        td_factors = trial_division(num)
        end_td = t.default_timer()
        run_td = end_td - start_td
        print("TD | Factors: " + td_factors + " Run: " + str(run_td)) 

    if args.method == 'pollards_rho' or args.method == 'both':
        start_pr = t.default_timer()
        pr_factors = pollards_rho(num)
        end_pr = t.default_timer()
        run_pr = end_pr - start_pr
        print("PR | Factors: " + pr_factors + " Run: " + str(run_pr)) 


def trial_division(num):
    n = 1
    small_factors = []
    large_factors = []
    while n**2 < num:
        if num % n == 0:
            small_factors.append(n)
            large_factors.insert(0, num // n)
        n += 1
    factors = small_factors + large_factors

    return ','.join(str(f) for f in factors)


def pollards_rho(num):
    return ""



def gen_rand_int(num_digits):
    rand = 0
    for n in range(0, num_digits):
        rand += r.randint(0, 9) * (10 ** n)
    return rand    

if __name__ == "__main__":
    main()

