import numpy as np
import sympy as sp
import pandas as pd

# Define the symbolic variables
a = int(input("Please enter the number of variable min 2 and max 4: "))
if a == 2:
    x1, x2 = sp.symbols('x1 x2')

    # Define the function
    f_expr = input("Enter the function containing x1 and x2 variables only: ")
    f = sp.lambdify((x1, x2), sp.sympify(f_expr), 'numpy')

    # Given values
    X1 = list(map(int, input("Enter the initial values of x1 and x2 separated by space: ").strip().split()))
    X1 = np.array(X1)
    delx1 = float(input("Enter the value of delta x1: "))
    delx2 = float(input("Enter the value of delta x2: "))
    ep = float(input("Enter the value of epsilon: "))

    # Hooke-Jeeves search algorithm
    rsl = []
    for i in range(20):
        # Explanatory move in x1 direction
        A = np.array([X1[0] - delx1, X1[1]])
        B = np.array([X1[0] + delx1, X1[1]])
        fminus = f(A[0], A[1])
        ff = f(X1[0], X1[1])
        fplus = f(B[0], B[1])
        x_vector = [A, X1, B]
        f_vector = [fminus, ff, fplus]
        min_index = np.argmin(f_vector)
        xmin = x_vector[min_index]

        # Explanatory move in x2 direction
        A = np.array([xmin[0], xmin[1] - delx2])
        B = np.array([xmin[0], xmin[1] + delx2])
        fminus = f(A[0], A[1])
        ff = f(xmin[0], xmin[1])
        fplus = f(B[0], B[1])
        x_vector = [A, xmin, B]
        f_vector = [fminus, ff, fplus]
        min_index = np.argmin(f_vector)
        xmin = x_vector[min_index]
        A = xmin

        # Pattern search
        if np.array_equal(X1, A):
            delx1 /= 2
            delx2 = delx1 / 2
            if delx1 <= ep:
                n = i
                print(f'The optimal solution is X2 =[{X1[0]};{X1[1]}]')
                break
        else:
            # Pattern move
            S = A - X1  # Calculate direction

            # To calculate lambda
            df_dx1 = sp.diff(f_expr, x1)
            df_dx2 = sp.diff(f_expr, x2)
            d2f_dx1x1 = sp.diff(df_dx1, x1)
            d2f_dx2x2 = sp.diff(df_dx2, x2)
            d2f_dx1x2 = sp.diff(df_dx1, x2)
            d2f_dx2x1 = sp.diff(df_dx2, x1)
            H = sp.Matrix([[d2f_dx1x1, d2f_dx1x2], [d2f_dx2x1, d2f_dx2x2]])
            delf = sp.Matrix([df_dx1, df_dx2])
            delfA = delf.subs([(x1, A[0]), (x2, A[1])])
            S_mat = sp.Matrix(S)
            lambda_val = -delfA.dot(S_mat) / (S_mat.dot(H * S_mat))

            # New point
            X2 = np.array(A + lambda_val * S, dtype=float)
            rsl.append([i, X1.copy(), A.copy(), S, float(lambda_val), X2.copy()])

            # Check optimality
            delfX2 = delf.subs([(x1, X2[0]), (x2, X2[1])])
            if delfX2[0] == 0 and delfX2[1] == 0:
                n = i
                print(f'The optimal solution is X2 =[{X2[0]};{X2[1]}]')
                break
            else:
                X1 = X2

    # Create a result table
    Variables = ['k', 'Initial value', 'Explanatory move', 'Direction S', 'lambda', 'Pattern move']
    Resl = pd.DataFrame(rsl, columns=Variables)
    print(Resl)

    # Optimal value
    fopt = f(X2[0], X2[1])
    print(f'Optimal value of x=[{X2[0]}; {X2[1]}]')
    print(f'Optimal value of f(x)={fopt}')
