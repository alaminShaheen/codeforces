from typing import List


def calculate_inversions(arr: List[int]) -> int:
    inversions = ones = 0

    for index in range(len(arr)):
        if arr[index]:
            ones += 1
        else:
            inversions += ones
    return inversions


def solve(arr: List[int]):
    inversions = calculate_inversions(arr)

    for index, num in enumerate(arr):
        if num == 0:
            arr[index] = 1
            inversions = max(inversions, calculate_inversions(arr))
            arr[index] = 0
            break

    for index in range(len(arr) - 1, -1, -1):
        if arr[index]:
            arr[index] = 0
            inversions = max(inversions, calculate_inversions(arr))
            arr[index] = 1
            break
    print(inversions)


def take_input():
    for _ in range(int(input())):
        input()
        solve(list(map(int, input().split())))


take_input()
