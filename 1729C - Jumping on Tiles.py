from collections import defaultdict


def solve(tiles: str):
    increment = 1 if tiles[0] <= tiles[-1] else -1
    prev_char = tiles[0]
    cost = visited = 0
    visited_indices_order = []
    char_indices = defaultdict(list)

    for index, char in enumerate(tiles):
        char_indices[char].append(index + 1)

    for order in range(ord(tiles[0]), ord(tiles[-1]) + increment, increment):
        char = chr(order)
        if char in char_indices:
            visited += len(char_indices[char])
            cost += abs(ord(prev_char) - order)
            visited_indices_order += char_indices[char]
            prev_char = char
    print(cost, visited)
    print(*visited_indices_order)


def take_input():
    for _ in range(int(input())):
        solve(input())


take_input()
