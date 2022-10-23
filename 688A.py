from typing import List


def solve(attendances: List[List[int]]):
    max_consecutive, current_consecutive = 0, 0
    for attendance in attendances:
        if "0" in attendance:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 0
    print(max_consecutive)


def take_input():
    enemies, days = list(map(int, input().split()))
    attendances = []
    while days:
        attendances.append(input())
        days -= 1
    solve(attendances)


take_input()
