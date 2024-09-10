import math

def f(x, equation):
    try:
        return eval(equation)
    except Exception as e:
        print(f"Error in equation: {e}")
        return None

def secant(x1, x2, tolerance, equation):
    iteration_count = 0
    
    if f(x1, equation) is None or f(x2, equation) is None:
        return
    
    if f(x1, equation) * f(x2, equation) >= 0:
        print("Invalid initial guesses: Root may not exist within the given interval.")
        return
    
    while True:
        f_x1 = f(x1, equation)
        f_x2 = f(x2, equation)
        
        x0 = (x1 * f_x2 - x2 * f_x1) / (f_x2 - f_x1)
        
        if abs(x2 - x1) < tolerance:
            break
        
        x1, x2 = x2, x0
        iteration_count += 1
    
    print(f"Root of the equation = {round(x0, 6)}")
    print(f"Number of iterations = {iteration_count}")

equation = input("Enter the equation (in terms of x): ")
x1 = float(input("Enter the first guess: "))
x2 = float(input("Enter the second guess: "))
tolerance = float(input("Enter the tolerance level: "))

secant(x1, x2, tolerance, equation)
