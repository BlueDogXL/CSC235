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

import datetime
replay = True

def datetimeExplorer():
    choice = int(input("Which property of the datetime object would you like to view?\n1. Year\n2. Month\n3. Day\n4. Hour\n5. Minute\n6. Second\n7. Microsecond\n"))
    if choice == 1:
        print("Year:")
        print(f"A number between the MINYEAR constant, {datetime.MINYEAR}, and the MAXYEAR constant, {datetime.MAXYEAR} representing what year it is.")
        print(f"The current year is {datetime.datetime.today().year}.") # originally i thought about getting datetime.datetime.today before entering the choices but then the second and milleseconds wouldn't be right, and potentially neither would the minute. so i just call em in the strings to be more accurate.

    elif choice == 2:
        print("Month:")
        print("A number between 1 and 12 that represents what month it is.")
        print(f"The current month is {datetime.datetime.today().month}, {datetime.datetime.today().strftime('%B')}.") # i'm using strftime to get the name of the month. for example, choosing this option in december would yield "The current month is 12, December."
    elif choice == 3:
        print("Day:")
        print("A number between 1 and however many days are in the specified month. Represents the day of the month.")
        print(f"The current day is number {datetime.datetime.today().day}.")
    elif choice == 4:
        print("Hour:")
        print("A number between 1 and 24 representing an hour of the day.")
        print(f"The current hour is {datetime.datetime.today().hour}.")
    elif choice == 5:
        print("Minute:")
        print("A number between 0 and 59, representing the current minute of the hour.")
        print(f"The current minute is {datetime.datetime.today().minute}.")
    elif choice == 6: 
        print("Second:")
        print("A number between 0 and 59, representing the current second of the minute.")
        print(f"The current second is {datetime.datetime.today().second}. Or, well, it was.")
    elif choice == 7:
        print("Microsecond:")
        print("A number between 0 and 999999, representing the current microsecond of the second.")
        print(f"The current microsecond is {datetime.datetime.today().microsecond}. Er, at least it was, for a microsecond.")

def askPlayAgain(choice):
    global replay
    if choice.upper() == "Y":
        return True
    else:
        return False

while replay == True:
    datetimeExplorer()
    replay = askPlayAgain(input("Continue? Y/N\n"))
 












# import tkinter as tk
# root = tk.Tk()
# root.title("clock")
# root.geometry("480x270")
# clockTitle = tk.Label(root, text = "Clock").pack()
# dateLabel = tk.Label(root, text = f"Date: {today.month}/{today.day}/{today.year}").pack()
# timeLabel = tk.Label(root, text = f"Time: {today.hour}:{today.minute}:{today.second}").pack()

# def updateTime():
#     global today 
#     today = datetime.datetime.today()
#     root.update_idletasks()

# updateButton = tk.Button(root, text="Update Time", command=updateTime).pack()

# root.mainloop()