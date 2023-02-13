#!/usr/bin/python3

import sys

def main():
    if len(sys.argv) == 2:
        print("Hello, " + sys.argv[1] + "!")
    else:
        print("Hello, World!")

if __name__ == "__main__":
    main() 

