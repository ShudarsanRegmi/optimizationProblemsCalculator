'''
Test Case 1:
Enter 'max' for maximize/ 'min' for minizize: min
Enter the function to minimize/maximize (in terms of x): x*(x-1.5)
Enter the starting point of the interval (a): 0
Enter the ending point of the interval (b): 1
Do you want to use tolerance (T) or percentage constraint (P)? p
Enter the percentage constraint (e.g., 10 for 10%): 10
Iteration 1: Interval [0.5, 1.0]
Iteration 2: Interval [0.625, 0.875]
Iteration 3: Interval [0.6875, 0.8125]
The minimum value is approximately at x = 0.75 with function value f(x) = -0.5625

Test Case 2:
Enter 'max' for maximize/ 'min' for minizize: max
Enter the function to minimize/maximize (in terms of x): x*(x-1.5)
Enter the starting point of the interval (a): 0
Enter the ending point of the interval (b): 1
Do you want to use tolerance (T) or percentage constraint (P)? t
Enter the tolerance value (e.g., 0.1): 0.1
Iteration 1: Interval [0.0, 0.5]
Iteration 2: Interval [0.0, 0.25]
Iteration 3: Interval [0.0, 0.125]
Iteration 4: Interval [0.0, 0.0625]
The maximum value is approximately at x = 0.03125 with function value f(x) = -0.0458984375
'''

import math
def interval_halving(func, a, b, tol=None, percentage=None):
    """
    Interval Halving optimization technique.

    Parameters:
    func: The function to be minimized/maximized.
    a: The starting point of the interval.
    b: The ending point of the interval.
    tol: The tolerance for convergence.
    percentage: The percentage within which to minimize/maximize the function.

    Returns:
    The minimum/maximum point and the corresponding function value.
    """
    
    # Number of iterations counter
    iteration = 0
    
    if tol is not None:
        stopping_criterion = tol
        # Perform interval halving
        while (b - a) > stopping_criterion and iteration < 100:
            iteration += 1

            # Find three points within the interval
            x1 = a + (b - a) / 4
            x2 = a + 3 * (b - a) / 4
            x0 = (a + b) / 2
        
            # Evaluate the function at those points
            f1 = func(x1)
            f2 = func(x2)
            f0 = func(x0)

            if choice=="min":
                # Check where the function is smaller and update the interval
                arr = [f1, f2, f0]
                min_arr = min(arr)
                if min_arr == f0:
                    a = x1
                    b = x2
                elif min_arr == f1:
                    b = x0
                elif min_arr == f2:
                    a = x0
        
                print(f"Iteration {iteration}: Interval [{a}, {b}]")
                
            elif choice=="max":
                # Check where the function is larger and update the interval
                arr = [f1, f2, f0]
                max_arr = max(arr)
                if max_arr == f0:
                    a = x1
                    b = x2
                elif max_arr == f1:
                    b = x0
                elif max_arr == f2:
                    a = x0
        
                print(f"Iteration {iteration}: Interval [{a}, {b}]")

        # Compute the final midpoint as the optimal value
        x_opt = (a + b) / 2
        f_opt = func(x_opt)
        return x_opt, f_opt

    elif percentage is not None:
        L0 = b - a
        
        def check_inequality_for_n(n):
            # Check if the inequality Ln / 2 <= L0 / percentage holds true for n
            Ln = ((1/2)**((n-1)/2)) * L0
            lhs = Ln / 2
            rhs = L0 / percentage
            return lhs <= rhs

        def find_first_value_where_inequality_holds(min_n, max_n):
            # Find the first value of n where the inequality holds true
            for n in range(min_n, max_n + 1):
                if check_inequality_for_n(n):
                    return n
            return None

        result_value = find_first_value_where_inequality_holds(1, 50)

        if result_value is None:
            print("No values of n in the range satisfy the inequality.")
            return None, None

        iteration = 1
        while iteration <= result_value // 2:
            # Find three points within the interval
            x1 = a + (b - a) / 4
            x2 = a + 3 * (b - a) / 4
            x0 = (a + b) / 2
        
            # Evaluate the function at those points
            f1 = func(x1)
            f2 = func(x2)
            f0 = func(x0)

            if choice=="min":
                # Check where the function is smaller and update the interval
                arr = [f1, f2, f0]
                min_arr = min(arr)
                if min_arr == f0:
                    a = x1
                    b = x2
                elif min_arr == f1:
                    b = x0
                elif min_arr == f2:
                    a = x0
        
                print(f"Iteration {iteration}: Interval [{a}, {b}]")
                iteration += 1
                
            elif choice=="max":
                # Check where the function is larger and update the interval
                arr = [f1, f2, f0]
                max_arr = max(arr)
                if max_arr == f0:
                    a = x1
                    b = x2
                elif max_arr == f1:
                    b = x0
                elif max_arr == f2:
                    a = x0
        
                print(f"Iteration {iteration}: Interval [{a}, {b}]")
                iteration += 1

        # Compute the final midpoint as the optimal value
        x_opt = (a + b) / 2
        f_opt = func(x_opt)
        return x_opt, f_opt

    else:
        raise ValueError("Either tolerance or percentage must be provided.")

# Get if maximize/minimize
choice=input("Enter 'max' for maximize/ 'min' for minizize: ")

# Get function input from user
func_input = input("Enter the function to minimize/maximize (in terms of x): ")
# Example input: (x - 2)**2 + math.sin(5 * x)

# Convert the string into a function
def user_function(x):
    return eval(func_input)

# Get interval input from user
a = float(input("Enter the starting point of the interval (a): "))
b = float(input("Enter the ending point of the interval (b): "))

# Ask the user if they want to use tolerance or percentage constraint
method_choice = input("Do you want to use tolerance (T) or percentage constraint (P)? ").lower()

# Initialize tolerance and percentage variables
tol = None
percentage = None

if method_choice == 't':
    tol = float(input("Enter the tolerance value (e.g., 0.1): "))
elif method_choice == 'p':
    percentage = float(input("Enter the percentage constraint (e.g., 10 for 10%): "))
else:
    print("Invalid choice. Please restart and select either T or P.")
    exit()

# Call the interval halving function
if tol or percentage:
    x_value, f_value = interval_halving(user_function, a, b, tol=tol, percentage=percentage)
    if x_value is not None:
        if choice == "min":
            print(f"The minimum value is approximately at x = {x_value} with function value f(x) = {f_value}")
        elif choice == "max":
            print(f"The maximum value is approximately at x = {x_value} with function value f(x) = {f_value}")
            
