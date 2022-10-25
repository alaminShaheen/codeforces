def solve(palindrome: str) -> None:
    for index in range(len(palindrome)):
        current_index_from_end = len(palindrome) - 1 - index
        if palindrome[index] != palindrome[current_index_from_end]:
            print("YES")
            if palindrome[index] == "a":
                print(palindrome[:index] + "a" + palindrome[index:])
            else:
                print(palindrome[:current_index_from_end] + "a" + palindrome[current_index_from_end:])
            return
        elif palindrome[index] != "a":
            print("YES")
            print(palindrome[:index] + "a" + palindrome[index:])
            return
    print("NO")


def take_input() -> None:
    n = int(input())

    while n:
        palindrome = input()
        solve(palindrome)
        n -= 1


take_input()
