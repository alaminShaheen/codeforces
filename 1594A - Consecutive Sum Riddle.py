def solve(n: int):
    print(-(n - 1), n)


def take_input():
    for _ in range(int(input())):
        solve(int(input()))


take_input()
