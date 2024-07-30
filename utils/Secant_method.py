from prettytable import PrettyTable
from sympy import symbols, sympify, SympifyError


def get_input(prompt, cast_func):
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")


# Input function, value of x1, x2, symbol, and epsilon
f_x_input = input("Enter the function (e.g., x**2 + 3*x + 2): ")
x1 = get_input("Enter the value of x1: ", float)
x2 = get_input("Enter the value of x2: ", float)
x_symbol = input("Enter the symbol for the function: ")
epsilon = get_input("Enter the value of epsilon: ", float)

# Define the symbol
x = symbols(x_symbol)

# Parse the input function
try:
    f_x = sympify(f_x_input)
except SympifyError:
    print("Invalid function. Please enter a valid function.")
    exit(1)

# Define the table
table = PrettyTable()
table.field_names = ['No. of iteration', 'x1', 'x2', 'x_new', '|| x2 - x_new ||']


# Function to calculate f(x) value
def f_value(x_value):
    return f_x.evalf(subs={x: x_value})


# Initialize variables
x_new = x2  # Start with the initial guess
i = 1
maintable = []

# Secant method loop
while abs(x2 - x1) > epsilon:
    f_x1 = f_value(x1)
    f_x2 = f_value(x2)

    if f_x2 == f_x1:  # Avoid division by zero
        print("Division by zero error in iteration", i)
        break

    x_new = x2 - (f_x2 * (x2 - x1)) / (f_x2 - f_x1)
    table_rows = [i, round(x1, 5), round(x2, 5), round(x_new, 14), round(abs(x2 - x_new), 14)]
    x1, x2 = x2, x_new
    i += 1
    maintable.append(table_rows)

# Add rows to the table
for row in maintable:
    table.add_row(row)

# Print table
print(table)

# Output the results
print("Root (x):", round(x2, 14))
print("Optimal Value of function at root (f(x)):", round(f_value(x2), 14))
