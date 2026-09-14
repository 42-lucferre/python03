#!/usr/bin/env python3

import sys


class NoScores(Exception):
    pass


def parse(args: list[object]) -> list[int]:
    scores_list: list[int] = []
    if len(args) < 1:
        raise NoScores("No scores provided. Usage: python3 "
                       "ft_score_analytics.py <score1> <score2> ...")

    i: int = 0
    for arg in args:
        try:
            arg = int(arg)
            scores_list[len(scores_list):] = [arg]
            i += 1
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
            i += 1

    if len(scores_list) <= 0:
        raise NoScores("No scores provided. Usage: python3 "
                       "ft_score_analytics.py <score1> <score2> ...")
    return (scores_list)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        scores_list: list[int] = parse(sys.argv[1:])
        print(f"Scores processed: {scores_list}")
        print(f"Total players: {len(scores_list)}")
        print(f"Total score: {sum(scores_list)}")
        print(f"Avarage score: {sum(scores_list) / len(scores_list)}")
        print(f"High score: {max(scores_list)}")
        print(f"Low score: {min(scores_list)}")
        print(f"Score Range: {max(scores_list) - min(scores_list)}")
    except Exception as e:
        print(f"{e}")
