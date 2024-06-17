# Calculator Program

## Overview

This is a simple calculator program written in Python. It supports basic arithmetic operations including Addition, Subtraction, Multiplication, and Division. The user can interact with the program through a command-line interface to perform calculations.

## Features

- **Addition (`+`)**: Adds two numbers.
- **Subtraction (`-`)**: Subtracts the second number from the first number.
- **Multiplication (`*`)**: Multiplies two numbers.
- **Division (`/`)**: Divides the first number by the second number. If the second number is zero, it returns an error message.
- **Quit (`quit`)**: Ends the program.

## How to Use

1. Run the script to start the calculator.
2. The program will display a list of options for the available operations.
3. Enter the operator for the desired operation.
4. Enter two numbers separated by a space when prompted.
5. The result of the operation will be displayed.
6. To exit the program, enter `quit` when asked for the operator.

## Example
```
Options:
Enter '+' to add
Enter '-' to subtract
Enter '*' to multiply
Enter '/' to divide
Enter 'quit' to end the program
Enter your operator: +
Enter two numbers separated by space: 5 3
Result: 5.0 + 3.0 = 8.0
```

## Error Handling
The calculator program includes basic error handling to manage common errors:

1. **Division by Zero:**

- If the user attempts to divide by zero, the program will return the following error message: 
```
Enter your operator: /
Enter two numbers separated by space: 10 0
Result: 10.0 / 0.0 = Error: Division by zero is not allowed
```
2. **Invalid Numerical Input**

- If the user enters non-numerical values or an incorrect format for the numbers, the program will catch a ValueError and display the following message:
```
Enter your operator: +
Enter two numbers separated by space: 10 a
Invalid Input: Please enter two numerical values separated by space.
```
3. **Invalid Operator:**

- If the user enters an operator that is not supported, the program will display the following message: 
```
Enter your operator: %
Invalid Input: Please enter a valid operator
```

