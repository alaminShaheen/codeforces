from typing import List


def solve(arr: List[int], target: int):
    lo, hi, ans = 0, len(arr) - 1, -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] <= target:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans + 1 if ans >= 0 else 0)


def take_input():
    int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for _ in range(int(input())):
        solve(arr, int(input()))


take_input()
