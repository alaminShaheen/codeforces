def solve(rows: int, cols: int, k: int):
    print("YES" if (cols - 1 + cols * (rows - 1)) == k else "NO")


def take_input():
    cases = int(input())
    while cases:
        row, col, k = list(map(int, input().split()))
        solve(row, col, k)
        cases -= 1


take_input()
