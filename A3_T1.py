
print("Program starting.")
print("")
print("Insert two integers.")
first_int = int(input("Insert first integer: "))

second_int = int(input("Insert second integer: "))
print("")
print("Comparing inserted integers...")
print("")
if(first_int < second_int):
    print("Second integer is greater.")
elif(first_int > second_int):
    print("First integer is greater.")
else:
    print(" Integers are the same")
print("")

print("Adding integers together...")
print(f"{first_int} + {second_int} = {sum}")
print("")
print("Checking the parity of the sum...")
if(Remainder == 0):
    print("Sum is even.")
else:
    print("Sum is odd")
print("")
print("Program ending.")
