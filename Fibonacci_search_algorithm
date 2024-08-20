import sympy as sp
from sympy.utilities.lambdify import lambdify
from fractions import Fraction

def fibonacci_numbers_up_to_k(k):
    # Generate Fibonacci numbers up to the k-th number
    fibs = [0, 1]
    for i in range(2, k + 2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def fibonacci_search(f, a, b, k):
    # Generate Fibonacci numbers up to k
    fibs = fibonacci_numbers_up_to_k(k)
    
    # Initialize variables for the search
    L = a
    R = b
    print(f"{'k':<5} {'Fn−k/Fn−k+1':<15} {'L':<10} {'R':<10} {'x1':<10} {'x2':<10} {'f(x1)':<10} {'f(x2)':<10} {'L/R':<10}")
    
    for iteration in range(1, k + 1):
        fib_n_minus_1 = fibs[k - iteration + 2]
        fib_n_minus_2 = fibs[k - iteration + 1]
        
        # Calculate ratio for Fn−k/Fn−k+1
        if fib_n_minus_1 != 0 and iteration != (k + 1):
            ratio = Fraction(fib_n_minus_2, fib_n_minus_1)
        else:
            ratio = float('inf')  # Avoid division by zero if fib_n_minus_1 is 0
        
        # Compute x2 and x1 based on the given formulas
        x2 = L + ratio * (R - L)
        x1 = L + R - x2
        
        # Evaluate function values
        f_x1 = f(x1)
        f_x2 = f(x2)
        
        # Print the results of the iteration
        print(f"{iteration:<5} {str(ratio):<15} {L:<10.4f} {R:<10.4f} {x1:<10.4f} {x2:<10.4f} {f_x1:<10.4f} {f_x2:<10.4f} {'R' if f_x1 > f_x2 else 'L':<10}")
        
        # Update the interval based on function evaluations
        if f_x1 > f_x2:
            L = x1
            x1 = x2
            x2 = L + ratio * (R - L)
            f_x1 = f_x2
            f_x2 = f(x2)
        else:
            R = x2
            x2 = x1
            x1 = L + R - x2
            f_x2 = f_x1
            f_x1 = f(x1)
    
    return (L + R) / 2

# Define the symbolic expression and convert it to a numerical function
try:
    expr_str = input("Enter the objective function (e.g., 'x**2 - 4*x + 4'): ")  # User input for function
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    f = lambdify(x, expr, 'numpy')
except Exception as e:
    print(f"Error in defining the function: {e}")
    exit(1)

# Define the interval and number of iterations
try:
    a = float(input("Enter the start of the interval (e.g., 0): "))  # User input for interval start
    b = float(input("Enter the end of the interval (e.g., 5): "))    # User input for interval end
    k = int(input("Enter the number of iterations (e.g., 10): "))   # User input for number of iterations
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

# Call the Fibonacci search function and print the result
min_x = fibonacci_search(f, a, b, k)
print(f"The minimum point is at x = {min_x:.4f}")
print(f"The minimum value is f(x)={f(min_x)}")
