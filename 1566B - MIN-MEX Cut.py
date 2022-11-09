def solve(binary: str):
    index = total_mex = 0

    while index < len(binary) and total_mex < 2:
        current_mex = 0
        while index < len(binary) and binary[index] == "0":
            current_mex = 1
            index += 1

        while index < len(binary) and binary[index] == "1":
            index += 1

        total_mex += current_mex

    print(2 if total_mex > 2 else total_mex)


def take_input():
    for _ in range(int(input())):
        solve(input())


take_input()
