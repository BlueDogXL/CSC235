# def function_name(parameters):
#     value = parameters # insert whatever logic here
#     return value

# def Greet(name):
#     print(f"Hello, {name}!")



# def addScore(currentScore, scoreToAdd):
#     newScore = currentScore + scoreToAdd
#     print(f"Score: {newScore}")
#     return newScore
# score = 45
# pointsGained = 20


# import random
# def rollDie():
#     return random.randint(1,6)


# def getArea(length, width = None):
#     if width == None:
#         area = length**2
#         return area
#     else:
#         area = length * width
#         return area

# def main():
#     function_name("arguments")
#     Greet("Alex")
#     addScore(score, pointsGained)
#     print(rollDie())
#     print(getArea(4))
#     print(getArea(4,5))


# main()



# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def main():
#     print("main start!")
#     print(add(2,3))
#     print(subtract(5,3))

# if __name__ == "__main()__":
#     main()

# psuedocode stuff
# start
# set the current balance to 1000
# while true:
    # display options
        # 1: check balance
        # 2: withdraw money
        # 3: exit
    # get user input
        # if input is check balance
            # display balance
        # if input is withdraw money
            # ask how much
            # if it's less than balance
                # subtract from balance
        # if input is exit
            # exit
# currentBalance = 1000
# while True:
#     print("Select an option: \n1: Check balance\n2:Withdraw\n3: Exit")
#     userInput = input()
#     if userInput == 1:
#         print(f"Your current balance is {currentBalance}.")
#     elif userInput == 2:
#         withdrawl = float(input("How much are you withdrawing?"))
#         if withdrawl <= currentBalance:
#             if withdrawl > 0:
#                 currentBalance -= withdrawl
#                 print(f"You have withdrawn {withdrawl}! Your current balance is {currentBalance}.")
#             else: print("Can't withdraw less than 0!")
#         else: print("You don't have that much!")
#     elif userInput == 3:
#         print("Goodbye!")
#         break
#     else: print("Invalid input!")


# def sumOfAll(*args):
#     result = 0
#     for num in args:
#         result = result + num
#     return result

# print(sumOfAll(10))
# print(sumOfAll(1, 2, 3))
# print(sumOfAll(1, 2, 3, 4, 5, 6, 7, 8, 9))


eaten = False
replay = True
def intro():
    print("You are in a room with a marshmallow. You can either eat the marshmallow immediately, or wait 15 minutes and get two marshmallows.")
    firstChoice(input("Do you eat the marshmallow? \n No (A) \n Yes (B) \n > "))

def firstChoice(choice):
    global eaten # this is here for scope reasons!
    if choice.upper() == "A":
        print(" > No")
        print("You leave the marshmallow where it is. It sure does look good, though...")
    elif choice.upper() == "B":
        eaten = True
        print(" > Yes")
        print("You eat the marshmallow. Delicious!")
    else: firstChoice(input("> "))
    if eaten == False:
        secondChoice(input("5 minutes have passed. Do you eat the marshmallow? \n No (A) \n Yes (B) \n > "))
    else:
        secondChoice("B")

def secondChoice(choice):
    global eaten
    if choice.upper() == "A":
        eaten = False
        print(" > No")
        print("You leave the marshmallow where it is. It's not getting any less tasty-looking...")
    elif choice.upper() == "B" and eaten == True:
        print("Five minutes pass.")
    elif choice.upper() == "B":
        eaten = True
        print(" > Yes")
        print("You eat the marshmallow. Delicious!")
    else: secondChoice(input("> "))
    if eaten == False:
        thirdChoice(input("10 minutes have passed. Do you eat the marshmallow? \n No (A) \n Yes (B) \n > "))
    else:
        thirdChoice("B")

def thirdChoice(choice):
    global eaten
    if choice.upper() == "A":
        eaten = False
        print(" > No")
        print("You leave the marshmallow where it is. And then...")
    elif choice.upper() == "B" and eaten == True:
        print("Another five minutes pass. And then...")
    elif choice.upper() == "B":
        print(" > Yes")
        print("You eat the marshmallow. Delicious!")
    else: thirdChoice(input("> "))
    ending()

def ending():
    print("A researcher enters the room. The fifteen minutes are over! They check the table...")
    if eaten == True:
        print("... to see the marshmallow gone. They escort you out of the room. \nYou got one marshmallow! Hope it was worth it.")
    else:
        print("... to see the marshmallow still there. They pull another marshmallow from inside their coat, and hand both of them to you. They escort you out of the room. \nYou got two marshmallows! And after staring at that one for so long, you're ready to dig in.")

def askPlayAgain(choice):
    global replay
    if choice.upper() == "Y":
        return True
    else:
        return False

while replay == True:
    eaten = False # resets the choice on repeat playthroughs
    intro()
    replay = askPlayAgain(input("Play again? Y/N "))
    

