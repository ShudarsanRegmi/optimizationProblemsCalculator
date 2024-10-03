from scipy.optimize import linprog

# Function to get user inputs dynamically
def get_user_inputs():
    # Get number of variables from the user
    num_variables = int(input("Enter the number of decision variables: "))

    # Get the coefficients of the objective function
    print(f"Enter the coefficients of the objective function (maximize Z = c1*x1 + c2*x2 + ...):")
    c = []
    for i in range(num_variables):
        coef = float(input(f"Coefficient c{i+1}: "))
        c.append(-coef)  # Negate because linprog does minimization by default

    # Get number of constraints
    num_constraints = int(input("Enter the number of constraints: "))

    # Get the coefficients of each constraint
    A = []
    b = []
    print("Enter the coefficients for each constraint (format: a1*x1 + a2*x2 + ... <= b):")
    for i in range(num_constraints):
        constraint = []
        print(f"Constraint {i+1}:")
        for j in range(num_variables):
            coef = float(input(f"Coefficient a{j+1} for x{j+1}: "))
            constraint.append(coef)
        A.append(constraint)
        rhs = float(input(f"Right-hand side value b for Constraint {i+1}: "))
        b.append(rhs)

    # Get variable bounds (optional)
    bounds = []
    for i in range(num_variables):
        lower_bound = float(input(f"Enter the lower bound for x{i+1} (default 0): ") or 0)
        upper_bound = input(f"Enter the upper bound for x{i+1} (default None for no upper bound): ")
        upper_bound = None if upper_bound == '' else float(upper_bound)
        bounds.append((lower_bound, upper_bound))

    return c, A, b, bounds

# Function to solve the linear programming problem using the Simplex Method
def solve_simplex():
    try:
        # Get the input data from the user
        c, A, b, bounds = get_user_inputs()

        # Solving the linear programming problem using the Simplex Method
        result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

        # Display the results
        if result.success:
            print("\nOptimal solution found:")
            for i, x_val in enumerate(result.x, start=1):
                print(f"x{i} = {x_val}")
            print(f"Maximum value of the objective function (Z): {-result.fun}")
        else:
            print("No solution found.")
    except ValueError as e:
        print(f"Error: Invalid input. {e}")
    except linprog.LinprogError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Welcome to the Simplex Method Solver!\n")
    solve_simplex()
