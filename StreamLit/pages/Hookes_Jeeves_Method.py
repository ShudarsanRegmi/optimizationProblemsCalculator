import streamlit as st
import numpy as np
import sympy as sp
import pandas as pd

st.write("# Hooke-Jeeves Method")

# Input number of variables
a = st.number_input("Please enter the number of variables", min_value=1, step=1, value=2)

# Dynamic input for function and variables
variables = sp.symbols(' '.join([f'x{i+1}' for i in range(a)]))
f_expr = st.text_input(f"Enter the function containing {a} variables (use x1, x2, ... format):", "x1**2 + x2**2")

if f_expr:
    try:
        f_sym = sp.sympify(f_expr)
        f = sp.lambdify(variables, f_sym, 'numpy')
    except Exception as e:
        st.error(f"Error in parsing function: {e}")
        st.stop()

# Input initial values and deltas
delta_columns = st.columns(a)
deltas_input = []
for i, col in enumerate(delta_columns):
    deltas_input.append(col.number_input(f"Delta for x{i + 1}", min_value=0.0, value=0.5, key=f"delta_{i}"))

# Single row with two columns: one for initial point input and one for epsilon
col_initial, col_epsilon = st.columns(2)
initial_values_input = col_initial.text_input(f"Enter the initial values of {', '.join([str(var) for var in variables])} (space-separated):", "0 1")
if initial_values_input:
    X1 = np.array(list(map(float, initial_values_input.split())))

ep = col_epsilon.number_input("Enter the value of epsilon", min_value=0.0, value=0.01)

# Hooke-Jeeves Search Algorithm
rsl = []
X2 = X1.copy()  # Initialize X2

for i in range(20):
    xmin = X1.copy()

    for j in range(a):
        # Exploratory move
        A = xmin.copy()
        B = xmin.copy()
        A[j] -= deltas_input[j]
        B[j] += deltas_input[j]
        fminus = f(*A)
        ff = f(*xmin)
        fplus = f(*B)
        x_vector = [A, xmin, B]
        f_vector = [fminus, ff, fplus]
        min_index = np.argmin(f_vector)
        xmin = x_vector[min_index]

    # Pattern Search
    if np.array_equal(X1, xmin):
        deltas_input = [delta / 2 for delta in deltas_input]
        if all(delta <= ep for delta in deltas_input):
            st.success(f'The optimal solution is X1 = [{"; ".join(map(str, X1))}]')
            break
    else:
        S = xmin - X1

        # Lambda calculation
        delf = sp.Matrix([sp.diff(f_sym, var) for var in variables])
        H = sp.hessian(f_sym, variables)
        delfA = delf.subs([(variables[k], xmin[k]) for k in range(a)])
        S_mat = sp.Matrix(S)
        lambda_val = -delfA.dot(S_mat) / (S_mat.dot(H * S_mat))

        # New point
        X2 = np.array(xmin + lambda_val * S, dtype=float)
        rsl.append([i, X1.copy(), xmin.copy(), S, float(lambda_val), X2.copy()])

        # Check optimality
        delfX2 = delf.subs([(variables[k], X2[k]) for k in range(a)])
        if all(d == 0 for d in delfX2):
            st.success(f'The optimal solution is X2 = [{"; ".join(map(str, X2))}]')
            break
        else:
            X1 = X2

# Display result in a table
if rsl:
    columns = ['Iteration', 'Initial Value', 'Exploratory Move', 'Direction S', 'Lambda', 'Pattern Move']
    df = pd.DataFrame(rsl, columns=columns)
    st.write(df)

# Show optimal value
if len(rsl) > 0:
    fopt = f(*X2)
    st.write(f"Optimal value of x = [{' '.join(map(str, X2))}]")
    st.write(f"Optimal value of f(x) = {fopt}")
