import numpy as np
import sympy as sp
import streamlit as st

# Streamlit App Title
st.title("Optimization using Gradient Descent with Hessian")

# Input for the number of variables
a = st.number_input("Please enter the number of variables:", min_value=1, value=2, step=1)

# Define the symbolic variables dynamically
variables = sp.symbols(' '.join([f'x{i + 1}' for i in range(a)]))

# Input for the function expression
f_expr = st.text_input(f"Enter the function containing {', '.join([str(var) for var in variables])} in the form x1, x2, ...:", "x1**2 + x2**2")
f_sym = sp.sympify(f_expr)
f = sp.lambdify(variables, f_sym, 'numpy')

# Input for the initial values of the variables
initial_values = st.text_input(f"Enter the initial values of {', '.join([str(var) for var in variables])} separated by spaces:", "1 1")
X1 = np.array(list(map(float, initial_values.strip().split())))

# Input for epsilon value
ep = st.number_input("Enter the value of epsilon:", min_value=0.0001, value=0.001, step=0.0001)

# Calculate gradients and Hessian matrix
grad = [sp.diff(f_sym, var) for var in variables]
H = sp.hessian(f_sym, variables)

# Function to check if all gradient values are less than epsilon
def is_optimal(grad, X, epsilon):
    grad_values = np.array([float(g.evalf(subs=dict(zip(variables, X)))) for g in grad])
    return np.all(np.abs(grad_values) < epsilon)

# Function to calculate lambda
def calc_lambda(S, H):
    S = np.array(S, dtype=float)
    H = np.array(H, dtype=float)
    a = np.dot(S.T, S)  # Matrix multiplication: S^T * S
    b = np.dot(np.dot(S.T, H), S)  # Matrix multiplication: S^T * H * S
    return a / b if b != 0 else 0  # Avoid division by zero

# Function to calculate the function value at a given point
def func_value(X):
    return f(*X)

# Main logic: Gradient descent iterations
if st.button("Start Optimization"):
    iteration = 1
    X1_new = X1.copy()
    iteration_data = []  # List to store iteration details for display

    while True:
        # Calculate the gradient values at the current X1
        grad_values = np.array([float(g.evalf(subs=dict(zip(variables, X1)))) for g in grad])
        S = -grad_values  # Direction vector (negative gradient)

        # Calculate Hessian at the current point
        H_func = sp.lambdify(variables, H, 'numpy')
        H_values = H_func(*X1)

        # Calculate lambda
        lambda_1 = calc_lambda(S, H_values)

        # Update the values of X
        X1_new = X1 + lambda_1 * S

        # Store iteration data for displaying
        iteration_data.append({
            "Iteration": iteration,
            "X Values": X1.copy(),
            "Lambda": lambda_1,
            "Gradient": grad_values.copy(),
            "New X Values": X1_new.copy()
        })

        # Display current iteration results
        st.write(f"### Iteration {iteration}:")
        st.write(f"X = {', '.join(f'{x:.6f}' for x in X1)}")
        st.write(f"Lambda = {lambda_1:.6f}")
        st.write(f"Gradient = {', '.join(f'{g:.6f}' for g in grad_values)}")

        iteration += 1

        # Check for optimality
        if is_optimal(grad, X1_new, ep):
            st.success("Optimization Complete.")
            break

        # Update X1 for the next iteration
        X1 = X1_new.copy()

    # Print final results
    min_value = func_value(X1)
    st.write("### Final Results:")
    st.write(f"Minimal Point: {', '.join(f'{x:.6f}' for x in X1)}")
    st.write(f"Function Value at Minimal Point: {min_value:.6f}")

# import numpy as np
# import sympy as sp

# # Define the symbolic variables dynamically
# a = int(input("Please enter the number of variables: "))
# variables = sp.symbols(' '.join([f'x{i + 1}' for i in range(a)]))

# # Define the function
# f_expr = input(f"Enter the function containing {', '.join([str(var) for var in variables])} in the form x1, x2, ...: ")
# f_sym = sp.sympify(f_expr)
# f = sp.lambdify(variables, f_sym, 'numpy')

# # Given values
# X1 = np.array(list(map(float, input(
#     f"Enter the initial values of {', '.join([str(var) for var in variables])} separated by spaces: ").strip().split())))
# ep = float(input("Enter the value of epsilon: "))

# # Calculate gradients and Hessian matrix
# grad = [sp.diff(f_sym, var) for var in variables]
# H = sp.hessian(f_sym, variables)

# # Function to compare the Delta difference with epsilon
# def all_values_not_less_than(values, threshold=ep):
#     return all(abs(value) >= threshold for value in values)

# # Function to calculate lambda
# def calc_lambda(S, H):
#     S = np.array(S)
#     H = np.array(H)
#     a = np.dot(S.T, S)  # Matrix multiplication: S^T * S
#     b = np.dot(np.dot(S.T, H), S)  # Matrix multiplication: S^T * H * S
#     return a / b if b != 0 else 0  # Avoid division by zero

# # Function to check optimality
# def is_optimal(grad, X, ep):
#     grad_values = np.array([g.evalf(subs=dict(zip(variables, X))) for g in grad])
#     return np.all(np.abs(grad_values) < ep)

# # Function to calculate function value at a point
# def func_value(X):
#     return f(*X)

# # Main Logic
# iteration = 1
# while True:
#     # Calculate direction vector
#     grad_values = np.array([g.evalf(subs=dict(zip(variables, X1))) for g in grad])
#     S = -grad_values

#     # Calculate Hessian with current X1 values
#     H_func = sp.lambdify(variables, H, 'numpy')
#     H_values = H_func(*X1)

#     # Calculate lambda
#     lambda_1 = calc_lambda(S, H_values)

#     # Update X1
#     X1_new = X1 + lambda_1 * S

#     print(f"Iteration {iteration}: X = {', '.join(f'{x:.3f}' for x in X1)}, Lambda = {lambda_1:.3f}")
#     iteration += 1

#     # Check for optimality
#     if is_optimal(grad, X1_new, ep):
#         break

#     # Update X1 for the next iteration
#     X1 = X1_new

# # Print final results
# min_value = func_value(X1)
# print(f"Optimization complete.\nMinimal Point: {', '.join(f'{x:.3f}' for x in X1)}")
# print(f"Function Value at Minimal Point: {min_value:.3f}")
