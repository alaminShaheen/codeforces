from typing import List


def solve(arr: List[int]):
    n = len(arr)
    zero_pointer, one_pointer = 0, n - 1
    moves = 0

    while zero_pointer < one_pointer:
        while zero_pointer < n and arr[zero_pointer] == 0:
            zero_pointer += 1

        while one_pointer >= 0 and arr[one_pointer] == 1:
            one_pointer -= 1

        if zero_pointer < one_pointer:
            moves += 1
            zero_pointer += 1
            one_pointer -= 1
    print(moves)


def take_input():
    cases = int(input())

    while cases:
        n = int(input())
        solve(list(map(int, input().split())))
        cases -= 1


take_input()
