import sympy as sp

def newton_raphson_optimization(expr, initial_guess, tol, max_iter=100):
    """Apply the Newton-Raphson method for optimization to find a local minimum or maximum."""
    x = sp.Symbol('x')
    
    # Derivatives
    f_prime = sp.lambdify(x, sp.diff(expr, x), 'math')  # First derivative (f'(x))
    f_double_prime = sp.lambdify(x, sp.diff(expr, x, 2), 'math')  # Second derivative (f''(x))
    
    current_guess = initial_guess
    iter_count = 0

    while iter_count < max_iter:
        fp = f_prime(current_guess)
        fpp = f_double_prime(current_guess)
        
        if fpp == 0:  # Avoid division by zero
            print("Second derivative is zero; cannot continue.")
            return current_guess
        
        # Compute the new guess using the Newton-Raphson formula for optimization
        new_guess = current_guess - fp / fpp
        
        # Check if the change in the guess is below the tolerance
        if abs(new_guess - current_guess) < tol:
            print(f"Convergence reached in {iter_count} iterations.")
            break
        
        current_guess = new_guess
        iter_count += 1
        print(f"Iteration {iter_count}: x = {current_guess:.6f}")
    
    if iter_count == max_iter:
        print("Max iterations reached without convergence.")
    
    return current_guess

def main():
    expr_input = input("Enter the expression to optimize (e.g., x**3 - 3*x**2 + 2): ")
    
    try:
        # Parse the expression
        x = sp.Symbol('x')
        expr = sp.sympify(expr_input)
        
        # Initial guess
        initial_guess = float(input("Enter an initial guess: "))
        
        # Tolerance input
        tol = float(input("Enter the tolerance value (e.g., 1e-6): "))
        
        print("Running Newton-Raphson Optimization...")
        result = newton_raphson_optimization(expr, initial_guess, tol)
        
        print(f"Optimized point: x = {result:.6f}")
        print(f"Function value at optimized point: f(x) = {expr.evalf(subs={x: result}):.6f}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
