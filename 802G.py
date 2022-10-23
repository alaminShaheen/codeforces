def solve(string: str):
    needle = "heidi"

    if needle == string:
        print("NO")
        return

    curr_index = 0
    for char in string:
        if char == needle[curr_index]:
            curr_index += 1
        if curr_index >= len(needle):
            print("YES")
            return
    print("NO")


def take_input():
    string = input()
    solve(string)


take_input()
