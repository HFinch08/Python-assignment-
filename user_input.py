# Prompting the user for their name, age, and location
name = input("What is your name? ")
age = input("How old are you? ")
location = input("Where are you located? ")

# Printing out a personalized message
print("Hello {}, you are {} years old and live in {}.".format(name, age, location))