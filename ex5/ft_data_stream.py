#!/usr/bin/env python3

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str]]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["climb", "eat", "grab", "move", "release",
               "run", "sleep", "swim"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(event_list:
                  list[tuple[str, str]]) -> typing.Generator[tuple[str, str]]:
    for _ in range(len(event_list)):
        event = random.randint(0, len(event_list) - 1)
        extract = event_list[event]
        event_list[event:event + 1] = []
        yield extract


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    events = gen_event()
    for i in range(1000):
        event = next(events)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = [next(events) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    extracts = consume_event(event_list)
    for _ in range(10):
        extract = next(extracts)
        print(f"Got event from list: {extract}")
        print(f"Remains in list {event_list}")
