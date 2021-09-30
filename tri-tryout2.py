def addition(number1, number2):
    return print(str(number1) + " + " + str(number2) + " = " + str(number1 + number2))

def subtraction(number1, number2):
    return print(str(number1) + " - " + str(number2) + " = " + str(number1 - number2))

def multiplication(number1, number2):
    return print(str(number1) + " x " + str(number2) + " = " + str(number1 * number2))

def division(number1, number2):
    return print(str(number1) + " : " + str(number2) + " = " + str(number1 / number2))

def increment(number):
    return print(str(number) + " + 1 = " + str(number + 1))

def decrement(number):
    return print(str(number) + " - 1 = " + str(number - 1))

def start():
    print("Hallo bij de rekenmachine.")
    x = input("Wat wil je berekenen: ")
    if x == "addition":
        number1 = input("nummer 1: ")
        number2 = input("number 2: ")
        addition((number1), (number2))
        start()
    elif x == "subtraction":
        number1 = input("nummer 1: ")
        number2 = input("number 2: ")
        subtraction((number1), (number2))
        start()
    elif x == "multiplication":
        number1 = input("nummer 1: ")
        number2 = input("number 2: ")
        multiplication((number1), (number2))
        start()
    elif x == "division":
        number1 = input("nummer 1: ")
        number2 = input("number 2: ")
        division((number1), (number2))
        start()
    elif x == "increment":
        number = input("number: ")
        increment(int(number))
        start()
    elif x == "decrement":
        number = input("number: ")
        decrement(int(number))
        start()
    else: print("invalid command, probeer opnieuw"), start()
start()

