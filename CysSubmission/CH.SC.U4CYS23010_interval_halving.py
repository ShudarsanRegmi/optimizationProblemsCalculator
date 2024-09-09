def evaluate_network_performance(bandwidth):
    """
    Simulate network performance based on bandwidth. Replace this with actual performance metrics.
    
    :param bandwidth: Bandwidth value to evaluate.
    :return: Performance metric for the given bandwidth.
    """
    # Example performance function; replace with actual evaluation logic
    optimal_bandwidth = 100  # Assume 100 Mbps is the ideal bandwidth
    performance = -1 * (bandwidth - optimal_bandwidth) ** 2 + 10000  # Simulated performance curve
    return performance

def interval_halving_bandwidth(f, low, high, tol):
    """
    Interval Halving Method to find the optimal bandwidth that maximizes network performance.
    
    :param f: Function to evaluate network performance.
    :param low: The minimum bandwidth to start with.
    :param high: The maximum bandwidth to start with.
    :param tol: The tolerance level; the method stops when the interval size is less than tol.
    :return: The optimal bandwidth approximation.
    """
    if f(low) * f(high) >= 0:
        raise ValueError("Function values at the interval endpoints must have opposite signs.")
    
    iteration = 0
    while (high - low) / 2.0 > tol:
        midpoint = (low + high) / 2.0
        f_mid = f(midpoint)
        
        # Print the current interval and midpoint for responsiveness
        print(f"Iteration {iteration}: Interval = [{low:.5f}, {high:.5f}], Midpoint = {midpoint:.5f}, f(Midpoint) = {f_mid:.5f}")
        
        # Determine which subinterval to use based on performance
        if f(low) * f_mid < 0:
            high = midpoint  # Optimal bandwidth is in the left subinterval
        else:
            low = midpoint  # Optimal bandwidth is in the right subinterval
        
        iteration += 1
    
    # Return the midpoint as the best approximation of the optimal bandwidth
    return (low + high) / 2.0

def main():
    print("Network Bandwidth Optimization Using Interval Halving Method")
    
    try:
        # Take user inputs
        low_bandwidth = float(input("Enter the minimum bandwidth (Mbps): "))
        high_bandwidth = float(input("Enter the maximum bandwidth (Mbps): "))
        tolerance = float(input("Enter the tolerance level (e.g., 1e-5): "))

        # Check if the inputs are valid
        if low_bandwidth >= high_bandwidth:
            raise ValueError("Minimum bandwidth must be less than maximum bandwidth.")
        if tolerance <= 0:
            raise ValueError("Tolerance must be a positive number.")
        
        # Find the optimal bandwidth
        optimal_bandwidth = interval_halving_bandwidth(evaluate_network_performance, low_bandwidth, high_bandwidth, tolerance)
        
        # Print the result
        print(f"\nOptimal Bandwidth: {optimal_bandwidth:.5f} Mbps")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
