import numpy as np

def print_tableau(tableau):
    print("Tableau:")
    for row in tableau:
        print("\t".join([f"{x:.2f}" for x in row]))
    print()

def simplex_method(c, A, b):
    num_vars = len(c)
    num_constraints = len(b)

    # Create the tableau
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    
    # Fill the tableau with the coefficients
    tableau[:num_constraints, :num_vars] = A
    tableau[:num_constraints, num_vars:num_vars + num_constraints] = np.eye(num_constraints)
    tableau[:num_constraints, -1] = b
    tableau[-1, :num_vars] = c
    tableau[-1, -1] = 0

    print("Initial Tableau:")
    print_tableau(tableau)
    
    iteration = 0
    while True:
        print(f"Iteration {iteration}:")
        print_tableau(tableau)

        # Check if the solution is optimal
        if all(x >= 0 for x in tableau[-1, :-1]):
            print("Optimal solution found!")
            break

        # Find the entering variable (pivot column)
        pivot_col = np.argmin(tableau[-1, :-1])
        print(f"Entering variable is column {pivot_col}")

        # Find the leaving variable (pivot row)
        ratios = []
        for i in range(num_constraints):
            if tableau[i, pivot_col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, pivot_col])
            else:
                ratios.append(np.inf)
        pivot_row = np.argmin(ratios)
        print(f"Leaving variable is row {pivot_row}")

        if ratios[pivot_row] == np.inf:
            print("Unbounded solution")
            return None

        # Perform the pivot operation
        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row] = tableau[pivot_row] / pivot_element
        for i in range(num_constraints + 1):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

        iteration += 1

    # Extract the solution
    solution = np.zeros(num_vars)
    for i in range(num_constraints):
        basic_var_index = np.where(tableau[i, :num_vars] == 1)[0]
        if len(basic_var_index) == 1:
            solution[basic_var_index[0]] = tableau[i, -1]

    print("Solution:")
    print(solution)
    return solution

# Example usage
c = [-3, -2]  # Coefficients for the objective function
A = [[2, 1], [1, 2]]  # Coefficients for the constraints
b = [20, 20]  # Right-hand side values for the constraints

simplex_method(c, A, b)


