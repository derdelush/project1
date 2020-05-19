while True:
        number1 = input("Please input the first number: ")
        number2 = input("Please input the second number: ")
        try:
            number1 = float(number1)
            number2 = float(number2)
        except:
            print("Please use numerals")
        else:
            break

operation = input("Please choose operation (+ - * /): ")

if operation == "+":
    addition = number1 + number2
    print(addition)
elif operation == "-":
    subtraction = number1 - number2
    print(subtraction)
elif operation == "*":
    multiplication = number1 * number2
    print(multiplication)
elif operation == "/":
    division = number1 / number2
    print(division)
else:
    print("ERROR")
