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


def find_factor(n, method):

    # Find a factor via trial division.
    if method == 'trial_division':
        tm.start()
        start_td = t.default_timer()
        td_factor = trial_division(n)
        end_td = t.default_timer()
        run_td = end_td - start_td
        current, peak = tm.get_traced_memory()
        tm.stop()
        print(f"\tTD | Factor: {td_factor} Run: {run_td} Peak Mem: {peak} bytes") 
        return td_factor, run_td

    # Find a factor via pollard's rho.
    elif method == 'pollards_rho':
        tm.start()
        start_pr = t.default_timer()
        pr_factor = pollards_rho(n)
        end_pr = t.default_timer()
        run_pr = end_pr - start_pr
        current, peak = tm.get_traced_memory()
        tm.stop()
        print(f"\tPR | Factor: {pr_factor} Run: {run_pr} Peak Mem: {peak} bytes") 
        return pr_factor, run_pr


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

        # Retry with a new seed value
        if d == num:
            x = r.randint(2, 100)
            y = x
            d = 1

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
        99991,
        400307,
        400331,
        1000003,
        10916449,
        14494619,
        100000007,
        949889989,
        5915587277,
        3367900313,
        73534323133,
        30369896303,
        101740496633,
        353373727757,
        3531577135439,
        9095665192937,
        27985032798461,
        81744303091421,
        320255973501901,
        973369606963379,
        2357353373727757,
        5111111111111119,
        37124508045065437,
        74747474747474747,
        618819619619660099,
        444444666868899899
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

