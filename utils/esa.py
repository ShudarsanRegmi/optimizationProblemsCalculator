import numpy as np
import sympy as sp
import pandas as pd

# Function to define the user input function with any number of variables
def get_function(var_list):
    expression = input("Enter the function in terms of " + ", ".join(var_list) + ": ")
    return sp.sympify(expression)

# Function to get user inputs for initial points and increments
def get_initial_values(var_list):
    initial_values = []
    increments = []
    for var in var_list:
        initial_values.append(float(input(f"Enter the initial value for {var}: ")))
        increments.append(float(input(f"Enter the increment for {var}: ")))
    return np.array(initial_values), np.array(increments)

# Function to calculate the function value at a given point
def calc_function_value(f, point, var_list):
    return float(f.subs({var: val for var, val in zip(var_list, point)}))

# User inputs
num_vars = int(input("Enter the number of variables: "))
var_list = [sp.symbols(f'x{i+1}') for i in range(num_vars)]
f = get_function([str(var) for var in var_list])
x0, Del = get_initial_values([str(var) for var in var_list])
ep = float(input("Enter the tolerance (epsilon): "))
max_iter = int(input("Enter the maximum number of iterations: "))

# Initialize
normDel = np.linalg.norm(Del)
rsl = []

# Iteration process
for i in range(max_iter):
    fx0 = calc_function_value(f, x0, var_list)
    increment = Del / 2
    neighbors = []
    
    # Generate neighbors by adjusting one variable at a time
    for j in range(num_vars):
        neighbors.append(np.array(x0))
        neighbors[j][j] += increment[j]
    
    # Evaluate the function at each neighbor point
    f_values = [fx0] + [calc_function_value(f, point, var_list) for point in neighbors]
    x_vector = [x0] + neighbors
    fx, min_index = min((val, idx) for (idx, val) in enumerate(f_values))
    xmin = x_vector[min_index]
    
    # Store the results
    rsl.append([i, x0] + neighbors + [fx0] + f_values[1:] + [xmin])
    x0 = xmin
    
    # Adjust increments if the point doesn't change
    if fx == fx0:
        Del = Del / 2
        normDel = np.linalg.norm(Del)
    
    # Terminal conditions
    if normDel <= ep:
        break

# Table display
columns = ['Iteration', 'x0'] + [f'Neighbor_{j+1}' for j in range(num_vars)] + ['fx0'] + [f'f(Neighbor_{j+1})' for j in range(num_vars)] + ['xmin']
Resl = pd.DataFrame(rsl, columns=columns)
print(Resl)

fopt = calc_function_value(f, x0, var_list)
print(f"Optimal value of x = {x0}")
print(f"Optimal value of f(x) = {fopt}")