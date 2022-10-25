def solve(n: int, k: int):
    result = []
    for number in range(1, n + 1):
        complement = abs(number - k)
        if number == k or (number != complement and number < complement < n):
            continue
        else:
            result.append(number)
    print(len(result))
    print(*result)


def take_input():
    cases = int(input())

    while cases:
        n, k = list(map(int, input().split()))
        solve(n, k)
        cases -= 1


take_input()
