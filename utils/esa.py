import numpy as np
import pandas as pd
from sympy import symbols, lambdify, sympify

def main():
    # Get user inputs
    function_input = input("Enter the function f(x1, x2): ")
    x0_input = input("Enter the initial values for x0 (comma-separated, e.g., 5,5): ")
    x0 = np.array([float(x) for x in x0_input.split(',')])

    del1 = float(input("Enter the value for del1: "))
    del2 = float(input("Enter the value for del2: "))
    Del = np.array([del1, del2])

    n = int(input("Enter the number of iterations (n): "))
    ep = float(input("Enter the terminal condition (epsilon): "))

    # Calculate the norm of Del
    normDel = np.linalg.norm(Del)

    # Symbolic variables
    x1, x2 = symbols('x1 x2')

    # Parse the function input
    f_sympy = sympify(function_input)
    f_lambdified = lambdify((x1, x2), f_sympy)

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

if __name__ == "__main__":
    main()
