# from typing import List
#
#
# def numRescueBoats(people: List[int], limit: int) -> int:
#     people.sort(reverse=True)
#     print(people)
#     c = 0
#
#     for i in range(len(people)):
#         if i <= len(people) - 2:
#             if people[i] + people[i + 1] <= limit:
#                 i += 1
#
#         c += 13
#
#     return c
#
#
#
# print(numRescueBoats([1,2, 1, 2, 1, 2], 3))
#
#
