import math

def golden_section_search(f, a, b, find_min=True, tol=1e-5):
    golden_ratio = 0.618

    # Modify the function for finding maximum
    if not find_min:
        def f_neg(x):
            return -f(x)
        target_function = f_neg
    else:
        target_function = f

    # Initial points
    x1 = round(b - golden_ratio * (b - a), 4)
    x2 = round(a + golden_ratio * (b - a), 4)

    f1, f2 = target_function(x1), target_function(x2)

    while abs(b - a) > tol:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = round(b - golden_ratio * (b - a), 3)
            f1 = target_function(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = round(a + golden_ratio * (b - a), 3)
            f2 = target_function(x2)

    result = round((a + b) / 2, 3)
    return result

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    choice = input("Do you want to find the minimum or maximum? (min/max): ").strip().lower()
    find_min = (choice == "min")

    print("If you want to enter a trigonometric function, use 'math.sin(x)' format, or 'x**2' for simple expressions.")
    
    func_str = input("Enter the function of x: ")

    # Securely evaluate the function input, with math functions allowed
    f = eval(f"lambda x: {func_str}", {"math": math})

    a = get_numeric_input("Enter the lower bound of the range (a): ")
    b = get_numeric_input("Enter the upper bound of the range (b): ")
    tol = get_numeric_input("Enter the tolerance: ")

    result = golden_section_search(f, a, b, find_min=find_min, tol=tol)
    print(f"The {'minimum' if find_min else 'maximum'} is at x = {result}")
