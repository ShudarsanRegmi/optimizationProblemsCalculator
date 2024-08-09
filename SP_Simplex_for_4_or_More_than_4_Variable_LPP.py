import numpy as np
from fractions import Fraction

def simplex_algorithm():
    print("\n**** Simplex Algorithm ****\n\n")

    # User inputs
    num_constraints = int(input("Enter the number of constraints: "))
    num_variables = int(input("Enter the number of variables: "))

    A = []
    print("Enter the coefficients of the constraints (row-wise):")
    for i in range(num_constraints):
        row = list(map(float, input(f"Constraint {i + 1}: ").split()))
        A.append(row)

    A = np.array(A)

    b = []
    print("Enter the amount of resources for each constraint:")
    for i in range(num_constraints):
        resource = float(input(f"Resource for constraint {i + 1}: "))
        b.append(resource)

    b = np.array(b)

    c = list(map(float, input("Enter the coefficients of the objective function: ").split()))

    B = np.array([[num_variables + i] for i in range(1, num_constraints + 1)])
    cb = np.array([0 for i in range(num_constraints)])
    xb = np.transpose([b])

    table = np.hstack((B, np.transpose([cb])))
    table = np.hstack((table, xb))
    table = np.hstack((table, A))
    table = np.array(table, dtype='float')

    MIN = 0
    print("Table at itr = 0")
    print("B \tCB \tXB \t" + "\t".join([f"y{i+1}" for i in range(num_variables + num_constraints)]))
    for row in table:
        for el in row:
            print(Fraction(str(el)).limit_denominator(100), end='\t')
        print()

    print("Simplex Working....")

    reached = 0
    itr = 1
    unbounded = 0
    alternate = 0

    while reached == 0:
        print("Iteration: ", end=' ')
        print(itr)
        print("B \tCB \tXB \t" + "\t".join([f"y{i+1}" for i in range(num_variables + num_constraints)]))
        for row in table:
            for el in row:
                print(Fraction(str(el)).limit_denominator(100), end='\t')
            print()

        rel_prof = []
        for i in range(len(A[0])):
            rel_prof.append(c[i] - np.sum(table[:, 1] * table[:, 3 + i]))

        print("rel profit: ", end=" ")
        for profit in rel_prof:
            print(Fraction(str(profit)).limit_denominator(100), end=", ")
        print()

        b_var = table[:, 0]

        for i in range(len(A[0])):
            present = False
            for j in range(len(b_var)):
                if int(b_var[j]) == i:
                    present = True
                    break
            if not present and rel_prof[i] == 0:
                alternate = 1
                print("Case of Alternate found")

        if all(profit <= 0 for profit in rel_prof):
            print("All profits are <= 0, optimality reached")
            reached = 1
            break

        k = rel_prof.index(max(rel_prof))
        min_ratio = 99999
        r = -1

        for i in range(len(table)):
            if table[:, 2][i] > 0 and table[:, 3 + k][i] > 0:
                val = table[:, 2][i] / table[:, 3 + k][i]
                if val < min_ratio:
                    min_ratio = val
                    r = i

        if r == -1:
            unbounded = 1
            print("Case of Unbounded")
            break

        print("pivot element index:", end=' ')
        print(np.array([r, 3 + k]))
        pivot = table[r][3 + k]
        print("pivot element: ", end=" ")
        print(Fraction(pivot).limit_denominator(100))

        table[r, 2:] = table[r, 2:] / pivot

        for i in range(len(table)):
            if i != r:
                table[i, 2:] = table[i, 2:] - table[i][3 + k] * table[r, 2:]

        table[r][0] = k
        table[r][1] = c[k]

        print()
        itr += 1
        print()
        print("*")

    if unbounded == 1:
        print("UNBOUNDED LPP")
        return

    if alternate == 1:
        print("ALTERNATE Solution")

    print("Optimal table:")
    print("B \tCB \tXB \t" + "\t".join([f"y{i+1}" for i in range(num_variables + num_constraints)]))
    for row in table:
        for el in row:
            print(Fraction(str(el)).limit_denominator(100), end='\t')
        print()

    print()
    print("Value of Z at optimality: ", end=" ")
    sum = 0
    for i in range(len(table)):
        sum += table[i][1] * table[i][2]
    if MIN == 1:
        print(-Fraction(str(sum)).limit_denominator(100))
    else:
        print(Fraction(str(sum)).limit_denominator(100))

    basis = []
    for i in range(len(table)):
        temp = "x" + str(int(table[i][0]) + 1)
        basis.append(temp)

    print("Final Basis: ", end=" ")
    print(basis)
    print("Simplex Finished...")

# To run the function
simplex_algorithm()
