import math


def solve(n: int):
    ans = math.ceil(n / 2)
    print(ans)
    left, right = 1, 3 * n

    while ans:
        print(left, right)
        left += 3
        right -= 3
        ans -= 1


def take_input():
    for _ in range(int(input())):
        solve(int(input()))


take_input()
