# decorators

# def simpleDec(func):
#     def wrapper():
#         print("Start function")
#         func()
#         print("End function")
#     return wrapper

# @simpleDec
# def greet():
#     print("Hello!")

# greet()

# def argsDec(func):
#     def wrapper(*args, **kwargs):
#         print("Start function")
#         result = func(*args, **kwargs)
#         print("End function")
#     return wrapper

# @argsDec
# def add(a, b):
#     return a + b

# print(add(3,4))

# import os

# os.chdir(path='C:/Users/blued/OneDrive/Desktop')
# with open("numbers.txt", "r") as f:
#     content = f.read()
# print(type(content))
# print(content.split("\n"))

# num = int(input("Enter a number: "))

# if num % 2 == 0 and num > 0:
#     print(f"{num} is a postive even number!")
# else:
#         print(f"{num} isn't a positive even number!")

# for i in range(1, 10, 2):
#     print (i, end=" ")

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for i in numbers:
#     total += i

# def average(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     average = sum / args.__len__()
#     return average

# print(average(4,5,3,6))