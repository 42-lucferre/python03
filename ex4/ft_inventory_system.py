#!/usr/bin/env python3

import sys


inventory = {}


def parse(args: list[str]) -> None:
    for arg in args:
        try:
            item = arg.split(':')
            if len(item) != 2:
                raise Exception
        except Exception:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            int(item[1])
        except Exception as e:
            print(f"Quantity error for '{item[0]}': {e}")
            continue
        if item[0] in inventory:
            print(f"Redundant item '{item[0]}' - discarding")
            continue
        inventory[item[0]] = int(item[1])


def most_finder(inventory: dict[str, int]) -> tuple[str, int]:
    most = (list(inventory)[0], list(inventory.values())[0])
    for key in inventory:
        if inventory[key] > most[1]:
            most = (key, inventory[key])
    return (most)


def least_finder(inventory: dict[str, int]) -> tuple[str, int]:
    least = (list(inventory)[0], list(inventory.values())[0])
    for key in inventory:
        if inventory[key] < least[1]:
            least = (key, inventory[key])
    return (least)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    parse(args)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(list(inventory.values()))}")

    for key in inventory:
        print(f"Item {key} represents "
              f"{inventory[key]/sum(list(inventory.values())) * 100:.1f}%")
    most = most_finder(inventory)
    least = least_finder(inventory)
    print(f"Item most abundant: {most[0]} with quantity {most[1]}")
    print(f"Item least abundant: {least[0]} with quantity {least[1]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
