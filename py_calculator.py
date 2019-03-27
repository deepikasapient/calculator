def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


def perform_operations(number_1, number_2):
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))


perform_operations(10, 20)
