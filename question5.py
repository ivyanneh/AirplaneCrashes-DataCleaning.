# Question 5:  The following is pseudocode for a program being designed. Write the Python program equivalent of the same.
   #BEGIN
   #SET x TO 0, y TO 20
   #REPEAT
   #SUBTRACT 4 FROM y
   #ADD 2/y TO x
   #UNTIL
   #y IS LESS THAN 6
   #DISPLAY x
   #END

# I started  with the given values
x = 0
y = 20

# I Kept repeating until y becomes less than 6
while y >= 6:
    y = y - 4        # This line of code subtracts 4 from y
    x = x + (2 / y)  # This line of code adds 2/y to x


print("Final x =", x)
