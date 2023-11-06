print('''-----------------------------------------------------------------
------------------------ SIMPLE CALCULATOR ----------------------
-----------------------------------------------------------------''')

while True:
    num1 = float(input("\n\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    def calculator(num1, num2, operation):
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2
        else:
            return "Invalid operation check your input..."

    result = calculator(num1, num2, operation)
    print("Result: ", result)
    
    X = input("\nDo you want to continue? (yes/no): ").lower()
    if X != 'yes':
        print("Thank You!")
        break





