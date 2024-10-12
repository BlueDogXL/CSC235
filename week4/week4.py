import os # os module
import datetime

# currentDirectory = os.getcwd() # get Current Working Directory
# print(currentDirectory)

# filesList = os.listdir(path=currentDirectory)
# print(filesList)

#os.chdir(path='C:/Users/blued/OneDrive/Desktop')
#os.rename('python waz here.txt', 'get renamed idiot.txt')

# os.chdir(path='C:/Users/blued/OneDrive/Desktop')
# print(os.path.exists('get renamed idiot.txt')) # prints true (it is there)
# print(os.path.isfile('TTRPGs')) # prints false (it's a folder)
# os.makedirs('intro to python demo/New folder')
# os.rmdir('intro to python demo/New folder')
# os.removedirs('intro to python demo')
# for root, dirs, files in os.walk('C:/Users/blued/OneDrive/Desktop/TTRPGs'):
#     print(f"Current root: {root}")
#     print("Subdirectories:", dirs)
#     print("Files:", files)
print("Welcome to the RPG character generator!")
filePath = input("Please enter the filepath to where you would like the output file to be created. (Example: \"C:/Users/blued/OneDrive/Desktop\". Make sure to replace \ with /!) ") # 
rpgname = input("Please enter your character's name: ")
rpgclass = input("Please enter your character's class: ")
rpghp = input("Please enter a number for your characters health points: ")
rpgatk = input("Please enter a number for your character's attack stat: ")
rpgdef = input("Please enter a number for your character's defense stat: ")
rpgmag = input("Please enter a number for your character's magic stat: ")
os.chdir(path=filePath)
file = open("CSC235 assignment 4.1.txt", "w")
file.write(f"{rpgname.upper()} the {rpgclass.upper()}\n\nHP:  {rpghp}\nATK: {rpgatk}\nDEF: {rpgdef}\nMAG: {rpgmag}\n\nCreated {datetime.datetime.now()}")
print("File created!")