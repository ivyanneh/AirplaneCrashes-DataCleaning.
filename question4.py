# Write a program using functions that determines whether a character input by a user is uppercase or lower case.

# First I took a  character input from the user
ch = input("Enter any character: ")

# Next I Checked if the character is in lowercase
if ch.islower():
    print("You entered a Lowercase Letter")

# Finally I Checked if the character is in uppercase
if ch.isupper():
    print("You entered an Uppercase Letter")
