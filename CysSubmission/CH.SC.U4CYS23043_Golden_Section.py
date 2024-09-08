def golden_section_search(f, a, b, tol=1e-5, max_iter=100):
    """
    Golden Section Search method to find the minimum of a function f within an interval [a, b].

    Parameters:
    f : function
        The function for which we are finding the minimum.
    a : float
        The start of the interval.
    b : float
        The end of the interval.
    tol : float
        The tolerance level for convergence.
    max_iter : int
        The maximum number of iterations.

    Returns:
    x_min : float
        The approximated minimum of the function.
    """
    # Golden ratio
    gr = (1 + 5**0.5) / 2
    
    # Calculate the initial points
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    
    iter_count = 0
    while (b - a) > tol and iter_count < max_iter:
        fc = f(c)
        fd = f(d)
        
        if fc < fd:
            b = d
            d = c
            c = b - (b - a) / gr
        else:
            a = c
            c = d
            d = a + (b - a) / gr
        
        iter_count += 1
    
    # Return the midpoint of the final interval as the approximation of the minimum
    return (a + b) / 2

# Example usage
if _name_=="_main_":
    # Define the function for which we want to find the minimum
    def func(x):
        return (x - 2) ** 2 + 1
    
    # Define the interval [a, b]
    a = 0
    b = 4
    
    # Find the minimum
    x_min = golden_section_search(func, a, b)
    print(f"The minimum is approximately at x = {x_min:.5f}")
    print(f"Function value at this minimum: {func(x_min):.5f}")
