# Question 2: Write a program that asks a user to input the radius then the program calculates the volume of a sphere (the formula for the volume is (4/3)πr3 ). Use the exponential operator in python to compute (r3 ).

# Take integer input from the user
m = int(input("Enter the value of m: "))

# Construct the numbers mm (m repeated twice) and mmm (m repeated thrice)
# For Example: if m = 4, mm = 44
mm = int(str(m) * 2)    

# For Example: if m = 4, mmm = 444
mmm = int(str(m) * 3)   


# Display intermediate values for clarity
print("Step 1: m =", m)
print("Step 2: mm =", mm)
print("Step 3: mmm =", mmm)

# Compute the final result
value = m + mm + mmm

# Display the result
print("Final Step: m + mm + mmm =", value)
