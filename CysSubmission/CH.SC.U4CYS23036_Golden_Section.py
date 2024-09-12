import math

def golden_section_search(f, a, b, tol=1e-5, mode='min'):
    """
    Perform Golden Section Search to find the minimum or maximum of a function.
    
    Parameters:
    f : function
        The function to be minimized or maximized.
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    tol : float
        The tolerance for stopping criterion.
    mode : str
        'min' for minimization, 'max' for maximization.

    Returns:
    float
        The x value where the function achieves the minimum or maximum.
    """
    phi = (1 + 5 ** 0.5) / 2  # Golden ratio
    inv_phi = 1 / phi
    c = b - inv_phi * (b - a)
    d = a + inv_phi * (b - a)

    while abs(b - a) > tol:
        if (mode == 'min' and f(c) < f(d)) or (mode == 'max' and f(c) > f(d)):
            b = d
        else:
            a = c
        c = b - inv_phi * (b - a)
        d = a + inv_phi * (b - a)

    return (b + a) / 2

# Question 1: Minimize f(x) = (x - 1)^2 + 4 in [0, 2]
# The function f(x) = (x - 1)^2 + 4 has its minimum value at x = 1.
# Expected result is 1.0.
f = lambda x: (x - 1) ** 2 + 4
result_min = golden_section_search(f, 0, 2, mode='min')
print("Minimum of f(x) at:", result_min)  # Expected: 1.0

# Question 2: Maximize g(x) = -x^2 + 4x - 1 in [0, 4]
# The function g(x) = -x^2 + 4x - 1 has its maximum value at x = 2.
# Expected result is 2.0.
g = lambda x: -x ** 2 + 4 * x - 1
result_max = golden_section_search(g, 0, 4, mode='max')
print("Maximum of g(x) at:", result_max)  # Expected: 2.0

# Question 3: Minimize h(x) = (x - 3)^2 + 2 in [0, 6]
# The function h(x) = (x - 3)^2 + 2 has its minimum value at x = 3.
# Expected result is 3.0.
h = lambda x: (x - 3) ** 2 + 2
result_min_h = golden_section_search(h, 0, 6, mode='min')
print("Minimum of h(x) at:", result_min_h)  # Expected: 3.0

# Question 4: Minimize j(x) = sin(x) + 2 in [0, 2π]
# The function j(x) = sin(x) + 2 is minimized when sin(x) is -1.
# Expected result is approximately x = 3π/2.
j = lambda x: math.sin(x) + 2
result_min_j = golden_section_search(j, 0, 2 * math.pi, mode='min')
print("Minimum of j(x) at:", result_min_j)  # Expected: approximately 4.712 (3π/2)

# Question 5: Maximize k(x) = -cos(x) in [0, π]
# The function k(x) = -cos(x) is maximized when cos(x) is -1.
# Expected result is approximately x = π.
k = lambda x: -math.cos(x)
result_max_k = golden_section_search(k, 0, math.pi, mode='max')
print("Maximum of k(x) at:", result_max_k)  # Expected: approximately 3.1416 (π)
