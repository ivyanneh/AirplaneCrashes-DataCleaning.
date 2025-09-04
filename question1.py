"""
Question 1: Write a program that asks the user for a number of days. The program then
prints out the number of seconds in the amount of days given.
"""


hours_in_day = 24          # Number of hours in one day
minutes_in_hour = 60       # Number of minutes in one hour
seconds_in_minute = 60     # Number of seconds in one minute

# Ask the user to enter the number of days
num_days = int(input("Enter the number of days: "))

# Calculate total seconds using the formula
# total_seconds = days × hours × minutes × seconds
total_seconds = num_days * hours_in_day * minutes_in_hour * seconds_in_minute

# Display the result 
print("Total seconds in %d day(s) = %d" % (num_days, total_seconds))
