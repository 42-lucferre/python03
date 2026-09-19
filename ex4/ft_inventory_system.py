#!/usr/bin/env python3

import sys


inventory = {}


def parse(args: list[object]) -> None:
    for arg in args:
        try:
            item = arg.split(':')
            if len(item) != 2:
                raise Exception
        except Exception:
            print(f"Error - invalid parameter {arg}")
        try:
            item[1] = int(item[1])
        except Exception as e:
            print(f"Quantity error for '{item[0]}': {e}")
            continue
        if item[0] in inventory:
            print(f"Redundant item '{item[0]}' - discarding")
            continue
        inventory[item[0]] = item[1]
        print(inventory)



if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    parse(args)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(list(inventory.values()))}")

    most = None
    less = None
    most = inventory["sword"]
    print(f"{most}")
    for key in inventory:
        print(f"Item {key} represents "
              f"{inventory[key]/sum(list(inventory.values())) * 10:.1f}%")
        # if not most:
        #     most = inventory[key]
        # else:
        #     if

    print(f"Item most abundant: {most} with quantity")
