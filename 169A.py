from typing import List


def solve(n: int, petya_chores: int, vasya_chores: int, chores: List[int]):
    chores.sort()
    print(chores[vasya_chores] - chores[vasya_chores - 1])


def take_input():
    n, petya_chores, vasya_chores = list(map(int, input().split()))
    chores = list(map(int, input().split()))
    solve(n, petya_chores, vasya_chores, chores)


take_input()
