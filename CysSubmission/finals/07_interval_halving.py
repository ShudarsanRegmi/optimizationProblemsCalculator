import math

def compute_expression(expr, x_val):
    allowed_symbols = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "sqrt": math.sqrt,
        "exp": math.exp,
        "x": x_val
    }

    try:
        result = eval(expr, {"_builtins_": None}, allowed_symbols)
    except Exception as e:
        print(f"Error computing expression: {e}")
        result = None

    return result

def interval_halving(interval_range, expr, total_iters, maximize):
    curr_range = interval_range
    best_x_val = None
    best_fn_val = None

    for iteration in range(1, total_iters + 1):
        mid_point = (curr_range[0] + curr_range[1]) / 2
        left_mid = (curr_range[0] + mid_point) / 2
        right_mid = (mid_point + curr_range[1]) / 2

        fn_mid = compute_expression(expr, mid_point)
        fn_left = compute_expression(expr, left_mid)
        fn_right = compute_expression(expr, right_mid)

        if fn_mid is None or fn_left is None or fn_right is None:
            print("Error in function evaluation.")
            return None, None

        # Use x0, x1, x2 and f(x0), f(x1), f(x2) in output
        print(f"\nIteration {iteration}:")
        print(f"x0 = {left_mid}, f(x0) = {fn_left}")
        print(f"x1 = {mid_point}, f(x1) = {fn_mid}")
        print(f"x2 = {right_mid}, f(x2) = {fn_right}")

        if maximize:
            if best_fn_val is None or fn_mid > best_fn_val:
                best_x_val = mid_point
                best_fn_val = fn_mid
            if fn_right < fn_mid < fn_left:
                curr_range[1] = mid_point
            elif fn_left < fn_mid < fn_right:
                curr_range[0] = mid_point
            else:
                curr_range = [left_mid, right_mid]
        else:
            if best_fn_val is None or fn_mid < best_fn_val:
                best_x_val = mid_point
                best_fn_val = fn_mid
            if fn_right > fn_mid > fn_left:
                curr_range[1] = mid_point
            elif fn_left > fn_mid > fn_right:
                curr_range[0] = mid_point
            else:
                curr_range = [left_mid, right_mid]

    return best_x_val, best_fn_val

def input_interval():
    print("\nPlease provide the interval range.")
    lower_limit = float(input("Enter the lower limit of the interval: "))
    upper_limit = float(input("Enter the upper limit of the interval: "))
    return [lower_limit, upper_limit]

def calculate_iterations(tolerance):
    log_ratio = math.log(tolerance) / math.log(0.5)
    estimated_iters = math.ceil((log_ratio + 0.25) / 0.5)
    return estimated_iters

def filter_odd_iters(count):
    odd_iter_list = [i for i in range(3, count + 1) if i % 2 != 0]
    return len(odd_iter_list)

# Main program execution
print("\nWelcome to the Interval Halving Method Solver!")

user_expr = input("\nPlease enter the mathematical expression for f(x) (e.g., x**2 + 3*x + 2): ")

interval_bounds = input_interval()

accuracy = float(input("\nEnter the accuracy tolerance in percentage : ")) / 100

total_iterations = filter_odd_iters(calculate_iterations(accuracy))

maximize_choice = input("\nWould you like to maximize or minimize the function? (Type 'max' for maximize, 'min' for minimize): ").strip().lower()
maximize_fn = maximize_choice == 'max'

print("\nSummary of Inputs:")
print(f"Expression: f(x) = {user_expr}")
print(f"Interval: [{interval_bounds[0]}, {interval_bounds[1]}]")
print(f"Accuracy: {accuracy * 100}%")
print(f"Estimated number of iterations: {total_iterations}")

optimal_x, optimal_fn_val = interval_halving(interval_bounds, user_expr, total_iterations, maximize_fn)

print(f"\nOptimal solution found:")
print(f"x = {optimal_x}, f(x) = {optimal_fn_val}")
