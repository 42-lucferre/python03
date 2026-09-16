#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    has_pos = 0
    while has_pos == 0:
        input_string = input("Enter new coordinates as floats "
                             "in format 'x,y,z': ")
        c = 0
        coordinates = ["", "", ""]
        for char in input_string:
            if char == ",":
                c += 1
            if c > 2:
                break
            if char != "," and char != " ":
                coordinates[c] += char
        if c > 2 or "" in coordinates:
            print("Invalid syntax")
            continue
        c = 0
        value_error = 0
        for coord in coordinates:
            try:
                float(coord)
            except (ValueError) as e:
                print(f"Error on parameter '{coord}': {e}")
                value_error = 1
        if not value_error:
            has_pos = 1

    X = float(coordinates[0])
    Y = float(coordinates[1])
    Z = float(coordinates[2])

    return (X, Y, Z)


if __name__ == "__main__":
    print("=== Game Cooordinate System ===")

    print("\nGet a first set of coordinates")
    first_tuple = get_player_pos()

    print(f"Got a first tuple: {first_tuple}")
    X1 = first_tuple[0]
    Y1 = first_tuple[1]
    Z1 = first_tuple[2]
    print(f"It includes: X={X1}, Y={Y1}, Z={Z1}")
    center_distance = math.sqrt((X1)**2 + (Y1)**2 + (Z1)**2)
    print(f"Distance to center: {round(center_distance, 4)}")

    print("\nGet a second set of coordinates")
    second_tuple = get_player_pos()
    X2 = second_tuple[0]
    Y2 = second_tuple[1]
    Z2 = second_tuple[2]
    points_distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2 + (Z2 - Z1)**2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(points_distance, 4)}")
