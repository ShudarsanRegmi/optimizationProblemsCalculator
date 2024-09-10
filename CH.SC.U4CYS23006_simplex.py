from scipy.optimize import linprog

def simplex_method():
    print("Simplex Method Optimization")

    # Taking input for the objective function
    num_vars = int(input("Enter the number of variables in the objective function: "))
    print("Enter the coefficients of the objective function (separated by spaces):")
    obj_coeffs = list(map(float, input().split()))
    
    # Check if it's maximization or minimization
    opt_type = input("Enter 'max' for maximization or 'min' for minimization: ").lower()

    if opt_type == 'max':
        obj_coeffs = [-c for c in obj_coeffs]  # Negate coefficients for maximization

    # Taking input for the constraints
    num_constraints = int(input("Enter the number of constraints: "))
    lhs_constraints = []
    rhs_constraints = []
    
    for i in range(num_constraints):
        print(f"Enter the coefficients for constraint {i+1} (separated by spaces):")
        lhs = list(map(float, input().split()))
        lhs_constraints.append(lhs)
        
        rhs = float(input(f"Enter the right-hand side value for constraint {i+1}: "))
        rhs_constraints.append(rhs)
    
    # Set the bounds for variables (default: x >= 0)
    bounds = [(0, None) for _ in range(num_vars)]
    
    # Solve the linear programming problem
    result = linprog(c=obj_coeffs, A_ub=lhs_constraints, b_ub=rhs_constraints, bounds=bounds, method='simplex')

    if result.success:
        print("\nOptimal solution found!")
        print(f"Optimal value: {-result.fun if opt_type == 'max' else result.fun}")
        print(f"Variable values: {result.x}")
    else:
        print("No optimal solution found.")

if __name__ == "__main__":
    simplex_method()
