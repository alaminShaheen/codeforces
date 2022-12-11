from typing import List


def solve(s: List[str]):
    reversing, moves = False, 0
    index = 0

    while index < len(s) and s[index] == "0":
        index += 1

    while index < len(s) and s[index] == "1":
        index += 1

    while index < len(s):
        if s[index] == "0" and not reversing:
            reversing = True
            moves += 1
        elif s[index] == "1" and reversing:
            reversing = False
            moves += 1

        while index < len(s) and s[index] == "0" and reversing:
            s[index] = "1"
            index += 1

        while index < len(s) and s[index] == "1" and not reversing:
            index += 1
    print(moves)


def take_input():
    for _ in range(int(input())):
        input()
        solve(list(input()))


take_input()
