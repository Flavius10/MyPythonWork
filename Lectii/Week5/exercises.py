# Ex. 1
nums = [1, 2, 3]

def some_function(num):
    return nums.append(num)

print(nums.append(4))
print(some_function(5))
print(nums)
print()

# a. [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]
# b. None, [1, 2, 3, 5], nums = [1, 2, 3]
# c. None, None, [1, 2, 3, 4, 5]
# d. None, None, [1, 2, 3]

# Ex. 2
print("Python" "is" "Python")

# a. Syntax Error
# b. Value Error
# c. Python is Python
# d. PythonisPython

# Ex. 3
values = ('a1', 'b2', 'c3')

print(dict(values))

# a. Value Error
# b. {'a': '1', 'b': '2', 'c': '3'}
# c. {'a': None, 'b': None, 'c': None}
# d. {'a1', 'b2', 'c3'}

# Ex. 4
a = 5 # variabilă globală

def func():
    # variabile locale
    a = 10

func()
print(a)
# a. 5
# b. 10
# c. Syntax Error
# d. Name Error

# Ex. 5
text = 'Python'

print(text[1::3])

# a. Syntax Error
# b. Ph
# c. yth
# d. yo

