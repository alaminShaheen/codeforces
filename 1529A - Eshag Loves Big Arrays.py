from typing import List


def solve(arr: List[int]):
    minimum = min(arr)
    print(len(arr) - arr.count(minimum))


def take_input():
    cases = int(input())

    while cases:
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr)
        cases -= 1


take_input()
