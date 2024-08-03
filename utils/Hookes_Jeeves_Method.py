import numpy as np
import sympy as sp
import pandas as pd

# Define the symbolic variables dynamically
a = int(input("Please enter the number of variables: "))
variables = sp.symbols(' '.join([f'x{i+1}' for i in range(a)]))

# Define the function
f_expr = input(f"Enter the function containing {a} variables in the form x1, x2, ...: ")
f_sym = sp.sympify(f_expr)
f = sp.lambdify(variables, f_sym, 'numpy')

# Given values
X1 = list(map(int, input(f"Enter the initial values of {', '.join([str(var) for var in variables])} separated by spaces: ").strip().split()))
X1 = np.array(X1)
deltas = [float(input(f"Enter the value of delta x{i+1}: ")) for i in range(a)]
ep = float(input("Enter the value of epsilon: "))

# Hooke-Jeeves Search algorithm
rsl = []
X2 = X1.copy()  # Initialize X2 to avoid NameError
for i in range(20):
    xmin = X1.copy()

    for j in range(a):
        # Exploratory move in xj direction
        A = xmin.copy()
        B = xmin.copy()
        A[j] -= deltas[j]
        B[j] += deltas[j]
        fminus = f(*A)
        ff = f(*xmin)
        fplus = f(*B)
        x_vector = [A, xmin, B]
        f_vector = [fminus, ff, fplus]
        min_index = np.argmin(f_vector)
        xmin = x_vector[min_index]

    # Pattern Search
    if np.array_equal(X1, xmin):
        deltas = [delta / 2 for delta in deltas]
        if all(delta <= ep for delta in deltas):
            print(f'The optimal solution is X1 = [{"; ".join(map(str, X1))}]')
            break
    else:
        # Pattern Move
        S = xmin - X1

        # To calculate lambda
        delf = sp.Matrix([sp.diff(f_sym, var) for var in variables])
        H = sp.hessian(f_sym, variables)
        delfA = delf.subs([(variables[k], xmin[k]) for k in range(a)])
        S_mat = sp.Matrix(S)
        lambda_val = -delfA.dot(S_mat) / (S_mat.dot(H * S_mat))

        # New Point
        X2 = np.array(xmin + lambda_val * S, dtype=float)
        rsl.append([i, X1.copy(), xmin.copy(), S, float(lambda_val), X2.copy()])

        # Check optimality
        delfX2 = delf.subs([(variables[k], X2[k]) for k in range(a)])
        if all(d == 0 for d in delfX2):
            print(f'The optimal solution is X2 = [{"; ".join(map(str, X2))}]')
            break
        else:
            X1 = X2

# Create a result table
Variables = ['k', 'Initial value', 'Explanatory move', 'Direction S', 'lambda', 'Pattern move']
Resl = pd.DataFrame(rsl, columns=Variables)
print(Resl)

# Optimal value
fopt = f(*X2)
print(f'Optimal value of x = [{"; ".join(map(str, X2))}]')
print(f'Optimal value of f(x) = {fopt}')
