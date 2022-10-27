def solve(distance: int):
    step = 5
    min_steps = 0
    while step and distance:
        min_steps += distance // step
        distance = distance % step
        step -= 1
    print(min_steps)


def take_input():
    distance = int(input())
    solve(distance)


take_input()
