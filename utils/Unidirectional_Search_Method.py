import sympy as sp

# Define the symbols
x, y, z, t = sp.symbols('x y z t')

# Get initial points and directions
a1, a2, a3 = map(float, input("Enter the value of initial point (comma-separated): ").strip().split(','))
l1, l2, l3 = map(float, input("Enter the value of direction (comma-separated): ").strip().split(','))

# Input function from user
f_expr_input = input("Enter the function containing x, y, z variables only: ")
f_expr = sp.sympify(f_expr_input)

# Parameterizations for x, y, z
x_param = a1 + l1 * t
y_param = a2 + l2 * t
z_param = a3 + l3 * t

# Substitute x, y, z in f(x, y, z) with their parameterized forms
f_t_expr = f_expr.subs({x: x_param, y: y_param, z: z_param})

# Simplify the resulting expression
f_t_expr_simplified = sp.simplify(f_t_expr)

# Display the result
print(f"f(t) = {f_t_expr_simplified}")

# Find the first derivative
first_derivative_f = sp.diff(f_t_expr_simplified, t)
print(f"f'(t) = {first_derivative_f}")

# Solve f'(t) = 0 for t
t_values = sp.solve(first_derivative_f, t)
print(f"Values of t where f'(t) = 0: {t_values}")

# Find the second derivative
second_derivative_f = sp.diff(f_t_expr_simplified, t, 2)
print(f"f''(t) = {second_derivative_f}")

# Evaluate the second derivative at the values of t found
second_derivative_values = [second_derivative_f.subs(t, val) for val in t_values]
print(f"Values of f''(t) at the points where f'(t) = 0: {second_derivative_values}")

# Determine maxima or minima
for i, t_val in enumerate(t_values):
    x_val = x_param.subs(t, t_val)
    y_val = y_param.subs(t, t_val)
    z_val = z_param.subs(t, t_val)
    second_derivative_val = second_derivative_values[i]

    if second_derivative_val < 0:
        print(f"The value of f''(t) < 0 at t = {t_val}, so it confirms a maximum.")
        max_value = f_expr.subs({x: x_val, y: y_val, z: z_val})
        print(f"Max point (x, y, z) = ({x_val}, {y_val}, {z_val}) and maximum value of function f(x, y, z) = {max_value}")
    elif second_derivative_val > 0:
        print(f"The value of f''(t) > 0 at t = {t_val}, so it confirms a minimum.")
        min_value = f_expr.subs({x: x_val, y: y_val, z: z_val})
        print(f"Min point (x, y, z) = ({x_val}, {y_val}, {z_val}) and minimum value of function f(x, y, z) = {min_value}")
    else:
        print(f"The value of f''(t) = 0 at t = {t_val}, which requires further investigation.")
