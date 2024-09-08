import math

def safe_evaluate(expression, x):
    # Safely evaluate the function for a given x
    allowed_functions = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "sqrt": math.sqrt,
        "exp": math.exp,
        "x": x
    }

    try:
        result = eval(expression, {"_builtins_": None}, allowed_functions)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        result = None

    return result

def find_optimal_points(interval, expression, num_iterations, maximize):
    current_interval = interval
    for iteration in range(1, num_iterations + 1):
        mid_left = (current_interval[0] + current_interval[1]) / 2
        left_third = (current_interval[0] + mid_left) / 2
        right_third = (mid_left + current_interval[1]) / 2

        y_mid_left = safe_evaluate(expression, mid_left)
        y_left_third = safe_evaluate(expression, left_third)
        y_right_third = safe_evaluate(expression, right_third)

        if y_mid_left is None or y_left_third is None or y_right_third is None:
            print("Error in evaluating function at one or more points.")
            return None

        print(f"\nIteration {iteration}:")
        print(f"Mid-left x = {mid_left}, f(x) = {y_mid_left}")
        print(f"Left-third x = {left_third}, f(x) = {y_left_third}")
        print(f"Right-third x = {right_third}, f(x) = {y_right_third}")

        if maximize:
            if y_right_third < y_mid_left and y_mid_left < y_left_third:
                current_interval[1] = mid_left
            elif y_left_third < y_mid_left and y_mid_left < y_right_third:
                current_interval[0] = mid_left
            elif y_left_third < y_mid_left and y_right_third < y_mid_left:
                current_interval = [left_third, right_third]
        else:
            if y_right_third > y_mid_left and y_mid_left > y_left_third:
                current_interval[1] = mid_left
            elif y_left_third > y_mid_left and y_mid_left > y_right_third:
                current_interval[0] = mid_left
            elif y_left_third > y_mid_left and y_right_third > y_mid_left:
                current_interval = [left_third, right_third]

    current_interval = [left_third, right_third]
    return y_mid_left

def input_interval():
    intervals = []
    for i in range(2):
        value = float(input(f"Enter the endpoint {i + 1} of the interval: "))
        intervals.append(value)
    return intervals

def calculate_n(accuracy_fraction):
    l1 = math.log(accuracy_fraction) / math.log(0.5)
    l2 = l1 + 0.25
    x = l2 / 0.5
    return math.ceil(x)

def get_iteration_count(max_value):
    iterations = []
    if max_value % 2 == 0:
        for i in range(3, max_value):
            if i % 2 != 0:
                iterations.append(i)
    else:
        for i in range(3, max_value + 1):
            if i % 2 != 0:
                iterations.append(i)
    
    return len(iterations)

print("\n\t\t***** WELCOME TO THE INTERVAL HALVING/BISECTION METHOD *****\n")

expression = input("Enter the function f(x): ")

interval = input_interval()  # Call to the interval input function

initial_length = interval[1] - interval[0]

accuracy_percentage = float(input("Enter the desired accuracy percentage: "))
accuracy_fraction = accuracy_percentage / 100

n = calculate_n(accuracy_fraction)  # Compute value of n
num_iterations = get_iteration_count(n)  # Compute number of iterations

# Prompt user to choose between maximization or minimization
opt_choice = input("Do you want to maximize or minimize the function? Enter 'maximize' or 'minimize': ").strip().lower()
maximize = opt_choice == 'maximize'

print("\nDetails:")
print(f"Function: f(x) = {expression}")
print(f"Interval: {interval}")
print(f"Accuracy: {accuracy_percentage}%")
print(f"Number of iterations: {num_iterations}")

optimal_value = find_optimal_points(interval, expression, num_iterations, maximize)  # Find optimal points
print(f"\nOptimum solution: f(x) = {optimal_value}")
