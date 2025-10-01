
print("Program starting.")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    Celc = float(input("Insert the amount of Celsius: "))
    fahr = Celc * 1.8 + 32
    print(f"{Celc:.1f} °C equals to {fahr:.1f} °F")

elif choice == 2:
    fahr = float(input("Insert the amount of Fahrenheit: "))
    Celc = (fahr - 32) / 1.8
    print(f"{fahr:.1f} °F equals to {Celc:.1f} °C")

elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")


