from typing import List


def solve(summands: List[int]):
    summands.sort()
    print("+".join(map(str, summands)))
    return


def take_input():
    summands = list(map(int, input().split("+")))
    solve(summands)


take_input()
