import numpy as np
import pandas as pd
from sympy import symbols, lambdify

# Define the function
def f(x1, x2):
    return 3*x1 + 23*x2 + 2*x1**2 + 4*x2**2

# Initial inputs
x0 = np.array([5, 5])
del1, del2 = 2, 2
Del = np.array([del1, del2])
normDel = np.linalg.norm(Del)
n = 9
ep = 0.3

# Symbolic variables
x1, x2 = symbols('x1 x2')

# Function lambdified for numerical computation
f_lambdified = lambdify((x1, x2), f(x1, x2))

# Iteration
rsl = []
for i in range(n):
    fx0 = f_lambdified(x0[0], x0[1])
    increment = Del / 2

    A = x0 + increment
    B = x0 - increment * np.array([1, -1])
    C = x0 - increment
    D = x0 + increment * np.array([1, -1])

    fA = f_lambdified(A[0], A[1])
    fB = f_lambdified(B[0], B[1])
    fC = f_lambdified(C[0], C[1])
    fD = f_lambdified(D[0], D[1])

    x_vector = [x0, A, B, C, D]
    f_vector = [fx0, fA, fB, fC, fD]

    fx, min_index = min((val, idx) for (idx, val) in enumerate(f_vector))
    xmin = x_vector[min_index]

    rsl.append([i, x0, A, B, C, D, fx0, fA, fB, fC, fD, xmin])
    x0 = xmin

    # If point not change
    if fx == fx0:
        Del = Del / 2
        normDel = np.linalg.norm(Del)

    # Terminal conditions
    if normDel <= ep:
        n = i
        break

# Convert results to DataFrame
columns = ['k', 'x0', 'A', 'B', 'C', 'D', 'fx0', 'fA', 'fB', 'fC', 'fD', 'xmin']
Resl = pd.DataFrame(rsl, columns=columns)

# Display results
print(Resl)
fopt = f_lambdified(x0[0], x0[1])
print(f'Optimal value of x = [{x0[0]:.6f}, {x0[1]:.6f}]')
print(f'Optimal value of f(x) = {fopt:.6f}')
