import numpy as np

def dual_simplex(c, A, b, inequalities, problem_type):
    m, n = A.shape

    # Create the tableau
    tableau = np.hstack((A, np.eye(m), b.reshape(-1, 1)))
    tableau = np.vstack((tableau, np.hstack((c, np.zeros(m + 1)))))

    # Handle inequalities (convert to <= by multiplying with -1)
    for i in range(m):
        if inequalities[i] == '>=':
            tableau[i, :] *= -1

    # Adjust the objective function for minimization problems
    if problem_type == 'min':
        tableau[-1, :-1] *= -1

    # Start the Dual Simplex iterations
    while np.any(tableau[:-1, -1] < 0):  # Check for negative elements in b (indicating non-feasibility)
        pivot_row = np.argmin(tableau[:-1, -1])  # Choose the most negative b as pivot row
        ratios = tableau[-1, :-1] / tableau[pivot_row, :-1]  # Calculate ratios for pivot column selection
        pivot_col = np.where(ratios > 0, ratios, np.inf).argmin()  # Select pivot column

        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element  # Normalize the pivot row

        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]  # Eliminate other entries in the pivot column

    # Extract the solution
    solution = np.zeros(n)
    for i in range(n):
        col = tableau[:, i]
        if np.count_nonzero(col[:-1]) == 1 and np.count_nonzero(col) == 1:  # Check if it's a basic variable
            solution[i] = tableau[np.where(col == 1)[0], -1]

    optimal_value = tableau[-1, -1]  # The optimal value is in the bottom-right corner
    if problem_type == 'max':
        optimal_value *= -1  # Adjust for maximization

    return solution, optimal_value

# Input section
num_vars = int(input("Enter the number of variables: "))
num_constraints = int(input("Enter the number of constraints: "))
problem_type = input("Is this a maximization or minimization problem? (max/min): ").strip().lower()

c = np.zeros(num_vars)
print("Enter the coefficients of the objective function:")
for i in range(num_vars):
    c[i] = float(input(f"Coefficient of x{i+1}: "))

A = np.zeros((num_constraints, num_vars))
b = np.zeros(num_constraints)
inequalities = []
print("Enter the coefficients of the constraints:")
for i in range(num_constraints):
    for j in range(num_vars):
        A[i, j] = float(input(f"Coefficient of x{j+1} in constraint {i+1}: "))
    inequalities.append(input(f"Type of inequality for constraint {i+1} (<=, >=, =): ").strip())
    b[i] = float(input(f"Right-hand side of constraint {i+1}: "))

solution, optimal_value = dual_simplex(c, A, b, inequalities, problem_type)
print("Solution:", solution)
print("Optimal value:", optimal_value)
