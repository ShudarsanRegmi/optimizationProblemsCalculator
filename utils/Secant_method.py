from prettytable import PrettyTable
from sympy import symbols, sympify

# Input function, value of x1, x2, symbol, and epsilon
f_x_input = input("Enter the function (e.g., x**2 + 3*x + 2): ")
x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
x_symbol = input("Enter the symbol for the function: ")
epsilon = float(input("Enter the value of epsilon: "))

# Define the symbol
x = symbols(x_symbol)

# Parse the input function
f_x = sympify(f_x_input)

# Define table
table = PrettyTable()
table.field_names = ['Iteration', 'x1', 'x2', 'x_new', '|| x2 - x_new ||']


# Function to calculate f(x) value
def f_value(x_value):
    return f_x.evalf(subs={x: x_value})


# Initialize variables
iteration = 1
table_rows = []

# Secant method loop
while abs(x2 - x1) > epsilon:
    f_x1 = f_value(x1)
    f_x2 = f_value(x2)

    if f_x2 == f_x1:  # Avoid division by zero
        print("Division by zero error in iteration", iteration)
        break

    x_new = x2 - (f_x2 * (x2 - x1)) / (f_x2 - f_x1)

    table_rows = [iteration, x1, x2, x_new, abs(x2 - x_new)]
    x1, x2 = x2, x_new
    iteration += 1

    table.add_row(table_rows)

# Print table
print(table)

# Output the results
print("Root (x):", x2)
print("Optimal Value of function at root (f(x)):", f_value(x2))
