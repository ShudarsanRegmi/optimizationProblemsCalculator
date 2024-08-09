import numpy as np
import sympy as sp

# Define the symbolic variables dynamically
a = int(input("Please enter the number of variables: "))
variables = sp.symbols(' '.join([f'x{i + 1}' for i in range(a)]))

# Define the function
f_expr = input(f"Enter the function containing {', '.join([str(var) for var in variables])} in the form x1, x2, ...: ")
f_sym = sp.sympify(f_expr)
f = sp.lambdify(variables, f_sym, 'numpy')

# Given values
X1 = np.array(list(map(float, input(
    f"Enter the initial values of {', '.join([str(var) for var in variables])} separated by spaces: ").strip().split())))
ep = float(input("Enter the value of epsilon: "))

# Calculate gradients and Hessian matrix
grad = [sp.diff(f_sym, var) for var in variables]
H = sp.hessian(f_sym, variables)

# Function to compare the Delta difference with epsilon
def all_values_not_less_than(values, threshold=ep):
    return all(abs(value) >= threshold for value in values)

# Function to calculate lambda
def calc_lambda(S, H):
    S = np.array(S)
    H = np.array(H)
    a = np.dot(S.T, S)  # Matrix multiplication: S^T * S
    b = np.dot(np.dot(S.T, H), S)  # Matrix multiplication: S^T * H * S
    return a / b if b != 0 else 0  # Avoid division by zero

# Function to check optimality
def is_optimal(grad, X, ep):
    grad_values = np.array([g.evalf(subs=dict(zip(variables, X))) for g in grad])
    return np.all(np.abs(grad_values) < ep)

# Function to calculate function value at a point
def func_value(X):
    return f(*X)

# Main Logic
iteration = 1
while True:
    # Calculate direction vector
    grad_values = np.array([g.evalf(subs=dict(zip(variables, X1))) for g in grad])
    S = -grad_values

    # Calculate Hessian with current X1 values
    H_func = sp.lambdify(variables, H, 'numpy')
    H_values = H_func(*X1)

    # Calculate lambda
    lambda_1 = calc_lambda(S, H_values)

    # Update X1
    X1_new = X1 + lambda_1 * S

    print(f"Iteration {iteration}: X = {', '.join(f'{x:.3f}' for x in X1)}, Lambda = {lambda_1:.3f}")
    iteration += 1

    # Check for optimality
    if is_optimal(grad, X1_new, ep):
        break

    # Update X1 for the next iteration
    X1 = X1_new

# Print final results
min_value = func_value(X1)
print(f"Optimization complete.\nMinimal Point: {', '.join(f'{x:.3f}' for x in X1)}")
print(f"Function Value at Minimal Point: {min_value:.3f}")
