import sympy as sp
from tabulate import tabulate

# Define function to calculate the index of Fibonacci series from series value.
def index_value_of_fib_series(series_value):
    if series_value == 1:
        return 0
    elif series_value == 2:
        return 2
    else:
        f0 = 1
        f1 = 1
        f2 = f1 + f0
        n = 2
        while f2 < series_value:
            f0 = f1
            f1 = f2
            f2 = f0 + f1
            n = n + 1
        return n + 1

# Define function to generate List of Fibonacci series up to series value.
def generate_fibonacci(index_of_fib_series):
    fib_list = [0] * (index_of_fib_series + 1)
    
    # Handling the base cases
    if index_of_fib_series >= 1:
        fib_list[0] = 1
    if index_of_fib_series >= 2:
        fib_list[1] = 1
    
    # Filling the list with Fibonacci numbers
    for i in range(2, index_of_fib_series + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    
    return fib_list

def fib_Array(n):
    if n < 0:
        return 1
    fib_array = generate_fibonacci(ittetration)
    return fib_array[n]

# Define the symbols
x = sp.symbols('x')

# Input function from user
f_expr_input = input("Enter the function containing x variables only: ")
f_expr = sp.sympify(f_expr_input)

# Get initial points and Precision Percentage
a, b = map(float, input("Enter the value of initial point (comma-separated): ").strip().split(','))
percentage = float(input("Enter the output Precision Percentage: "))

series_value = 100 / (2 * percentage)
ittetration = index_value_of_fib_series(series_value)

print("Given,")
print("Initial Point: (", a, ",", b, ")")
print("Precision Percentage(%) = ", percentage)
print("\n")

# List to store results for table display
table_data = []

for i in range(1, ittetration + 1):
    l0 = b - a
    itterations = i
    ratio = (fib_Array(ittetration - i) / fib_Array(ittetration - i + 1))
    x2 = a + ratio * l0
    x1 = (a + b) - x2
    f_x1_eqn = f_expr.subs({x: x1})
    f_x1 = sp.simplify(f_x1_eqn)
    f_x2_eqn = f_expr.subs({x: x2})
    f_x2 = sp.simplify(f_x2_eqn)

    table_data.append([itterations, ratio,a, b, x1, x2, f_x1, f_x2])
    
    if x1 <= x2:
        if f_x1 >= f_x2:
            a = x1
        else:
            b = x2

optimal_point = (a + b) / 2
optimal_eqn = f_expr.subs({x: optimal_point})
optimal_value = sp.simplify(optimal_eqn)

# Print the table
headers = ["Itterations","f(n-k)/f(n-k+1)","a", "b", "x1", "x2", "f(x1)", "f(x2)"]
print(tabulate(table_data, headers, tablefmt="grid"))

# Print the optimal point and value
print("The Optimal Point is:", optimal_point, "\nAnd The Optimal Value is:", optimal_value)
