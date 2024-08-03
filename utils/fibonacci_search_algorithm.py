import sympy as sp


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
    if (n-k < 0):
        print("Maximum Iteration Reached..")
        return -1
    return fibo(n-k) / fibo(n-k+1)

print(get_kth_ratio(9))



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
initial_row = [initial_ratio, l1, r1, x1, x2, func(x1), func(x2), l_r]

table.append(initial_row)

print(table)
