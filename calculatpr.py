print("what do you want? ")
print("add ")
print("multiply ")
print("subtract ")
print("divide ")
while True:
    choice = input("Enter your choice: ")
    if choice in ('add', 'multiply', 'subtract', 'divide'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if choice == 'add':
           print(number1, "+", number2, "=", (number1 + number2))
        elif choice == 'multiply':
           print(number1, "*", number2, "=", (number1 * number2))
        elif choice == 'subtract':
           print(number1, "-", number2, "=", (number1 - number2))
        elif choice == 'divide':
           print(number1, "/", number2, "=", (number1 / number2))
        break
