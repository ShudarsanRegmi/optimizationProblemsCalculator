import math

# Golden Ratio constant
phi = (1 + math.sqrt(5)) / 2

def golden_section_search(f, a, b, tol):
   
    
    # Initialize points
    c = b - (b - a) / phi
    d = a + (b - a) / phi
    
    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        
        # Recompute points
        c = b - (b - a) / phi
        d = a + (b - a) / phi
    
    # Return the approximate minimum point
    return (b + a) / 2

# Example usage
if  __name__ == "__main__":
    # Define a test function (unimodal)
    def f(x):
        return (x - 2)**2 + 3
    # User inputs the function as a string
    function_str = input("Enter the function to minimize (use 'x' as the variable, e.g., (x-2)**2 + 3): ")

# Convert the string input into a lambda function
    f = eval(f"lambda x: {function_str}")

# User inputs the interval [a, b]
    a = float(input("Enter the left endpoint of the interval (a): "))
    b = float(input("Enter the right endpoint of the interval (b): "))

# User inputs the tolerance
    tol = float(input("Enter the stopping tolerance: "))
    # Perform the search on the interval [0, 5]
    result = golden_section_search(f, 0, 5, 0.01)
    print(f"The minimum is approximately at x = {result}")
