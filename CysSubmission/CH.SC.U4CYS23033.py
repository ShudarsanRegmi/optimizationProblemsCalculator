# Newton-Raphson Method Implementation in Python

"""
Newton-Raphson Method
=====================
The Newton-Raphson method is an iterative numerical technique used to approximate
the roots of a real-valued function. This file implements the method, along with
examples, test cases, and expected output.
"""

# Import necessary modules (if any are needed for additional functionality)

# Function: newton_raphson
def newton_raphson(f, df, x0, tolerance=1e-7, max_iter=100):
    """
    Newton-Raphson method for finding the root of a function.
    
    Parameters:
    f : function
        The function whose root is being found.
    df : function
        The derivative of the function.
    x0 : float
        Initial guess for the root.
    tolerance : float
        The tolerance for convergence.
    max_iter : int
        Maximum number of iterations before the method halts.
    
    Returns:
    float or None
        The root of the function, or None if the solution doesn't converge.
    """
    
    x_n = x0
    for n in range(max_iter):
        f_xn = f(x_n)
        df_xn = df(x_n)
        
        if df_xn == 0:
            print(f"Zero derivative at x = {x_n}. No solution found.")
            return None
        
        x_next = x_n - f_xn / df_xn
        
        if abs(x_next - x_n) < tolerance:
            print(f"Converged to {x_next} after {n+1} iterations.")
            return x_next
        
        x_n = x_next
    
    print("Exceeded maximum iterations. No solution found.")
    return None


# Example usage of the Newton-Raphson method
def example_func(x):
    """
    Example function: f(x) = x^2 - 2.
    The root of this function is sqrt(2).
    """
    return x**2 - 2

def example_derivative(x):
    """
    Derivative of the example function: f'(x) = 2x.
    """
    return 2 * x


if __name__ == "__main__":
    # Example of finding the root of the equation f(x) = x^2 - 2
    print("Example: Finding the root of x^2 - 2 = 0")
    root = newton_raphson(example_func, example_derivative, 1)
    print(f"Calculated Root: {root}")

    # Test cases
    print("\nRunning test cases...")

    # Test case 1: Solving for sqrt(2) with an initial guess of 1
    print("Test Case 1: Solving x^2 - 2 = 0 with initial guess x0 = 1")
    root1 = newton_raphson(example_func, example_derivative, 1)
    print(f"Result: Root = {root1}\n")

    # Test case 2: Solving for sqrt(2) with an initial guess of 2
    print("Test Case 2: Solving x^2 - 2 = 0 with initial guess x0 = 2")
    root2 = newton_raphson(example_func, example_derivative, 2)
    print(f"Result: Root = {root2}\n")

    # Test case 3: Function with zero derivative (f(x) = x^3)
    print("Test Case 3: Function with zero derivative at x = 0 (f(x) = x^3)")
    def zero_derivative_func(x):
        return x**3
    
    def zero_derivative_derivative(x):
        return 3 * x**2
    
    root3 = newton_raphson(zero_derivative_func, zero_derivative_derivative, 0)
    print(f"Result: Root = {root3}\n")

    # Test case 4: Function that oscillates (f(x) = x^3 - 2x + 2)
    print("Test Case 4: Oscillating function (f(x) = x^3 - 2x + 2)")
    def oscillating_func(x):
        return x**3 - 2*x + 2
    
    def oscillating_derivative(x):
        return 3*x**2 - 2
    
    root4 = newton_raphson(oscillating_func, oscillating_derivative, 0)
    print(f"Result: Root = {root4}\n")

"""
# Conclusion

This Python script implements the Newton-Raphson method for finding the roots of real-valued functions. 

## Key Points:

1. **Newton-Raphson Method**:
   - This numerical technique iterates to approximate the root of a function.
   - It uses the formula: x_{n+1} = x_n - f(x_n) / f'(x_n) to update guesses.

2. **Implementation**:
   - The `newton_raphson` function takes a function, its derivative, an initial guess, and optional parameters for tolerance and maximum iterations.
   - It iteratively refines the guess for the root and prints the result upon convergence or failure.

3. **Example**:
   - An example of finding the root of the function f(x) = x^2 - 2 is provided. The root approximates sqrt(2), demonstrating the method's practical application.

4. **Test Cases**:
   - Several test cases are included to validate the implementation. They cover:
     - Standard root finding
     - Cases with zero derivatives
     - Oscillating functions
   - The output of these test cases demonstrates the method's robustness and highlights scenarios where it may not converge.

5. **Usage**:
   - This script is designed to be easily run as a standalone file. Modify the function and its derivative in the example usage section to apply the Newton-Raphson method to different problems.
   
