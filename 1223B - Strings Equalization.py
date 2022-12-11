def solve(s: str, t: str):
    print("YES") if set(s).intersection(set(t)) else print("NO")


def take_input():
    for _ in range(int(input())):
        s = input()
        t = input()
        solve(s, t)


take_input()
