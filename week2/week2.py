# # f-strings
# name = "Alex"
# age = 21
# print (f"My name is {name}, and I'm {age} years old.") # works
# # print ("My name is " + name +", and I'm" + age + "years old.") # does not work


# a = "test"
# print(a.upper()) # prints "TEST"
# print(f"{a.upper()}") # also prints "TEST"

# b = "we doin string arrays now"
# print(b[8:21]) # prints "string arrays"
# print(b[:14]) # prints "we doin string"
# print(b[15:]) # prints "arrays now"
# print(b[-5:-2]) # prints "s n"

#age = int(input("ok new age")) # makes age an int (inputs are strings by default)

# itemName = input("Enter the name of the item: ")
# itemPrice = float(input("Enter the price of the item: "))
# itemQuantity = int(input("Enter the number of items you're buying: "))

# totalPrice = round(((itemPrice * itemQuantity) * .9), 2)

# print(f"----------Receipt----------\n{itemName} x{itemQuantity}            {round((itemPrice * itemQuantity), 2)}\n10% off            -{round(((itemPrice * itemQuantity) * .1), 2)}\nTotal            {totalPrice}")

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# print(f"{x} + {y} = {x + y}")
# print(f"{x} - {y} = {x - y}")
# print(f"{x} * {y} = {x * y}")
# print(f"{x} / {y} = {x / y}")
# print(f"{x}^{y} = {x ** y}") # not ^

principal = float(input("Principal: "))
rate = (float(input("Rate of interest (as a percent): "))/100)
time = int(input("Number of years: "))
compoundsPerYear = int(input("Number of times compounded per year: "))
# simple: p * r * t
simple = principal * rate * time
# compound: A = P * (1+ r/n) ** (n * t)
compound = principal * (1 + (rate / compoundsPerYear)**(compoundsPerYear * time))
print(f"Simple interest: Principal ({principal}) * Interest rate ({rate}) * Years ({time}) = Interest amount ({simple})")
print(f"Compound interest: Principal ({principal}) * (1 + (Interest rate ({rate}) / Times compounded per year({compoundsPerYear}))^(Times compounded({compoundsPerYear}) * Years ({time}))) = {compound}")