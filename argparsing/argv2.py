import argparse

# define an parser object

parser = argparse.ArgumentParser()

parser.add_argument("greeting", help="the greeting messange displayed")
parser.add_argument("-n", "--numbers", type=float, nargs=2, help="the number to be added")

args = parser.parse_args()

print(args.numbers)

if args.numbers is not None:
    print(args.numbers[0] + args.numbers[1])
