# b = 5
# if b > 10:
#     print("b is greater than 10!")
# elif b > 3:
#     print("b is greater than 3!")
# else:
#     print("neither of the other things happened")

# b = 10
# if b > 5:
#     if b < 15:
#         print("b is between 5 and 15!")
#     else:
#         print("b is greater than 15!")
# else:
#     print("b is less than 5!")

# username = "BlueDogbL"
# password = "12345"
# userTry = input("Enter username: ")
# passTry = input("Enter password: ")
# if userTry == username:
#     if passTry == password:
#         print("Access granted!")
#     else:
#         print("Access denied!")
# else:
#     print("Access denied!")

# totalPrice = 150
# if totalPrice > 100:
#     discountPercent = 0.1
# else:
#     discountPercent = 0.05
# print((totalPrice ) * (1 - discountPercent))

# b = 1
# result = "even" if b % 2 == 0 else "odd"
# print(result)

# def dummyFunction():
#     print("Dummy statement")

# b = 11

# if b > 10 or dummyFunction():
#     print("dummy value")

# b = 4
# y = 8

# b, y = y, b # swap the variables without a temp variable

# a, b, c, d = 1, 2, 3, 4
# print(a, b, c, d)
# if a > b and a > c and a > d:
#     print("A is the greatest!")
# if b > a and b > c and b > d:
#     print("B is the greatest!")
# if c > a and c > b and c > d:
#     print("C is the greatest!")
# if d > a and d > b and d > c:
#     print("D is the greatest!")
# else: print("what")

# n = int(input("Enter a number between 2 and 20: "))
# if n > 20 or n < 2:
#     print(f"{n} is outside the bounds.")
# elif n == 2 or n == 3:
#     print(f"{n} is prime!")
# elif n % 2 == 0 or n % 3 == 0:
#     print(f"{n} is not prime!")
# else:
#     print(f"{n} is prime!")

# list = ['one', 'two', 'three']
# for list_items in list:
#     print(list_items)

# for i in range(3):
#     print(i)

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# for i in range(3):
#     for j in range(2):
#         print(f"{i} , {j}")

# names = ['Aleb', 'Nat', 'Lulu']
# scores = [5, 1, 4]
# for name, score in zip(names, scores):
#     print(f"{name}: {score}")

# data = [10, -5, 20, -2, 10, -4]
# cleanData = []
# print("Data: ")
# for number in data:
#     print(number)
#     if number >= 0:
#         cleanData.append(number)
# print("Clean Data: ")
# for cleanNumber in cleanData:
#     print(cleanNumber)

# squaredValues = [b**2 for b in range(5)]
# print(squaredValues)

print("text adventure! except i don't have a text adventure in me and this is way too late so it's just gonna be kinda lame text that fulfills the technical requirements")
decision = chr(input("press 1 for option 1, 2 for option 2"))

if decision == 1:
    decision = chr(input("chosen so far: 1. press 1 for option 1, 2 for option 2"))

    if decision == 1:
        decision = chr(input("chosen so far: 1, 1. press 1 for option 1, 2 for option 2"))

        if decision == 1:
            decision = chr(input("chosen so far: 1, 1, 1. this ends the text adventure"))

        elif decision == 2:
            decision = chr(input("chosen so far: 1, 1, 2. this ends the text adventure"))

    elif decision == 2:
        decision = chr(input("chosen so far: 1, 2. press 1 for option 1, 2 for option 2"))

        if decision == 1:
            decision = chr(input("chosen so far: 1, 2, 1. this ends the text adventure"))

        elif decision == 2:
            decision = chr(input("chosen so far: 1, 2, 2. this ends the text adventure"))

elif decision == 2:
    decision = chr(input("chosen so far: 2. press 1 for option 1, 2 for option 2"))

    if decision == 1:
        decision = chr(input("chosen so far: 2, 1. press 1 for option 1, 2 for option 2"))
        if decision == 1:
            decision = chr(input("chosen so far: 2, 1, 1. this ends the text adventure"))

        elif decision == 2:
            decision = chr(input("chosen so far: 2, 1, 2. this ends the text adventure"))

    elif decision == 2:
        decision = chr(input("chosen so far: 2, 2. press 1 for option 1, 2 for option 2"))
        if decision == 1:
            decision = chr(input("chosen so far: 2, 2, 1. this ends the text adventure"))

        elif decision == 2:
            decision = chr(input("chosen so far: 2, 2, 2. this ends the text adventure"))