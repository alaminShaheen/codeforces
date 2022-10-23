from typing import List


def solve(n: int, arthur: List[int], alexander: List[int]):
    apples = [1] * n

    for apple in alexander:
        if apple <= n:
            apples[apple - 1] = 2

    for apple in apples:
        print(apple, end=" ")


def take_input():
    n, a, b = list(map(int, input().split()))
    arthur = list(map(int, input().split()))
    alexander = list(map(int, input().split()))
    solve(n, arthur, alexander)


take_input()
