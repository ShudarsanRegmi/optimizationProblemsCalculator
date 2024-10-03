import numpy as np
import itertools

def get_user_input():
    # Get the number of constraints from the user
    num_constraints = int(input("Enter the number of constraints: "))

    # Initialize lists to store coefficients of constraints
    A = []
    b = []

    for i in range(num_constraints):
        # Input coefficients for the constraint
        coefficients = list(map(float, input(f"Enter coefficients for constraint {i+1} (separated by space, e.g., 'a b' for ax + by ≤ c): ").split()))
        rhs = float(input(f"Enter the RHS value for constraint {i+1}: "))
        A.append(coefficients)
        b.append(rhs)

    # Get the coefficients for the objective function
    obj_coefficients = list(map(float, input("Enter coefficients for the objective function (separated by space, e.g., 'c d' for cx + dy): ").split()))

    return np.array(A), np.array(b), np.array(obj_coefficients)

def find_intersections(A, b):
    vertices = []

    # Find intersections between every pair of constraints
    for (i, j) in itertools.combinations(range(len(A)), 2):
        A_subset = np.array([A[i], A[j]])
        b_subset = np.array([b[i], b[j]])
        try:
            # Solve the system of equations
            vertex = np.linalg.lstsq(A_subset, b_subset, rcond=None)[0]
            # Check if the vertex is valid (non-negative if constraints require it)
            if np.all(vertex >= 0):
                vertices.append(vertex)
        except np.linalg.LinAlgError:
            # Handle cases where constraints are parallel and do not intersect
            pass

    return np.array(vertices)

def objective_function(x, obj_coefficients):
    return np.dot(obj_coefficients, x)

def find_optimal_solution(vertices, obj_coefficients):
    optimal_value = -np.inf
    optimal_vertex = None

    for vertex in vertices:
        value = objective_function(vertex, obj_coefficients)
        if value > optimal_value:
            optimal_value = value
            optimal_vertex = vertex

    return optimal_vertex, optimal_value

def main():
    A, b, obj_coefficients = get_user_input()

    # Find the intersection points of the constraints
    vertices = find_intersections(A, b)

    if len(vertices) == 0:
        print("No feasible region found.")
        return

    # Find the optimal solution
    optimal_vertex, optimal_value = find_optimal_solution(vertices, obj_coefficients)

    if optimal_vertex is not None:
        print(f"Optimal solution found at x = {optimal_vertex[0]}, y = {optimal_vertex[1]}")
        print(f"Maximum value of the objective function: {optimal_value}")
    else:
        print("No feasible solution found.")

if __name__ == "__main__":
    main()
