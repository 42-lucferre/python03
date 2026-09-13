#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    p_name: str = sys.argv[0]
    argc: int = len(sys.argv)

    print("=== Command Quest ===")

    print(f"Program name: {p_name}")
    if argc <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        c: int = 1
        for i in sys.argv[1:]:
            print(f"Argument {c}: {i}")
            c = c + 1
    print(f"Total arguments: {argc}")
