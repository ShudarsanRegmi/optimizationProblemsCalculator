import math

# Define the golden section search algorithm
def golden_section_search(f, a, b, tol=1e-5, find_max=False):
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio, approximately 1.618

    # Initial points for the golden section method
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    # Iterate until the interval length is within the tolerance
    while abs(b - a) > tol:
        if find_max:
            # Maximization case
            if f(x1) > f(x2):
                b = x2
            else:
                a = x1
        else:
            # Minimization case
            if f(x1) < f(x2):
                b = x2
            else:
                a = x1

        # Recalculate new points
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi

    return (a + b) / 2  # The final point approximation

# Ask user for maximum or minimum
opt_type = input("Do you want to find the 'maximum' or 'minimum'? ").strip().lower()
if opt_type not in ['maximum', 'minimum']:
    print("Error: Please enter 'maximum' or 'minimum'.")
    exit(1)

# Ask the user for a custom function
f_input = input("Enter the function f(x) (use 'x' as the variable, e.g., '4*x**3 + x**2 - 7*x + 14'): ")

# Allow names from the math library
allowed_names = {name: getattr(math, name) for name in dir(math) if not name.startswith("__")}
allowed_names['x'] = 0  # Initialize x variable

# Convert the user input into a lambda function
try:
    f = eval(f"lambda x: {f_input}", {"__builtins__": None}, allowed_names)
except (SyntaxError, NameError) as e:
    print(f"Error: Invalid function. Make sure your function uses 'x' as the variable and is a valid mathematical expression. Details: {e}")
    exit(1)

# Get the interval from the user
try:
    a = float(input("Enter the lower bound of the interval a: "))
    b = float(input("Enter the upper bound of the interval b: "))
    if a >= b:
        raise ValueError("The lower bound a must be less than the upper bound b.")
except ValueError as e:
    print(f"Error: {e}")
    exit(1)

# Get tolerance (optional input)
tol_input = input("Enter the tolerance (or press Enter to use default 1e-5): ")
tol = float(tol_input) if tol_input.strip() else 1e-5

# Check if the user selected maximum or minimum
find_max = opt_type == 'maximum'

# Call the golden section search function
result = golden_section_search(f, a, b, tol=tol, find_max=find_max)

# Output the result
if find_max:
    print(f"The maximum value is approximately at x = {result:.5f}")
else:
    print(f"The minimum value is approximately at x = {result:.5f}")
