#!/usr/bin/env python3

import random

players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john",
           "kevin", "Liam"]

players_cap_all = [player.capitalize() for player in players]
players_cap_only = [player for player in players
                    if player == player.capitalize()]

score = {key: random.randint(0, 1000) for key in players_cap_all}

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    print(f"\nInitial list of players: {players}")
    print(f"New list with all names capitalized: {players_cap_all}")
    print(f"New list of capitalized names only: {players_cap_only}")

    print(f"\nScore dict: {score}")
    avarage = round(sum(list(score.values()))/len(score), 2)
    print(f"Score average is: {avarage}")
    above_avarage = {key: score[key] for key in score if score[key] > avarage}
    print(f"High scores: {above_avarage}")
