def solve(H: int, L: int):
    ans = (L ** 2 - H ** 2) / (2 * H)
    print("%.13f" % ans)


def take_input():
    H, L = list(map(int, input().split()))
    solve(H, L)


take_input()
