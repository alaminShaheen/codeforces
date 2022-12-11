import string


def solve(latin: str, p: int):
    answer = []
    char_value_frequency = [[char, 0, 0] for char in string.ascii_lowercase]
    for char in latin:
        char_value_frequency[ord(char) - ord("a")] = [
            char,
            ord(char) - ord("a") + 1,
            char_value_frequency[ord(char) - ord("a")][2] + 1
        ]
    char_value_frequency.sort(key=lambda char_freq: char_freq[1])

    for index, [_, value, freq] in enumerate(char_value_frequency):
        if not value or value > p:
            char_value_frequency[index][1] = char_value_frequency[index][2] = 0
        else:
            if p // value <= freq:
                char_value_frequency[index][2] = p // value
            p -= char_value_frequency[index][1] * char_value_frequency[index][2]

    for letter in latin:
        for index, [char, _, freq] in enumerate(char_value_frequency):
            if letter == char and freq:
                answer.append(char)
                char_value_frequency[index][2] -= 1
    print("".join(answer))


def take_input():
    for _ in range(int(input())):
        solve(input(), int(input()))


take_input()
