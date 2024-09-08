def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        print(f"Iteration {i+1}: x = {x}, f(x) = {fx}, f'(x) = {dfx}")

        if abs(fx) < tol:
            print(f"Converged after {i+1} iterations with root: {x}")
            return x, i+1
        
        x = x - fx / dfx

    raise ValueError("Maximum iterations exceeded. No solution found.")

# Example usage:
f = lambda x: x**3 - 2*x - 5  # Function: x^3 - 2x - 5 = 0
df = lambda x: 3*x**2 - 2     # Derivative: 3x^2 - 2

x0 = 2.0

root, iterations = newton_raphson(f, df, x0=x0, tol=1e-6)

print(f"Root: {root}, found in {iterations} iterations.")
