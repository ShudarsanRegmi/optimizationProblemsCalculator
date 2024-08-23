

import sympy as sp
import numpy as np

# Given parameters
x1, x2 = sp.symbols('x1 x2')
f = x1**2 - x1*x2 + 3*x2**2
X = [np.array([1, 2])]

# Gradient calculations
df_dx1 = sp.diff(f, x1)
df_dx2 = sp.diff(f, x2)
grad_f = sp.Matrix([df_dx1, df_dx2])

# Hessian calculations
df_dx1_x1 = sp.diff(df_dx1, x1)
df_dx1_x2 = sp.diff(df_dx1, x2)
df_dx2_x2 = sp.diff(df_dx2, x2)
df_dx2_x1 = sp.diff(df_dx2, x1)
H = sp.Matrix([[df_dx1_x1, df_dx1_x2], [df_dx2_x1, df_dx2_x2]])
H = np.array(H).astype(np.float64)

# Conjugate Gradient Method iterations
for i in range(5):
    if i == 0:
        grad_f_x = np.array(grad_f.subs([(x1, X[i][0]), (x2, X[i][1])]), dtype=np.float64).flatten()
        S = -grad_f_x  # Initialize S as a numpy array
    else:
        grad_f_x = np.array(grad_f.subs([(x1, X[i][0]), (x2, X[i][1])]), dtype=np.float64).flatten()
        beeta = (grad_f_x.T @ grad_f_x) / (prev_grad_f_x.T @ prev_grad_f_x)
        S = -grad_f_x + beeta * prev_S  # Update S as a numpy array
    
    lambda_ = (grad_f_x.T @ grad_f_x) / (S.T @ H @ S)
    X.append(X[i] + lambda_ * S)
    
    # Check for convergence
    grad_f_x_next = np.array(grad_f.subs([(x1, X[i+1][0]), (x2, X[i+1][1])]), dtype=np.float64).flatten()
    if np.allclose(grad_f_x_next, np.zeros(2)):
        print(f"The final iteration number is {i+1}")
        xopt = X[i+1]
        break
    
    prev_grad_f_x = grad_f_x
    prev_S = S

print(f"The optimal solution is {xopt}")
print(f"The function value is {f.subs([(x1, xopt[0]), (x2, xopt[1])])}")

