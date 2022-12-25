def solve(digits: str):
    soom = evens = zero = 0
    for digit in digits:
        soom += int(digit)
        evens += int(digit) % 2 == 0
        zero += int(digit) == 0
    print("red" if soom % 3 == 0 and evens > 1 and zero > 0 else "cyan")


def take_input():
    for _ in range(int(input())):
        solve(input())


take_input()
