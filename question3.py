# Ask user for a number
number = int(input("Enter a number: "))

# Check if negative
if number < 0:
    print("Invalid input - negative numbers not allowed")

# Check if even
elif number % 2 == 0:
    print("The number is EVEN")

# Otherwise odd
else:
    print("The number is ODD")