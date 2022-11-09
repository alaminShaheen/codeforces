from typing import List


def solve(arr: List[int]):
    print(max(arr) - min(arr))


def take_input():
    for _ in range(int(input())):
        input()
        arr = list(map(int, input().split()))
        solve(arr)


take_input()
