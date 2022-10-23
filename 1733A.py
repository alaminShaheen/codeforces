import math
from typing import List


def solve(arr: List[int], k: int):
    sum_of_k_elements = 0
    current_index = 0
    times = k
    while times:
        max_elem = -math.inf
        for index in range(current_index, len(arr), k):
            max_elem = max(max_elem, arr[index])
        sum_of_k_elements += max_elem
        current_index += 1
        times -= 1
    print(sum_of_k_elements)


def take_input():
    test_cases = int(input())
    while test_cases:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        solve(arr, k)
        test_cases -= 1


take_input()
