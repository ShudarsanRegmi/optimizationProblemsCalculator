#test case 1: f(x): x**3-6*x**2+4*x+12 ... optimum solution: f(x)= -4
#test case 2:  f(x): 0.4*x**3-6*x*sin(x) ...optimum solution: f(x)= -8.188102442176337 

#code goes here... 

import math

def evaluate_function(expression, x):
    # Safely evaluate the function for a given x
    allowed_names = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "sqrt": math.sqrt,
        "exp": math.exp,
        "x": x
    }

    try:
        result = eval(expression, {"__builtins__": None}, allowed_names)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        result = None

    return result

def graph_points(interval, expression, iterations, maximize):
    temp = interval
    for it in range(1, iterations + 1):
        x0 = (temp[0] + temp[1]) / 2
        x1 = (temp[0] + x0) / 2
        x2 = (x0 + temp[1]) / 2

        y0 = evaluate_function(expression, x0)
        y1 = evaluate_function(expression, x1)
        y2 = evaluate_function(expression, x2)

        if y0 is None or y1 is None or y2 is None:
            print("Error in evaluating function at one or more points.")
            return None

        print(f"\nFor iteration {it}:\n")
        print(f"x1 = {x1}, f(x1) = {y1}")
        print(f"x0 = {x0}, f(x0) = {y0}")
        print(f"x2 = {x2}, f(x2) = {y2}")

        if maximize:
            if y2 < y0 and y0 < y1:
                temp[1] = x0
            elif y1 < y0 and y0 < y2:
                temp[0] = x0
            elif y1 < y0 and y2 < y0:
                temp = [x1, x2]
        else:
            if y2 > y0 and y0 > y1:
                temp[1] = x0
            elif y1 > y0 and y0 > y2:
                temp[0] = x0
            elif y1 > y0 and y2 > y0:
                temp = [x1, x2]

    temp = [x1, x2]
    return y0

def graph_intervals():
    lst = []
    for i in range(2):
        n = float(input(f"Enter the interval {i + 1}: "))
        lst.append(n)
    return lst

def find_n(con):
    l1 = math.log(con) / math.log(0.5)
    l2 = l1 + 0.25
    x = l2 / 0.5
    x = math.ceil(x)
    return x

def no_of_iterations(n):
    it = []
    if n % 2 == 0:
        for i in range(3, n):
            if i % 2 != 0:
                it.append(i)
    else:
        for i in range(3, n + 1):
            if i % 2 != 0:
                it.append(i)

    length_it = len(it)
    return length_it

print("\n\t\t************ WELCOME TO INTERVAL HALVING/BISECTION METHOD ************\n")

expression = input("Enter the function f(x): ")

interval = graph_intervals()  # graph_intervals function call

L0 = interval[1] - interval[0]

per = float(input("Enter the accuracy in percentage: "))
con = per / 100

n = find_n(con)  # To find the value of n
iterations = no_of_iterations(n)  # To find number of iterations

# Prompt user to choose between maximization or minimization
choice = input("Do you want to maximize or minimize the function? Enter 'maximize' or 'minimize': ").strip().lower()
maximize = choice == 'maximize'

print("\nThe details given in question are:")
print(f"\nThe function: f(x) = {expression}")
print("Interval: ", interval)
print(f"Accuracy: {per}%")
print("No. of iterations: ", iterations)

soln = graph_points(interval, expression, iterations, maximize)  # function call for finding new intervals
print(f"\noptimum solution: f(x)= {soln} ")
