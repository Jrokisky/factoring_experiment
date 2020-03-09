import random as r
import argparse
import timeit as t
import math as m

# Good test numbers:
#    -> 636086005275917759

def main():

    # Parse user arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', type=int, default=12345, help='Number to find a factor of.')
    parser.add_argument('--digits', type=int, help='Number of digits of randomly generated integer to factor')
    parser.add_argument('--method', type=str, default='both', help='Factoring Method: both, trial_division or pollards_rho')
    args = parser.parse_args()

    # Ensure a valid factoring method was provided
    if args.method not in ['trial_division', 'pollards_rho', 'both']:
        parser.print_help()
        raise SystemExit()

    # Factor a randomly generated number or a given number.
    if args.digits is not None:
        num = gen_rand_int(args.digits)
    else:
        num = args.number

    print("Number to factor:")
    print(str(num))

    # Find a factor via trial division.
    if args.method == 'trial_division' or args.method == 'both':
        start_td = t.default_timer()
        td_factor = trial_division(num)
        end_td = t.default_timer()
        run_td = end_td - start_td
        print("TD | Factor: " + str(td_factor) + " Run: " + str(run_td)) 

    # Find a factor via pollard's rho.
    if args.method == 'pollards_rho' or args.method == 'both':
        start_pr = t.default_timer()
        pr_factor = pollards_rho(num)
        end_pr = t.default_timer()
        run_pr = end_pr - start_pr
        print("PR | Factor: " + str(pr_factor) + " Run: " + str(run_pr)) 

# Find a factor via trial division.
def trial_division(num):
    n = 2
    while n**2 < num:
        if num % n == 0:
            return n
        n += 1
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

    return d


# Generate a random integer of a certain number of digits.
def gen_rand_int(num_digits):
    rand = 0
    for n in range(0, num_digits):
        rand += r.randint(0, 9) * (10 ** n)
    return rand    

if __name__ == "__main__":
    main()

