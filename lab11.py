#1.wappto handle a zerodivisionerror exception when dividing a number zero
x = 14
y = 0

try:
    quot = x / y
except ZeroDivisionError:
    print("Please check the denominator. It is zero.")
#2.wapp that prompts user to input an integer and raises a valueerror exception if the input is not valid integer
   def get_integer_input(prompt):
    user_input = input(prompt)
    try:
        return int(user_input)
    except ValueError:
        raise ValueError(f"Invalid input: '{user_input}' is not a valid integer.")

# Example usage:
try:
    number = get_integer_input("Please enter an integer: ")
    print(f"You entered the integer: {number}")
except ValueError as e:
    print(e)

#write a python program that opena file and handles a file not found error Exception if file does not exsist

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# Example usage:
file_path = input("Enter the path to the file: ")

content = read_file(file_path)
if content is not None:
    print("File content:")
    print(content)
#write a python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical

def get_numerical_input(prompt):
    user_input = input(prompt)
    try:
        return float(user_input)
    except ValueError:
        raise TypeError(f"Invalid input: '{user_input}' is not a valid number.")

# Example usage:
try:
    number1 = get_numerical_input("Please enter the first number: ")
    number2 = get_numerical_input("Please enter the second number: ")
    print(f"You entered the numbers: {number1} and {number2}")
except TypeError as e:
    print(e)
