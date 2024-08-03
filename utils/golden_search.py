# Golden Search method minimization

from sympy import symbols, sympify, SympifyError
from prettytable import PrettyTable

def get_input(prompt, cast_func):
    # Function to get input and apply cast_func. Until right type entered.
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

# Getting the function and the symbol in function as input
f_x_input = input("Enter the function: ")
x_symbol = input("Enter the function variable symbol: ")

x = symbols(x_symbol)
try:
    f_x = sympify(f_x_input)
except SympifyError:
    print("Invalid function. Please enter a valid function.")
    exit(1)

# Getting the left and right bounds to perform golden search
left_bound = get_input("Enter left bound: ", float)
right_bound = get_input("Enter right bound: ", float)
epsilon = get_input("Enter the epsilon value (tolerance): ", float)

# Initialize a table
table = PrettyTable()
table.field_names = ["No. of iteration", "L", "R", "X1", "X2", "f(x1)", "f(x2)", "Preserved limit"]

# Initializing all the required variables
iteration = 1

# Golden Search Method loop
while (right_bound - left_bound > epsilon):
    # Calculating everything that is required
    x2 = left_bound + 0.618 * (right_bound - left_bound)
    x1 = left_bound + right_bound - x2
    f_x1_val = f_x.subs(x_symbol, x1)
    f_x2_val = f_x.subs(x_symbol, x2)
    row = [iteration, left_bound, right_bound, x1, x2, f_x1_val, f_x2_val]
    preserve = "L"

    # If minimize then following conditions
    if f_x1_val <= f_x2_val:
        right_bound = x2
    else:
        left_bound = x1
        preserve = "R"
    
    # Appending the preserve value and adding the row to the table
    row.append(preserve)
    table.add_row(row) 
    iteration += 1

# Printing the outputs
print(table)

# The next iteration we just take left and right bound as that is enough
print("Minimum at = ", (left_bound + right_bound) / 2)
print("Optimal minimal value of given function is = ", f_x.subs(x_symbol, ((left_bound + right_bound) / 2)))
    