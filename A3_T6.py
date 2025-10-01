
print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice1 = int(input("Your choice: "))

if choice1 == 1:
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    
Lenght_choice = int(input("Your choice: "))
if Lenght_choice == 1:
    meters = float(input("Insert meters: "))
    kilometers = float(meters / 1000)

    print(f"{meters} m is {kilometers} km")
    
elif Lenght_choice == 2:
    kilometers = float(input("Insert kilometers: "))
    meters = float(kilometers * 1000)
    print(f"{kilometers} km is {meters} m")

elif Lenght_choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.\n")


print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")


print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

choice2 = int(input("Your choice: "))
if choice2 == 2:
        print("Weight options:")
        print("1 - Grams to pounds")
        print("2 - Pounds to grams")
        print("0 - Exit")


Weight_choice = int(input("Your choice: "))

if Weight_choice ==1:
    grams = float(input("Insert grams:"))
    pounds = float(grams / 453.592)
    print(f"{grams} g is {pounds} lb")

elif Weight_choice ==2:
    pounds = float(input("Insert pounds:"))
    grams = float(pounds * 453.592)
    print(f"{pounds} kg is {grams} g")

elif Weight_choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.")


