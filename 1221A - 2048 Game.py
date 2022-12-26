from typing import List


def solve(nums: List[int]):
    print("YES" if sum(list(filter(lambda x: x <= 2048, nums))) >= 2048 else "NO")


def take_input():
    for _ in range(int(input())):
        input()
        solve(list(map(int, input().split())))


take_input()

8, 4, 3, 2


