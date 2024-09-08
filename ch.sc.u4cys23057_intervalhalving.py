import math

# Define the function for which we want to find the minimum
def func(x):
    return x * x + 4 * math.sin(x)  # Example function f(x) = x^2 + 4sin(x)

# Interval Halving Method to find the minimum
def interval_halving(a, b, epsilon):
    while (b - a) > epsilon:
        mid1 = a + (b - a) / 4.0  # First mid-point
        mid2 = b - (b - a) / 4.0  # Second mid-point

        f1 = func(mid1)
        f2 = func(mid2)

        if f1 < f2:
            b = mid2
        else:
            a = mid1

    return (a + b) / 2.0  # Return the mid-point as the minimum

# Example usage
a = -10
b = 10
epsilon = 0.001
minimum = interval_halving(a, b, epsilon)

print(f"The minimum value is at x = {minimum}")
