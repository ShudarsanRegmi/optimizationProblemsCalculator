import math  

def f(x):
    return eval(func_input)  

def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            print("Division by zero encountered!")
            return None


        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:
            print(f"Converged in {i+1} iterations.")
            return x2

        x0, x1 = x1, x2

    print(f"Did not converge after {max_iter} iterations.")
    return x2

func_input = input("Enter the function in terms of x (e.g., 'math.sin(x)', 'x**2 - 4', etc.): ")

x0 = float(input("Enter the first initial guess (x0): "))
x1 = float(input("Enter the second initial guess (x1): "))
tol = float(input("Enter the tolerance (e.g., 0.0001): "))


root = secant_method(f, x0, x1, tol)

# Output the result
if root is not None:
    print(f"Found root: {root}")
