


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

sign = input("Enter a mathematical sign (+, -, *, /): ")

match sign:
    case "+":
        print(number1 + number2)

    case "-":
        print(number1 - number2)

    case "*":   
        print(number1 * number2)

    case "/":
        print(number1 / number2)

    case _:
    	print("Invalid mathematical sign")
