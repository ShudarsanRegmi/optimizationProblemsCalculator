from sympy import symbols, diff, sympify
from prettytable import PrettyTable

# Input function, value of x0, symbol, and epsilon
f_x_input = input("Enter the function (must be quadratic or greater degree, e.g., x**2 + 3*x + 2): ")
y = float(input("Enter the value of x0: "))
x_symbol = input("Enter the symbol for the function: ")
epsilon = float(input("Enter the value of epsilon: "))

# Define the symbol
x = symbols(x_symbol)

# Parse the input function
f_x = sympify(f_x_input)

# Define table
table = PrettyTable()
table.field_names = ['No. of iteration', 'x_n', "x_n+1 - x_n"]

# Find the first and second derivatives
derivative_f = diff(f_x, x)
derivative2_f = diff(derivative_f, x)

# Initialize variables
last = y + 2 * epsilon  # Ensure the loop starts
last2 = y


def derivative_values(x_value):
    f_prime = derivative_f.evalf(subs={x: x_value})
    f_double_prime = derivative2_f.evalf(subs={x: x_value})
    return f_prime, f_double_prime


def f_value(x_value):
    return f_x.evalf(subs={x: x_value})


iteration = 1  # Initializing iteration

# Newton's method loop
while abs(last2 - last) > epsilon:
    last = last2
    f_prime, f_double_prime = derivative_values(last2)

    if f_double_prime == 0:  # Prevent division by zero
        print(f"Division by zero error at iteration {iteration}")
        break

    last2 = last2 - (f_prime / f_double_prime)
    table_row = [iteration, last2, abs(last2 - last)]
    table.add_row(table_row)
    iteration += 1

# Printing table
print(table)

# Output the results
print("Least value (x):", last2)
print("Optimal Value of function (f(x)):", f_value(last2))
