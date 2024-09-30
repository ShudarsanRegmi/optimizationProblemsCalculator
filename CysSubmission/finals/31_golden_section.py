import math

def golden_section_search(f, a, b, tol=1e-5):
    golden_ratio = (math.sqrt(5) - 1) / 2  # Golden ratio ≈ 0.618

    # Initial points
    c = b - golden_ratio * (b - a)
    d = a + golden_ratio * (b - a)

    while (b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        # Recalculate new points
        c = b - golden_ratio * (b - a)
        d = a + golden_ratio * (b - a)

    # Return the midpoint as the optimal value
    return (a + b) / 2

# Example usage
f = lambda x: (x - 2) ** 2  # Example function with a minimum at x=2
result = golden_section_search(f, a=0, b=5)
print(f"Optimal value found at: {result}")
