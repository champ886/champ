print("Where are you from?", end = ' ')
country = input()
print("What is your name?", end = ' ')
name = input()
print("Where do you currently live?")
currentlocation = input()
print("How old are you?", end =" ")
age = float(input())
print(">>> age=", age, repr(age))
print(f"My name is {name}, I am from {country}. I currently live in {currentlocation}, and I am ", age, "years old" )