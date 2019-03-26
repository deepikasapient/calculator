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

print("Please select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n")

# Take input from the user
select = input("Select operations from 1, 2, 3, 4 :")

def getinputs():

    number_1 = input("Enter first number: ")
    number_2 =  input("Enter second number: ")
    check_inputs(number_1, number_2)

def check_inputs(num1, num2):
    if not num1.isdigit() or not num2.isdigit():
        print("Please enter numerical values only")
        getinputs()
    else:
        num1 = int(num1)
        num2 = int(num2)
        perform_operations(num1,num2)

def perform_operations(number_1, number_2):
    if select == '1':
        print(number_1, "+", number_2, "=",
              add(number_1, number_2))

    elif select == '2':
        print(number_1, "-", number_2, "=",
              subtract(number_1, number_2))

    elif select == '3':
        print(number_1, "*", number_2, "=",
              multiply(number_1, number_2))

    elif select == '4':
        print(number_1, "/", number_2, "=",
              divide(number_1, number_2))
    else:
        print("Invalid input")

getinputs()

