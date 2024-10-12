import streamlit as st
import sympy as sp

# Define the symbols
x, y, z, t = sp.symbols('x y z t')

# Get initial points and directions from the user
st.write("# Function Optimization in Multiple Dimensions")

# Initial points and directions inputs
a1, a2, a3 = map(float, st.text_input("Enter the value of initial point (comma-separated):", "1, 2, 3").strip().split(','))
l1, l2, l3 = map(float, st.text_input("Enter the value of direction (comma-separated):", "0.5, -0.5, 1").strip().split(','))

# Input function from the user
f_expr_input = st.text_input("Enter the function containing x, y, z variables only (e.g., x**2 + y**2 + z**2):", "x**2 + y**2 + z**2")
try:
    f_expr = sp.sympify(f_expr_input)
except sp.SympifyError:
    st.error("Invalid function input. Please enter a valid function.")
    st.stop()

# Parameterizations for x, y, z
x_param = a1 + l1 * t
y_param = a2 + l2 * t
z_param = a3 + l3 * t

# Substitute x, y, z in f(x, y, z) with their parameterized forms
f_t_expr = f_expr.subs({x: x_param, y: y_param, z: z_param})

# Simplify the resulting expression
f_t_expr_simplified = sp.simplify(f_t_expr)
st.write(f"### f(t) = {f_t_expr_simplified}")

# Find the first derivative
first_derivative_f = sp.diff(f_t_expr_simplified, t)
st.write(f"### f'(t) = {first_derivative_f}")

# Solve f'(t) = 0 for t
t_values = sp.solve(first_derivative_f, t)
st.write(f"### Values of t where f'(t) = 0: {t_values}")

# Find the second derivative
second_derivative_f = sp.diff(f_t_expr_simplified, t, 2)
st.write(f"### f''(t) = {second_derivative_f}")

# Evaluate the second derivative at the values of t found
second_derivative_values = [second_derivative_f.subs(t, val) for val in t_values]
st.write(f"### Values of f''(t) at the points where f'(t) = 0: {second_derivative_values}")

# Determine maxima or minima and display results
for i, t_val in enumerate(t_values):
    x_val = x_param.subs(t, t_val)
    y_val = y_param.subs(t, t_val)
    z_val = z_param.subs(t, t_val)
    second_derivative_val = second_derivative_values[i]

    if second_derivative_val < 0:
        st.write(f"#### For t = {t_val}:")
        st.write(f"The value of f''(t) < 0, so it confirms a maximum.")
        max_value = f_expr.subs({x: x_val, y: y_val, z: z_val})
        st.write(f"Max point (x, y, z) = ({x_val}, {y_val}, {z_val}) and maximum value of function f(x, y, z) = {max_value}")
    elif second_derivative_val > 0:
        st.write(f"#### For t = {t_val}:")
        st.write(f"The value of f''(t) > 0, so it confirms a minimum.")
        min_value = f_expr.subs({x: x_val, y: y_val, z: z_val})
        st.write(f"Min point (x, y, z) = ({x_val}, {y_val}, {z_val}) and minimum value of function f(x, y, z) = {min_value}")
    else:
        st.write(f"#### For t = {t_val}:")
        st.write(f"The value of f''(t) = 0, which requires further investigation.")
  