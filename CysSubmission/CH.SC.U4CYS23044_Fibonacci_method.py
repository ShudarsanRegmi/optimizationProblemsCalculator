import sympy as sp
from sympy.utilities.lambdify import lambdify
from fractions import Fraction

def generate_fibonacci_sequence(n):
    # Generate a Fibonacci sequence up to the (n+2)-th term
    fibonacci = [0, 1]
    for i in range(2, n + 2):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci

def perform_fibonacci_search(function, lower_bound, upper_bound, iterations):
    # Obtain the required Fibonacci sequence
    fibonacci_sequence = generate_fibonacci_sequence(iterations)
    
    # Initialize bounds for the search
    left = lower_bound
    right = upper_bound
    
    print(f"{'Iteration':<10} {'Ratio':<15} {'Left':<10} {'Right':<10} {'x1':<10} {'x2':<10} {'f(x1)':<10} {'f(x2)':<10} {'Interval'}")
    
    for i in range(1, iterations + 1):
        fib_next = fibonacci_sequence[iterations - i + 2]
        fib_current = fibonacci_sequence[iterations - i + 1]
        
        # Compute the ratio using Fibonacci numbers
        if fib_next != 0 and i != (iterations + 1):
            ratio_value = Fraction(fib_current, fib_next)
        else:
            ratio_value = float('inf')  # Prevent division by zero
        
        # Determine x1 and x2 within the interval [left, right]
        point2 = left + ratio_value * (right - left)
        point1 = left + right - point2
        
        # Evaluate the function at x1 and x2
        function_value1 = function(point1)
        function_value2 = function(point2)
        
        # Print current iteration details
        print(f"{i:<10} {str(ratio_value):<15} {left:<10.4f} {right:<10.4f} {point1:<10.4f} {point2:<10.4f} {function_value1:<10.4f} {function_value2:<10.4f} {'Right' if function_value1 > function_value2 else 'Left'}")
        
        # Adjust the interval based on function evaluations
        if function_value1 > function_value2:
            left = point1
            point1 = point2
            point2 = left + ratio_value * (right - left)
            function_value1 = function_value2
            function_value2 = function(point2)
        else:
            right = point2
            point2 = point1
            point1 = left + right - point2
            function_value2 = function_value1
            function_value1 = function(point1)
    
    # Return the midpoint of the final interval
    return (left + right) / 2

# Input from user for the objective function
try:
    input_expression = input("Enter the objective function (e.g., 'x**2 - 4*x + 4'): ")
    variable = sp.symbols('x')
    expression = sp.sympify(input_expression)
    func = lambdify(variable, expression, 'numpy')
except Exception as error:
    print(f"Function definition error: {error}")
    exit(1)

# Input for interval and iterations
try:
    start = float(input("Enter the starting point of the interval (e.g., 0): "))
    end = float(input("Enter the end point of the interval (e.g., 5): "))
    max_iterations = int(input("Enter the number of iterations (e.g., 10): "))
except ValueError as error:
    print(f"Invalid input: {error}")
    exit(1)

# Execute the Fibonacci search
optimal_point = perform_fibonacci_search(func, start, end, max_iterations)
print(f"The minimum is approximately at x = {optimal_point:.4f}")
print(f"The corresponding function value is f(x) = {func(optimal_point)}")
