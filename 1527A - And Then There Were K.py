def solve(n: int):
    binary_digit_count = len(bin(n)[2:])
    nearest_power_of_2 = "0b1" + "0" * (binary_digit_count - 1)
    print(int(nearest_power_of_2, 2) - 1)


def take_input():
    cases = int(input())

    while cases:
        solve(int(input()))
        cases -= 1


take_input()
