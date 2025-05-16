# Step 1: Get the year from the user
year = int(input("Enter a year: "))

# Step 2: Check the leap year conditions
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
