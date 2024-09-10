

python
import math

def secant_method(f, x0, x1, tol, max_iter):
    """
    Secant method to find the root of a function f(x).

    Parameters:
    f (function): The function for which we want to find the root.
    x0 (float): The first initial guess.
    x1 (float): The second initial guess.
    tol (float): The tolerance for stopping the iteration (accuracy).
    max_iter (int): The maximum number of iterations to perform.

    Returns:
    float: The approximate root of the function or None if it doesn't converge.
    """
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < tol:
            print("Small function difference. Possible division by zero.")
            return None

        # Secant method formula
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:
            return x2

        # Update guesses
        x0, x1 = x1, x2

    print("Maximum iterations reached. Method did not converge.")
    return None

# Generalized function handler
def general_func(f, target_value, x):
    """
    Generalized function handler that takes a mathematical function f(x) and adjusts it to target_value.
    f: The function (e.g., math.sin, math.exp, math.log)
    target_value: The value of the function we are solving for (e.g., sin(x) = 0.5, we solve for x)
    x: The value of x at which to evaluate the function
    """
    return f(x) - target_value

# Get user input to select the function type
print("Choose a function to solve:")
print("1. Trigonometric (e.g., sin(x) = target, cos(x) = target, tan(x) = target)")
print("2. Exponential (e.g., exp(x) = target)")
print("3. Logarithmic (e.g., log(x) = target)")
print("4. Polynomial (e.g., x^n + ax^m + ... = target)")

choice = input("Enter the number corresponding to the function: ")

# Initialize guesses for the secant method
x0, x1 = 0, 0  # Default initialization, will be set later
target_value = 0  # Initialize target value

if choice == '1':
    print("Choose a trigonometric function:")
    print("a. sin(x)")
    print("b. cos(x)")
    print("c. tan(x)")

    trig_choice = input("Enter the letter corresponding to the trigonometric function: ")

    if trig_choice == 'a':
        trig_f = math.sin
    elif trig_choice == 'b':
        trig_f = math.cos
    elif trig_choice == 'c':
        trig_f = math.tan
    else:
        print("Invalid choice!")
        trig_f = None

    if trig_f:
        target_value = float(input("Enter the target value (e.g., for sin(x) = target): "))
        x0, x1 = 0.5, 2  # Adjust initial guesses for the specific function if necessary
        root = secant_method(lambda x: general_func(trig_f, target_value, x), x0, x1, tol=1e-6, max_iter=100)

elif choice == '2':
    print("Solving exp(x) = target")
    target_value = float(input("Enter the target value for exp(x): "))
    x0, x1 = 0, 1  # Initial guesses for exponential
    root = secant_method(lambda x: general_func(math.exp, target_value, x), x0, x1, tol=1e-6, max_iter=100)

elif choice == '3':
    print("Solving log(x) = target")
    target_value = float(input("Enter the target value for log(x): "))
    x0, x1 = 15, 25  # Initial guesses for logarithmic
    root = secant_method(lambda x: general_func(math.log, target_value, x), x0, x1, tol=1e-6, max_iter=100)

elif choice == '4':
    print("Solving a polynomial equation of the form x^n + ax^m + ... = target")
    
    # Get polynomial degree and coefficients from the user
    degree = int(input("Enter the degree of the polynomial: "))
    
    # Collect coefficients
    coefficients = []
    for i in range(degree, -1, -1):
        coeff = float(input(f"Enter the coefficient for x^{i}: "))
        coefficients.append(coeff)

    target_value = float(input("Enter the target value for the polynomial: "))
    
    # Define the polynomial function
    def poly_func(x):
        result = 0
        for i, coeff in enumerate(coefficients):
            power = degree - i
            result += coeff * (x ** power)
        return result - target_value  # Adjust by target value

    x0, x1 = 0, 2  # Initial guesses for the polynomial
    root = secant_method(poly_func, x0, x1, tol=1e-6, max_iter=100)

else:
    print("Invalid choice!")
    root = None

if root is not None:
    print(f"Root is approximately: {root}")
else:
    print("No root found or method did not converge.")


