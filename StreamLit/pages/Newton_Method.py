import streamlit as st
from sympy import symbols, diff, sympify, SympifyError
import pandas as pd

# Function to compute the derivative values
def derivative_values(x_value, derivative_f, derivative2_f, x):
    f_prime = derivative_f.evalf(subs={x: x_value})
    f_double_prime = derivative2_f.evalf(subs={x: x_value})
    return f_prime, f_double_prime

# Function to compute the value of f(x)
def f_value(x_value, f_x, x):
    return f_x.evalf(subs={x: x_value})

# Streamlit application starts here
st.title("Newton's Method for Minimization")

# Input fields for the user
f_x_input = st.text_input("Enter the function (e.g., x**2 + 3*x + 2):", "x**2 + 3*x + 2")
y = st.number_input("Enter the value of x0:", value=0.0)
x_symbol = st.text_input("Enter the symbol for the function:", "x")
epsilon = st.number_input("Enter the value of epsilon:", value=0.001)

# Initialize the symbol for the variable in the function
x = symbols(x_symbol)

# Parse the input function
try:
    f_x = sympify(f_x_input)
except SympifyError:
    st.error("Invalid function. Please enter a valid function.")
    st.stop()

# Find the first and second derivatives
derivative_f = diff(f_x, x)
derivative2_f = diff(derivative_f, x)

# Initialize variables
last = y + 2 * epsilon  # Ensure the loop starts
last2 = y
iteration = 1  # Initializing iteration

# Create an empty list to store iteration data for the table
data = []

# Newton's method loop
while abs(last2 - last) > epsilon:
    last = last2
    f_prime, f_double_prime = derivative_values(last2, derivative_f, derivative2_f, x)

    if f_double_prime == 0:  # Prevent division by zero
        st.error(f"Division by zero error at iteration {iteration}")
        break

    last2 = last2 - (f_prime / f_double_prime)

    # Store iteration data for the table
    data.append([iteration, round(last2, 14), round(abs(last2 - last), 14)])

    iteration += 1

# Convert the iteration data into a pandas DataFrame for table display
df = pd.DataFrame(data, columns=['Iteration', 'x_n', 'x_n+1 - x_n'])

# Display the result table in Streamlit
st.write("## Iteration Results:")
st.write(df)

# Output the least value and the optimal value of the function
st.write(f"### Least value (x): {round(last2, 14)}")
st.write(f"### Optimal Value of function (f(x)): {round(f_value(last2, f_x, x), 14)}")


# from sympy import symbols, diff, sympify, SympifyError
# from prettytable import PrettyTable

# def get_input(prompt, cast_func):
#     while True:
#         try:
#             return cast_func(input(prompt))
#         except ValueError:
#             print("Invalid input. Please try again.")

# # Input function, value of x0, symbol, and epsilon
# f_x_input = input("Enter the function (must be quadratic or greater degree, e.g., x**2 + 3*x + 2): ")
# y = get_input("Enter the value of x0: ", float)
# x_symbol = input("Enter the symbol for the function: ")
# epsilon = get_input("Enter the value of epsilon: ", float)

# # Define the symbol
# x = symbols(x_symbol)

# # Parse the input function
# try:
#     f_x = sympify(f_x_input)
# except SympifyError:
#     print("Invalid function. Please enter a valid function.")
#     exit(1)

# # Define table
# table = PrettyTable()
# table.field_names = ['No. of iteration', 'x_n', "x_n+1 - x_n"]

# # Find the first and second derivatives
# derivative_f = diff(f_x, x)
# derivative2_f = diff(derivative_f, x)

# # Initialize variables
# last = y + 2 * epsilon  # Ensure the loop starts
# last2 = y

# def derivative_values(x_value):
#     f_prime = derivative_f.evalf(subs={x: x_value})
#     f_double_prime = derivative2_f.evalf(subs={x: x_value})
#     return f_prime, f_double_prime

# def f_value(x_value):
#     return f_x.evalf(subs={x: x_value})

# iteration = 1  # Initializing iteration

# # Newton's method loop
# while abs(last2 - last) > epsilon:
#     last = last2
#     f_prime, f_double_prime = derivative_values(last2)

#     if f_double_prime == 0:  # Prevent division by zero
#         print(f"Division by zero error at iteration {iteration}")
#         break

#     last2 = last2 - (f_prime / f_double_prime)
#     table_row = [iteration, round(last2, 14), round(abs(last2 - last), 14)]
#     table.add_row(table_row)
#     iteration += 1

# # Printing table
# print(table)

# # Output the results
# print("Least value (x):", round(last2, 14))
# print("Optimal Value of function (f(x)):", round(f_value(last2), 14))
