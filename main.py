import random as r
import argparse
import timeit as t
import math as m
import tracemalloc as tm

# Good test numbers:
#    -> 636086005275917759
#    -> 17314412934193618477343869685312819749443744906661

# General Notes:
# * my laptop could not factor 26635471789425906547647385926040984830917970985852013232301594943048742010847353 using pollard's rho method in 10 hours.
#
#
#
#
#

def main():

    # Parse user arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', type=int,  help='Number to find a factor of.')
    parser.add_argument('--digits', type=int, help='Number of digits of randomly generated integer to factor')
    parser.add_argument('--method', type=str, default='both', help='Factoring Method: both, trial_division or pollards_rho')
    args = parser.parse_args()

    # Ensure a valid factoring method was provided
    if args.method not in ['trial_division', 'pollards_rho', 'both']:
        parser.print_help()
        raise SystemExit()

    # Factor a randomly generated number or a given number.
    if args.digits is not None:
        nums = [gen_rand_int(args.digits)]
    elif args.number is not None:
        nums = [args.number]
    else:
        nums = gen_semiprimes()

    for n in nums:
        print("Finding factor of number: " + str(n) + "\n")
        # Find a factor via trial division.
        if args.method == 'trial_division' or args.method == 'both':
            find_factor(n, 'trial_division')
        # Find a factor via pollard's rho.
        if args.method == 'pollards_rho' or args.method == 'both':
            find_factor(n, 'pollards_rho')
        print("----------------------------------------------------\n")


def find_factor(n, method, verbose=True):

    # Find a factor via trial division.
    if method == 'trial_division':
        tm.start()
        start_td = t.default_timer()
        td_factor = trial_division(n)
        end_td = t.default_timer()
        run_td = end_td - start_td
        current, peak = tm.get_traced_memory()
        tm.stop()
        if verbose:
            print(f"\tTD | Factor: {td_factor} Run: {run_td} Peak Mem: {peak /10**6}MB") 
        return td_factor, run_td, peak

    # Find a factor via pollard's rho.
    elif method == 'pollards_rho':
        tm.start()
        start_pr = t.default_timer()
        pr_factor = pollards_rho(n)
        end_pr = t.default_timer()
        run_pr = end_pr - start_pr
        current, peak = tm.get_traced_memory()
        tm.stop()
        if verbose:
            print(f"\tPR | Factor: {pr_factor} Run: {run_pr} Peak Mem: {peak /10**6}MB") 
        return pr_factor, run_pr, peak


# Find a factor via trial division.
def trial_division(num):
    n = 2
    while n**2 <= num:
        if num % n == 0:
            return n
        if n == 2:
            n += 1
        else:
            n += 2
    return num

# Find a factor via pollard's rho.
def pollards_rho(num):
    x = 2
    y = 2
    d = 1

    fn = lambda x: (x**2 + 1) % num
    while d == 1:
        x = fn(x)
        y = fn(fn(y))
        d = m.gcd(abs(x-y), num)

    # Since we are only computing costs, we ignore the failure d = n.
    return d


# Generate a random integer of a certain number of digits.
def gen_rand_int(num_digits):
    rand = 0
    for n in range(0, num_digits):
        rand += r.randint(0, 9) * (10 ** n)
    return rand    

def gen_semiprimes(return_factors=False):
    primes = [
        10007,
        44701,
        65537,
        65701,
        90709,
        99989,
        99991,
        400307,
        400313,
        400321,
        400331,
        1000003,
        1023571,
        1074701,
        1120573,
        1203793,
        1258723,
        2233753,
        2535373,
        2935241,
        3241423,
        10000019,
        10916449,
        14494619,
        14641661,
        14689861,
        14829047,
        18303877,
        18518809,
        18771947,
        100000007,
        191681099,
        263123573,
        333667001,
        387423899,
        452942827,
        511729877,
        627626947,
        733353337,
        812182027,
        923850761,
        949889989,
        5915587277,
        1500450271,
        3267000013,
        5754853343,
        4093082899,
        9576890767,
        3628273133,
        2860486313,
        5463458053,
        3367900313
    ]
    semiprimes = []

    for p in primes:
        for r in primes:
            s = p * r
            if s not in semiprimes:
                if return_factors:
                    semiprimes.append((s,p,r))
                else:
                    semiprimes.append(s)

    return semiprimes
        

if __name__ == "__main__":
    main()

