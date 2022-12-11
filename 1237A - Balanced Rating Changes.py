import math
from typing import List


def solve(ratings: List[int]):
    plus = minus = 0
    old = ratings[:]

    for index in range(len(ratings)):
        if ratings[index] % 2 == 0:
            ratings[index] //= 2
        else:
            if ratings[index] < 0:
                ratings[index] = math.ceil(ratings[index] / 2)
            else:
                ratings[index] = math.floor(ratings[index] / 2)

        if ratings[index] >= 0:
            plus += ratings[index]
        else:
            minus += ratings[index]

    index = 0
    while index < len(ratings):
        if old[index] % 2 != 0:
            if old[index] < 0 and plus > abs(minus):
                ratings[index] -= 1
                minus -= 1
            elif old[index] > 0 and plus < abs(minus):
                ratings[index] += 1
                plus += 1
        print(ratings[index])
        index += 1


def take_input():
    ratings = []
    for _ in range(int(input())):
        ratings.append(int(input()))
    solve(ratings)


take_input()
