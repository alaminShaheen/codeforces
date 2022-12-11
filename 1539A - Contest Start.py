# n = 4
# x = 2
# t = 5


#             <-----4----->
#         <-----3----->
#     <-----2----->
# <----1---->
# 0 1 2 3 4 5 6 7 8 9 10 11

# n = 3
# x = 1
# t = 2


#     <-3->
#   <-2->
# <-1->
# 0 1 2 3 4 5 6 7 8 9 10 11

# n = 4
# x = 4
# t = 3


#     <-3->
#         <--2-->
# <--1-->
# 0 1 2 3 4 5 6 7 8 9 10 11

# n = 4
# x = 4
# t = 4


#                 <---3--->
#         <---2--->
# <---1--->
# 0 1 2 3 4 5 6 7 8 9 10 11


# n = 6
# x = 1
# t = 8

#           <-------6------->
#         <-------5------->
#       <-------4------->
#     <-------3------->
#   <-------2------->
# <-------1------->
# 0 1 2 3 4 5 6 7 8 9 10 11

# if x >= t:
#     return n
# elif x < t:
#     n - (t - x - 1) * (t - x - 1) + (t - x - 2) * (t - x - 1) // 2

#  n  x  t
# 998 1 2000000000

def solve(n: int, x: int, t: int):
    dissatisfaction = 0
    if x <= t:
        dissatisfaction = 0
        dissatisfaction_per_person = t // x
        fully_dissatisfied_people = n - dissatisfaction_per_person
        if fully_dissatisfied_people >= 0:
            dissatisfaction += fully_dissatisfied_people * dissatisfaction_per_person
            dissatisfaction += ((dissatisfaction_per_person - 1) * dissatisfaction_per_person) // 2
        else:
            dissatisfaction += ((n - 1) * n) // 2
    print(dissatisfaction)


def take_input():
    for _ in range(int(input())):
        n, x, t = list(map(int, input().split()))
        solve(n, x, t)


take_input()
