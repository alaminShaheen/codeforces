from typing import List


def solve(arr: List[int]):
    left, right = -1, len(arr) - 1
    coins = 0

    while right >= 0:
        while right >= 0 and arr[right] >= 0:
            coins += arr[right]
            right -= 1

        if left == -1 or left > right:
            left = right - 1

        while left >= 0 and arr[left] <= 0:
            left -= 1

        if 0 <= left < right:
            if arr[left] >= abs(arr[right]):
                arr[left] -= abs(arr[right])
                arr[right] = 0
            else:
                arr[right] += abs(arr[left])
                arr[left] = 0
        else:
            break
    print(coins)


def take_input():
    for _ in range(int(input())):
        input()
        solve(list(map(int, input().split())))


take_input()
