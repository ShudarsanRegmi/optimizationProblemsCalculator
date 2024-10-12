import math
import sympy as sp
import streamlit as st
import pandas as pd

# Function to evaluate polynomial at a given x
def evaluate_polynomial(expr, x_value):
    x = sp.symbols('x')
    return float(expr.subs(x, x_value))

# Function to perform interval halving and return table data
def graph_points(interval, expr, iterations):
    temp = interval
    table_data = []
    
    for it in range(1, iterations + 1):
        x0 = (temp[0] + temp[1]) / 2
        x1 = (temp[0] + x0) / 2
        x2 = (x0 + temp[1]) / 2

        y0 = evaluate_polynomial(expr, x0)
        y1 = evaluate_polynomial(expr, x1)
        y2 = evaluate_polynomial(expr, x2)

        table_data.append([it, x0, x1, x2, y0, y1, y2])

        if y2 > y0 and y0 > y1:
            temp[1] = x0
        elif y1 > y0 and y0 > y2:
            temp[0] = x0
        elif y1 > y0 and y2 > y0:
            temp = [x1, x2]

    return y0, temp, table_data

# Function to calculate n based on accuracy
def find_n(con):
    l1 = math.log(con) / math.log(0.5)
    l2 = l1 + 0.25
    x = l2 / 0.5
    return math.ceil(x)

# Function to determine number of iterations
def no_of_iterations(n):
    it = []
    if n % 2 == 0:
        for i in range(3, n):
            if i % 2 != 0:
                it.append(i)
    else:
        for i in range(3, n + 1):
            if i % 2 != 0:
                it.append(i)
    return len(it)

# Streamlit App
st.title("Interval Halving/Bisection Method")

# User input for the polynomial function
function_input = st.text_input("Enter the function (e.g., x**2 + 3*x + 2):", value="x**2 + 3*x + 2")
expr = sp.sympify(function_input)
x = sp.symbols('x')

# Displaying the polynomial
st.write(f"**The function: f(x) = {expr}**")

# Get intervals from user
st.write("### Define the interval for the method:")
col1, col2, col3 = st.columns(3)
initial_point = col1.number_input("Enter the initial point:", value=0.0)
final_point = col2.number_input("Enter the final point:", value=1.0)
# initial_point = st.number_input("Enter the initial point:", value=0.0)
# final_point = st.number_input("Enter the final point:", value=1.0)
interval = [initial_point, final_point]
L0 = interval[1] - interval[0]

# Accuracy and n calculations
per = col3.number_input("Enter the accuracy in percentage:", value=1.0, min_value=0.1)
con = per / 100
n = find_n(con)
iterations = no_of_iterations(n)

# Display input details
st.write(f"**Interval:** {interval}")
st.write(f"**Accuracy:** {per}%")
st.write(f"**Number of iterations:** {iterations}")

# Perform interval halving method
soln, reg, table_data = graph_points(interval, expr, iterations)

# Display the solution
st.write(f"\nThe solution for the given function is approximately: {soln} within the interval {reg}")

# Create a DataFrame for displaying the results in table form
df = pd.DataFrame(table_data, columns=["Iteration", "x0", "x1", "x2", "f(x0)", "f(x1)", "f(x2)"])

# Display the table
st.write("## Results Table:")
st.write(df)
