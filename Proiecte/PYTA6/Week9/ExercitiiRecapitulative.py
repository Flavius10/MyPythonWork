"""Exercitiul 1"""


# def reverse(n: int):
#     if n < 0:
#         raise ValueError("Numarul trebuie sa fie mai mare ca si 0")
#     else:
#         return int(str(n)[::-1])
#
#
# print(reverse(1234567))
# print(reverse(10))


"""Exercitiul 2"""

# 1 2 3 4 5  2


# def rotate(lis: list, n: int):
#     if n > len(lis):
#         n = n - len(lis)
#     for i in range(len(lis)):
#         if i >= n:
#             print(lis[i], end=' ')
#     for i in range(len(lis)):
#         if i < n:
#             print(lis[i], end=' ')
#
#
# lista = [1, 2, 3, 4, 5]
# rotate(lista, 4)

"""Exercitiul 3"""


# def is_anagram(string1: str, string2: str):
#     stri = sorted(string1.lower())
#     stri2 = sorted(string2.lower())
#     return stri == stri2
#
#
# print(is_anagram('Adela', 'ealad'))
# print(is_anagram('ITFactory', 'acfiorty'))
# # print(is_anagram('Stringy', 'gringsty'))


"""Exercitiul 4"""


def get_second_biggest(numbers):
    frecv = [0] * int(len(numbers) + 1)
    for i in range(len(numbers)):
        frecv[numbers[i]] += 1

    unique = list(set(numbers))
    unique.sort(reverse=True)

    cnt = 1

    for i in range(len(unique)):
        if frecv[unique[i]] == 1:
            cnt += 1
        if frecv[unique[i]] == 1 and cnt == 2:
            print(unique[i])


get_second_biggest([-1,-2,-3,-4,-5])

