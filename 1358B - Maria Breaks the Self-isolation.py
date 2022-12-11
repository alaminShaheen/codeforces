from typing import List


def solve(grannies: List[int]):
    grannies_in_yard = 1
    grannies.sort()

    pending_grannies = 0
    for granny in grannies:
        if granny <= grannies_in_yard + pending_grannies:
            grannies_in_yard += pending_grannies + 1
            pending_grannies = 0
        else:
            pending_grannies += 1
    print(grannies_in_yard)


def take_input():
    for _ in range(int(input())):
        input()
        grannies = list(map(int, input().split()))
        solve(grannies)


take_input()
