import math
from sympy import sympify, symbols

def golden_section_method(f, a, b, tol=1e-5):
    # Define the golden ratio
    golden_ratio = (1 + math.sqrt(5)) / 2

    # Initialize points
    x1 = b - (b - a) / golden_ratio
    x2 = a + (b - a) / golden_ratio

    # Evaluate the function at the points
    f1 = f(x1)
    f2 = f(x2)

    while abs(b - a) > tol:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / golden_ratio
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / golden_ratio
            f1 = f(x1)

    # The minimum point is approximately at (a + b) / 2
    return (a + b) / 2

# Function to convert the user input into a function
def get_function_from_input(func_input):
    x = symbols('x')  # Symbolic variable
    expr = sympify(func_input)  # Convert string to a sympy expression
    return lambda val: float(expr.subs(x, val))  # Return a callable function

# User inputs
func_input = input("Enter the function f(x) you want to minimize (e.g., '4*x**3 + x**2 - 7*x + 14'): ")
a = float(input("Enter the start of the interval a: "))
b = float(input("Enter the end of the interval b: "))
tol = float(input("Enter the stopping tolerance value (e.g., 1e-5): "))

# Convert the input string into a usable function
f = get_function_from_input(func_input)

# Call the golden section method
min_x = golden_section_method(f, a, b, tol)
min_value = f(min_x)  # Calculate the minimum value of the function at min_x

print(f"The minimum value of the function is approximately at x = {min_x}, f(x) = {min_value}")
