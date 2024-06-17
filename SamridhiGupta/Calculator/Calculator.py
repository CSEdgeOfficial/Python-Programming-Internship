def perform_operation(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"

def calculator():
    operations = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
        "quit": "end the program"
    }

    while True:
        print("Options:")
        for op, desc in operations.items():
            print(f"Enter '{op}' to {desc}")

        user_input = input("Enter your operator: ")

        if user_input == "quit":
            break
        elif user_input in operations:
            try:
                num1, num2 = map(float, input("Enter two numbers separated by space: ").split())

                result = perform_operation(user_input, num1, num2)

                print(f"Result: {num1} {user_input} {num2} = {result}")

            except ValueError:
                print("Invalid Input: Please enter two numerical values separated by space.")
        else:
            print("Invalid Input: Please enter a valid operator")

# Call the calculator function to start the program
calculator()
