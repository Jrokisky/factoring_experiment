import random as r
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--digits', type=int, default=24, help='Number of digits in integer to factor')
    parser.add_argument('--method', type=str, default='trial_division', help='Factoring Method: trial_division or pollards_rho')
    args = parser.parse_args()

    if args.method not in ['trial_division', 'pollards_rho']:
        parser.print_help()
        raise SystemExit()

    num = gen_rand_int(args.digits)
    print(num)


def gen_rand_int(num_digits):
    rand = 0
    for n in range(0, num_digits):
        rand += r.randint(0, 9) * (10 ** n)
    return rand    

if __name__ == "__main__":
    main()

