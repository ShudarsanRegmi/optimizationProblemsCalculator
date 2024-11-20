import streamlit as st
import sympy as sp
from tabulate import tabulate

st.write("# Fibonacci Method Calculator")

data = st.text_input("Enter the function (e.g., x**2 + 3*x + 2):", "x**2 + 3*x + 2")

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
f_expr_input = data.strip()  # Trim whitespace
if f_expr_input:
    try:
        f_expr = sp.sympify(f_expr_input)
    except (sp.SympifyError, SyntaxError) as e:
        st.error(f"Error in input: {e}")
        st.stop()  # Stop execution if input is invalid
else:
    st.warning("Please enter a valid equation.")
    st.stop()  # Stop execution if input is empty

# Get initial points and Precision Percentage
col1, col2, col3  = st.columns(3)
a = col1.number_input("Enter the initial Point (x1)", value=0)
b = col2.number_input("Enter the final point (x2)", value=1)
percentage = col3.number_input("Enter the Tolerance Value", min_value=0.0, max_value=10.0, value=1.0)

series_value = 100 / (2 * percentage)
ittetration = index_value_of_fib_series(series_value)

st.write(" ")
st.write("#### Solution,")
st.write("Given,")
st.write("Initial Point: (", a, ",", b, ")")
st.write("Precision Percentage(%) = ", percentage)

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

    if f_x1 <= f_x2:
        result = "L"
    else:
        result = "R"

    table_data.append([itterations, ratio, a, b, x1, x2, f_x1, f_x2, result])
    
    if x1 <= x2:
        if f_x1 >= f_x2:
            a = x1
        else:
            b = x2

optimal_point = (a + b) / 2
optimal_eqn = f_expr.subs({x: optimal_point})
optimal_value = sp.simplify(optimal_eqn)
optimal_points = f"{optimal_point:.4e}"

# Print the table

import pandas as pd
# Convert to a DataFrame for better handling
df = pd.DataFrame(table_data, columns=["Iterations", "f(n-k)/f(n-k+1)", "a", "b", "x1", "x2", "f(x1)", "f(x2)", "L/R"])

# Format the numbers to 2 decimal places
df = df.round(2)

# Display the formatted table in the Streamlit app
st.write(df)

# Print the optimal point and value
st.write("The Optimal Point is :", optimal_point, "\nAnd The Optimal Value is: ", optimal_value)
