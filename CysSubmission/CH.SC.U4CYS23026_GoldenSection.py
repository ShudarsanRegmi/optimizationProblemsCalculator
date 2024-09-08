import math
phi = (1 + math.sqrt(5)) / 2

def get_function():
    func_str = input("Enter the function of x to optimize (use 'x' as the variable):\n")
    return lambda x: eval(func_str)

def golden_section_search(func, a, b, tol, find_max=False):
    iter_count = 0

    while True:
        c = b - (b - a) / phi
        d = a + (b - a) / phi
        if find_max:
            if func(c) > func(d):
                b = d  
            else:
                a = c  
        else:
            if func(c) < func(d):
                b = d  
            else:
                a = c  
        print(f"Iteration {iter_count}: a = {a}, b = {b}, interval length = {b - a}")
        if abs(b - a) < tol:
            result = (b + a) / 2
            if find_max:
                print(f"Converged to maximum at x = {result}")
            else:
                print(f"Converged to minimum at x = {result}")
            break

        iter_count += 1
        
        keep_going = input("Continue iterating? (y/n): ").strip().lower()
        if keep_going == 'n':
            break

if __name__ == "__main__":
    f = get_function()
    a = float(input("Enter the lower bound a: "))
    b = float(input("Enter the upper bound b: "))
    tol = float(input("Enter the tolerance level for stopping (e.g., 0.001): "))
    option = input("Find minimum or maximum? (min/max): ").strip().lower()
    golden_section_search(f, a, b, tol, find_max=(option == 'max'))
