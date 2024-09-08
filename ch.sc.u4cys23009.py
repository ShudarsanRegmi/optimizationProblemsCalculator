import numpy as np

def simplex_method(obj_coeffs, constraints, rhs):
    """
    Solves the linear programming problem using the Simplex method:
    Maximize:     obj_coeffs^T * x
    Subject to:   constraints * x <= rhs, x >= 0
    
    Parameters:
    obj_coeffs (ndarray): Coefficients of the objective function.
    constraints (ndarray): Coefficients of the constraints.
    rhs (ndarray): Right-hand side of the constraints.
    
    Returns:
    tuple: The optimal solution vector and the maximum value of the objective function.
    """
    num_constraints = len(constraints)
    num_vars = len(obj_coeffs)

    # Create initial tableau
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))

    # Fill the tableau with constraints and identity matrix
    for i in range(num_constraints):
        for j in range(num_vars):
            tableau[i, j] = constraints[i][j]
        tableau[i, num_vars + i] = 1  # Slack variable
        tableau[i, -1] = rhs[i]  # Right-hand side

    # Fill the objective function row
    for j in range(num_vars):
        tableau[-1, j] = -obj_coeffs[j]

    while True:
        # Step 1: Find entering variable (most negative element in last row)
        col_pivot = np.argmin(tableau[-1, :-1])
        if tableau[-1, col_pivot] >= 0:
            # If no negative values, solution is optimal
            break

        # Step 2: Find leaving variable (smallest ratio of RHS to pivot column)
        row_pivot = -1
        min_ratio = np.inf
        for i in range(num_constraints):
            if tableau[i, col_pivot] > 0:
                ratio = tableau[i, -1] / tableau[i, col_pivot]
                if ratio < min_ratio:
                    min_ratio = ratio
                    row_pivot = i

        # If problem is unbounded
        if row_pivot == -1:
            raise ValueError("The problem is unbounded.")

        # Step 3: Perform pivot operation
        tableau[row_pivot, :] /= tableau[row_pivot, col_pivot]
        for i in range(num_constraints + 1):
            if i != row_pivot:
                tableau[i, :] -= tableau[i, col_pivot] * tableau[row_pivot, :]

    # Extract solution
    solution = np.zeros(num_vars)
    for i in range(num_vars):
        col = tableau[:-1, i]
        if np.sum(col == 1) == 1 and np.sum(col == 0) == num_constraints - 1:
            solution[i] = tableau[np.where(col == 1)[0][0], -1]

    # Return the solution and the maximum value of the objective function
    max_val = tableau[-1, -1]
    return solution, max_val

def get_input():
    # Input for the number of variables
    num_vars = int(input("Enter the number of variables: ").strip())

    # Input for the number of constraints
    num_constraints = int(input("Enter the number of constraints: ").strip())

    # Input for the coefficients of the objective function
    print("Enter the coefficients of the objective function (separated by spaces): ")
    obj_coeffs = np.array(list(map(float, input().split())))

    if len(obj_coeffs) != num_vars:
        raise ValueError("Number of objective function coefficients must match the number of variables.")

    # Input for the constraints
    constraints = []
    print("Enter the coefficients of the constraints (row by row, separated by spaces):")
    for i in range(num_constraints):
        row = list(map(float, input(f"Constraint {i+1}: ").split()))
        if len(row) != num_vars:
            raise ValueError("Number of constraint coefficients must match the number of variables.")
        constraints.append(row)

    constraints = np.array(constraints)

    # Input for the right-hand side
    print("Enter the right-hand side values (separated by spaces): ")
    rhs = np.array(list(map(float, input().split())))

    if len(rhs) != num_constraints:
        raise ValueError("Number of RHS values must match the number of constraints.")

    return obj_coeffs, constraints, rhs

def main():
    print("Welcome to the Simplex Solver!")
    
    try:
        # Get the user input for the Simplex problem
        obj_coeffs, constraints, rhs = get_input()
        
        # Run the Simplex method
        solution, max_value = simplex_method(obj_coeffs, constraints, rhs)
        
        # Print the results
        print("\nOptimal solution:", solution)
        print("Maximum value of the objective function:", max_value)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
