from typing import List
import math


def solve(pieces: List[int]):
    great1, great2 = pieces[0], -math.inf

    for index in range(1, len(pieces)):
        if pieces[index] >= great1:
            great2 = great1
            great1 = pieces[index]
        elif pieces[index] > great2:
            great2 = pieces[index]
    print(great2 + great1)


def take_input():
    cases = int(input())

    while cases:
        n = int(input())
        pieces = list(map(int, input().split()))
        solve(pieces)
        cases -= 1


take_input()
