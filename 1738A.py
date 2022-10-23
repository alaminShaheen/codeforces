from typing import List


def solve(power_type: List[int], power: List[int]):
    frost, fire = [], []
    answer = 0

    for index in range(len(power)):
        if power_type[index] == 1:
            frost.append(power[index])
        else:
            fire.append(power[index])

    frost.sort()
    fire.sort()

    if len(fire) == 0:
        print(sum(frost))
        return
    elif len(frost) == 0:
        print(sum(fire))
        return
    elif len(frost) == len(fire):
        if fire[0] <= frost[0]:
            print(fire[0] + 2 * (sum(fire[1:]) + sum(frost)))
        else:
            print(frost[0] + 2 * (sum(frost[1:]) + sum(fire)))
        return
    elif len(fire) < len(frost):
        fire, frost = frost, fire

    fire_start, frost_start = 0, 0
    if len(fire) != len(frost):
        answer = fire[0]
        fire_start += 1

    i, j = len(fire) - 1, len(frost) - 1

    while True:
        if i >= fire_start and j >= frost_start:
            answer += (2 * (fire[i] + frost[j]))
            i -= 1
            j -= 1
        elif i >= fire_start:
            answer += sum(fire[fire_start: i + 1])
            break
        elif j >= frost_start:
            answer += sum(frost[frost_start: j + 1])
            break
        else:
            break
    print(answer)
    return


def take_input():
    tests = int(input())

    while tests:
        n = int(input())
        power_type = list(map(int, input().split()))
        power = list(map(int, input().split()))
        solve(power_type, power)
        tests -= 1


take_input()
