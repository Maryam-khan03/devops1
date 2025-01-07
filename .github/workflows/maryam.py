# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

# Function to divide two numbers
def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Function to find the maximum of two numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

# Main code to demonstrate the functions
if __name__ == "__main__":
    x = 10
    y = 5
    
    print(f"{x} + {y} = {add_numbers(x, y)}")
    print(f"{x} - {y} = {subtract_numbers(x, y)}")
    print(f"{x} * {y} = {multiply_numbers(x, y)}")
    print(f"{x} / {y} = {divide_numbers(x, y)}")
    print(f"Max of {x} and {y} is {max_of_two(x, y)}")
