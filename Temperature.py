def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = getCelsius()
            break
        elif choice == "F":
            fahrenheit = getFahrenheit()
            break
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you.")


def getFahrenheit():
    fahrenheit = float(input("Celsius: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} F".format(celsius))
    return fahrenheit


def getCelsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))
    return celsius


main()
