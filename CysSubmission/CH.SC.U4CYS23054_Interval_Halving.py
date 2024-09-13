def interval_halving(f, a, b, tol=1e-5, max_iter=100):
    """
    Interval Halving method to find the root of a function f within an interval [a, b].
    
    Parameters:
    f : function
        The function for which we are finding the root.
    a : float
        The start of the interval.
    b : float
        The end of the interval.
    tol : float
        The tolerance level for convergence.
    max_iter : int
        The maximum number of iterations.
        
    Returns:
    root : float
        The approximated root of the function.
    """
    # Check if the function has opposite signs at the endpoints
    if f(a) * f(b) > 0:
        raise ValueError("Function must have opposite signs at the interval endpoints.")
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        # Calculate the midpoint of the interval
        midpoint = (a + b) / 2
        
        # Evaluate the function at the midpoint
        f_mid = f(midpoint)
        
        # Decide which subinterval to keep
        if f(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint
        
        iter_count += 1
    
    # Return the midpoint as the root approximation
    return (a + b) / 2

# Example usage
if __name__ == "__main__":
    # Define the function for which we want to find the root
    def func(x):
        return x**3 - x - 2
    
    # Define the interval [a, b]
    a = 1
    b = 2
    
    # Find the root
    root = interval_halving(func, a, b)
    print(f"The root is approximately: {root:.5f}")
