from typing import List


def solve(grid: List[List[str]]):
    for row in grid:
        if row[0] == "R" and row.count(row[0]) == len(row):
            print(row[0])
            return
    print("B")


def take_input():
    for _ in range(int(input())):
        input()
        grid = []
        for _ in range(8):
            grid.append(input())
        solve(grid)


take_input()
