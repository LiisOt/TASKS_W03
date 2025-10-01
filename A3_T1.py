# Make Python program and implement if-statements in proper places.

# Ask user to insert two integers
# Compare the integers and then announce the greater number
# Create sum of the two integers
# Check the parity of the sum (see modulo-operator ‘%’)
# Other possible output variants:

# Integer comparison
# Integers are the same.
# First integer is greater.
# Parity check
# Sum is even.
# Example program run

# run 1 run 2 run 3
# Program starting.
print("Program starting.")
# Insert two integers.
print("")
print("Insert two integers.")
# Insert first integer: 5
first_int = int(input("Insert first integer: "))

# Insert second integer: 5
second_int = int(input("Insert second integer: "))
print("")
# Comparing inserted integers.
print("Comparing inserted integers...")
print("")
if(first_int < second_int):
    print("Second integer is greater.")
elif(first_int > second_int):
    print("First integer is greater.")
else:
    print(" Integers are the same")
# Integers are the same
print("")
# Adding integers together
print("Adding integers together...")
# 5 + 5 = 10
sum = first_int + second_int
print(f"{first_int} + {second_int} = {sum}")
print("")
# Checking the parity of the sum...
print("Checking the parity of the sum...")
Remainder = sum % 2
# Sum is even.
if(Remainder == 0):
    print("Sum is even.")
else:
    print("Sum is odd")
# Program ending.
print("")
print("Program ending.")