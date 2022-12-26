import math
from typing import List


def solve(arr: List[int]):
    exists = set(arr)
    pairs = []
    arr.sort()

    for left in range(len(arr) - 1):
        if len(pairs) >= math.floor(len(arr) / 2):
            break
        for right in range(left + 1, len(arr)):
            if len(pairs) >= math.floor(len(arr) / 2):
                break
            if arr[right] % arr[left] not in exists:
                pairs.append([arr[right], arr[left]])

    for pair in pairs:
        print(*pair)


def take_input():
    for _ in range(int(input())):
        input()
        solve(list(map(int, input().split())))


take_input()
