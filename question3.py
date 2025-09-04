# Question 3: Using functions, write a program to compute the area and perimeter of a square. The program should ask the user to enter a number corresponding to the side length of the square and display the area and perimeter of the square.

# First we take input from the user
side = float(input("Enter the side of the square: "))

# We then Calculate area (side × side)
area = side * side

# Calculate perimeter (4 × side)
perimeter = 4 * side

# Step 4: Display the results
print("Perimeter =", perimeter, "and Area =", area)
