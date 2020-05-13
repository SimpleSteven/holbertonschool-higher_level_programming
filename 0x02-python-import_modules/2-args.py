#!/usr/bin/python3
if __name__ == "__main__":
    import sys
arguments_len = len(sys.argv)
if arguments_len < 2:
    print("0 arguments.")
else:
    print("{:d} arguments:".format(arguments_len - 1))
    for arg in range(1, arguments_len):
        print("{:d}: {:s}".format(arg, sys.argv[arg]))
