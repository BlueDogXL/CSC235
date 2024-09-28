#print("Hello,\nPython!") # \n makes a new line
#print("Hello,", "Python!") # comma adds a space for us
#print("Hello, " + "Python!") # plus does not add a space

#name = input("What is your name? ")
#print(name)

#print("testing\tthe backslash-t thing") # supposed to do like a tab thing? but in my terminal it just looked like a space tbh

print("Welcome to this tutorial!")
print("We're learning about the input function today!")
print("This is the syntax:\ninput(\"question\")") # backslash is an escape character so we can print quotation marks without it ending the print statement
print("For example:\ninput(\"What is your favorite game?\") would print \"What is your favorite game?\" and have a little indicator for where the user can input a response.\nWe can then save it to a variable and use it in other places.")
name = input("By the way, what is your name? ")
print(name + "! That's a nice name!")
print("Well, that's all for this tutorial. Seeya,", name + "!")