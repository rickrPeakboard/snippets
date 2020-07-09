def printMenu():
    print("Welcome!")
    print("Choose a number from the menu and press enter to select a point")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiply")
    print("4: Division")
    print("5: Power")
    print("6: Modulus")
    print("0: Close")
    print("")
    return int(input("Selection: "))

while True:
    selection = printMenu()
    if selection == 0:
        # quit the application
        break
    elif selection == 1:
        # addition
        num1 = int(input("Insert the first number! "))
        num2 = int(input("Insert the second number! "))
        print(str(num1 + num2))
    elif selection == 2:
        # subtraction
        num1 = int(input("Insert the first number! "))
        num2 = int(input("Insert the second number! "))
        print(str(num1 - num2))
    elif selection == 3:
        # multiply
        num1 = int(input("Insert the first number! "))
        num2 = int(input("Insert the second number! "))
        print(str(num1 * num2))
    elif selection == 4:
        # division
        num1 = int(input("Insert the first number! "))
        num2 = int(input("Insert the second number! "))
        print(str(num1 / num2))
    else:
        print("Error: This functionality is not yet implemented.")
