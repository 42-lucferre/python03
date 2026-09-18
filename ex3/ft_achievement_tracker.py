#!/usr/bin/env python3

import random


achievements = ['Crafting Genius', 'World Savior', 'Master Explorer',
                'Collector Supreme', 'Untouchable', 'Boss Slayer',
                'Strategist', 'Unstopable', 'Speed Runner', 'Survivor',
                'Tresaure Hunter', 'First Steps', 'Sharp Mind',
                'Hidden Path Finder']


def gen_player_achievements() -> set[str]:

    player_achievements = set(random.choices(achievements,
                              k=random.randint(0, 42)))

    return (player_achievements)


if __name__ == '__main__':
    print("=== Achievement Tracker System ===")

    p_alice = gen_player_achievements()
    p_bob = gen_player_achievements()
    p_charlie = gen_player_achievements()
    p_dylan = gen_player_achievements()

    print(f"\nPlayer Alice: {p_alice}")
    print(f"Player Bob: {p_bob}")
    print(f"Player Charlie: {p_charlie}")
    print(f"Player Dylan: {p_dylan}")

    print(f"\nAll distinct achievements: {p_alice.union(p_bob, p_charlie,
                                                        p_dylan)}")

    print(f"\nCommon achievements: {p_alice.intersection(p_charlie, p_bob,
                                                         p_dylan)}")

    print(f"\nOnly Alice has: {p_alice.difference(p_charlie, p_bob, p_dylan)}")
    print(f"Only Bob has: {p_bob.difference(p_charlie, p_alice, p_dylan)}")
    print(f"Only Charlie has: {p_charlie.difference(p_bob, p_alice, p_dylan)}")
    print(f"Only Dylan has: {p_dylan.difference(p_bob, p_alice, p_charlie)}")

    print(f"\nAlice is missing: {set(achievements).difference(p_alice)}")
    print(f"Bob is missing: {set(achievements).difference(p_bob)}")
    print(f"Charlie is missing: {set(achievements).difference(p_charlie)}")
    print(f"Dylan is missing: {set(achievements).difference(p_dylan)}")
