# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = str(input("What is your name: "))
age = int(input("How old are you: "))
age += 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")
