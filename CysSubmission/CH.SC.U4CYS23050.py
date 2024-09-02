'''
Maximize: Z = 40x1 + 30x2
Subject to: x1 + x2 <= 12
2x1 + x2 <= 16
x1 >= 0, x2 >= 0
solution:
x1 = 4.0
x2 = 8.0
Objective function value: 400.0
'''

def print_table(table, num_vars, num_constraints):
    print(f"{'Basic Variables':<15}|", end="")
    for j in range(num_vars):
        print(f"x{j + 1:<10} ", end="")
    for i in range(num_constraints):
        print(f"S{i + 1:<10} ", end="")
    print("RHS")
    print("-" * 60)

    for i in range(len(table)):
        if i < num_constraints:
            print(f"Constraint {i + 1:<15}|", end="")
        else:
            print("Objective Function |", end="")
        for j in range(len(table[i]) - 1):
            print(f"{table[i][j]:<10.3f} ", end="")
        print(f"{table[i][-1]:<10.3f}")
    print("-" * 60)

def find_pivot_column(table, is_maximize):
    pivot_col = 0
    for i in range(1, len(table[0]) - 1):
        if (is_maximize and table[-1][i] < table[-1][pivot_col]) or \
           (not is_maximize and table[-1][i] > table[-1][pivot_col]):
            pivot_col = i
    return pivot_col

def find_pivot_row(table, pivot_col):
    pivot_row = -1
    min_ratio = float('inf')
    for i in range(len(table) - 1):
        if table[i][pivot_col] > 0:
            ratio = table[i][-1] / table[i][pivot_col]
            if ratio < min_ratio:
                min_ratio = ratio
                pivot_row = i
    return pivot_row

def pivot(table, pivot_row, pivot_col):
    pivot_value = table[pivot_row][pivot_col]
    table[pivot_row] = [x / pivot_value for x in table[pivot_row]]

    for i in range(len(table)):
        if i != pivot_row:
            factor = table[i][pivot_col]
            table[i] = [table[i][j] - factor * table[pivot_row][j] for j in range(len(table[i]))]

def simplex_method(table, is_maximize, num_vars, num_constraints):
    iteration = 0

    while True:
        print(f"Iteration {iteration + 1}:")
        print_table(table, num_vars, num_constraints)

        pivot_col = find_pivot_column(table, is_maximize)
        if (is_maximize and table[-1][pivot_col] >= 0) or \
           (not is_maximize and table[-1][pivot_col] <= 0):
            print("Optimal solution found.")
            break

        pivot_row = find_pivot_row(table, pivot_col)
        if pivot_row == -1:
            print("Unbounded solution.")
            return

        pivot(table, pivot_row, pivot_col)
        iteration += 1

    print("Final solution:")
    print_table(table, num_vars, num_constraints)

    variable_values = [0] * num_vars
    for i in range(num_constraints):
        for j in range(num_vars):
            if table[i][j] == 1:
                if all(table[k][j] == 0 for k in range(num_constraints) if k != i):
                    variable_values[j] = table[i][-1]

    print("\nValues of decision variables:")
    for i in range(num_vars):
        print(f"x{i + 1} = {variable_values[i]}")
    print(f"Objective function value: {table[-1][-1]}")

def main():
    num_vars = int(input("Enter the number of variables: "))
    num_constraints = int(input("Enter the number of constraints: "))

    # Initialize the table with zeros
    table = [[0] * (num_vars + num_constraints + 1) for _ in range(num_constraints + 1)]

    print("Enter the coefficients of the constraints:")
    for i in range(num_constraints):
        print(f"Constraint {i + 1} coefficients:")
        table[i][:num_vars] = list(map(float, input().split()))
        table[i][num_vars + i] = 1  # Add slack variable
        table[i][-1] = float(input("Enter the RHS value for this constraint: "))

    print("Enter the coefficients of the objective function:")
    table[-1][:num_vars] = list(map(float, input().split()))

    choice = input("Do you want to (M)aximize or (m)inimize the objective function? ").strip()
    is_maximize = choice.lower() == 'm'

    if is_maximize:
        table[-1][:num_vars] = [-x for x in table[-1][:num_vars]]

    simplex_method(table, is_maximize, num_vars, num_constraints)

if __name__ == "__main__":
    main()
