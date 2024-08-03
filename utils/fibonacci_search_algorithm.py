import sympy as sp
from table_printer import print_table

# Columns Of table
K = 0
Rat = 1
L = 2
R = 3
X1 = 4
X2 = 5
FX1 = 6
FX2 = 7
L_R = 8

# INPUTS
x = sp.Symbol('x')

y = x**2
interval = (-5, 15)
n = 7 # no. of iterations

# Utility Functions

def func(x_val):
    # Define the values to substitute
    values = {x: x_val}

    # Substitute the values into the expression and evaluate
    result = y.subs(values)
    return result

def fibo(n): #Todo: To make this logic iterative
    if n<0:
        print("Value of n =", n)
        raise ValueError("Value of n is negative")
    if n==0:
        return 1
    elif n==1:
        return 1
    return fibo(n-1)+fibo(n-2)


def get_kth_ratio(k):
    print("K = ", k)
    print("n-k= ", n-k, "n-k+1", n-k+1)
    print(fibo(n-k))
    print(fibo(n-k+1))
    if (n-k < 0):
        print("Maximum Iteration Reached..")
        return -1
    return fibo(n-k) / fibo(n-k+1)




def calculate_x2(k):
    r = table[k-1][1]
    l = table[k-1][0]
    ratio = get_kth_ratio(k)
    return l + ratio*(r-l)
def calculate_x2(k):
    r = table[k - 1][2]
    l = table[k - 1][1]
    x2 = table[k-1][4]

    return l + r - x2


def compare_f_values(x1, x2):
    """
    0 return value indicates 'l' to be taken
    1 return value indicates 'r' to be taken
    """
    if func(x1) < func(x2):
        return 0
    elif func(x1) > func(x2):
        return 1
    else:
        print("Function valuees are equal")
        return -1

# Initialization
table = []
initial_ratio = get_kth_ratio(1)
l1 = interval[0]
r1 = interval[1]
x2 = l1 + initial_ratio*(r1-l1)
x1 = l1 + r1 - x2
l_r = compare_f_values(x1, x2)
initial_row = [1, initial_ratio, l1, r1, x1, x2, func(x1), func(x2), l_r]

table.append(initial_row)

print(table)

for k in range(1,n):
    row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    row[K] = k+1
    if l_r != 0: # if is equal to 0,
        # left colum to keep as it is
        row[L] = table[k-1][X1]
        row[R] = table[k-1][R]
    else:
        row[R] = table[k-1][X2]
        row[L] = table[k-1][L]

    current_ratio = get_kth_ratio(k+1)
    row[Rat] = current_ratio

    row[X2] = row[L] + current_ratio*(row[R]-row[L])
    row[X1] = row[L] + row[R] - row[X2]

    x1_val = row[X1]
    x2_val = row[X2]

    row[FX1] = func(x1_val)
    row[FX2] = func(x2_val)

    l_r = compare_f_values(x1_val, x2_val)
    row[L_R] = l_r

    table.append(row)
    print(row)

print("Printing final table...")
print(table)

# print(table)
# print_table(table, ["K","Ratio","L","R","x1", "x2", "f(x1)", "f(x2)", "L/R"])

# Now find the final answer by unimodel principle
x_appox = (table[n-1][L] + table[n-1][R]) / 2

print("X value = ", x_appox)
print("f(x) value = ", func(x_appox))
