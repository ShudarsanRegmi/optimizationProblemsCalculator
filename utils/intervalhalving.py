import math

def evaluate_polynomial(coefficients, x): #to find f(x)
    result = 0
    degree = len(coefficients) - 1
    for i, coeff in enumerate(coefficients):
        result += coeff * (x ** (degree - i))
    return result

def graph_points(interval, coefficients, iterations): #to find the new intervals
    temp = interval
    for it in range(1, iterations + 1):
        x0 = (temp[0] + temp[1]) / 2
        x1 = (temp[0] + x0) / 2
        x2 = (x0 + temp[1]) / 2

        y0 = evaluate_polynomial(coefficients, x0)
        y1 = evaluate_polynomial(coefficients, x1)
        y2 = evaluate_polynomial(coefficients, x2)

        print(f"\nFor iteration {it}:\n")
        print(f"x1 = {x1}, f(x1) = {y1}")
        print(f"x0 = {x0}, f(x0) = {y0}")
        print(f"x2 = {x2}, f(x2) = {y2}")

        if y2 > y0 and y0 > y1:
            temp[1] = x0
        elif y1 > y0 and y0 > y2:
            temp[0] = x0
        elif y1 > y0 and y2 > y0:
            temp = [x1, x2]


    temp = [x1, x2]
    return y0,temp

def graph_intervals():   #to assign the initial interval
    lst = []
    for i in range(2):
        n = float(input(f"Enter the interval {i + 1}: "))
        lst.append(n)
    return lst

def find_n(con): #to find n
    l1 = math.log(con) / math.log(0.5)
    l2 = l1 + 0.25
    x = l2 / 0.5
    x = math.ceil(x)
    return x

def no_of_iterations(n):  #to find no.of iterations
    it = []
    if(n%2==0):
        for i in range(3, n):
            if i % 2 != 0:
                it.append(i)
    else:
        for i in range(3, n+1):
            if i % 2 != 0:
                it.append(i)

    print(it)
    length_it = len(it)
    return length_it

print("\n\t\t************ WELCOME TO INTERVAL HALVING/BISECTION METHOD ************\n")

deg = int(input("Enter the degree of the f(x) equation: "))

x = []
for i in range(deg + 1):
    c = float(input(f"Enter the coefficient of x^{deg - i}: "))
    x.append(c)

polynomial = ""
for i in range(deg + 1):
    if i == deg:
        polynomial += f"({x[i]})"
    else:
        polynomial += f"({x[i]})x^{deg - i} + "

interval = graph_intervals()  # graph_intervals function call

L0 = interval[1] - interval[0]

per = float(input("Enter the accuracy in percentage: "))
con = per / 100

n = find_n(con)  # To find the value of n
iterations = no_of_iterations(n)  # To find number of iterations

print("\nThe details given in question are:")
print(f"\nThe function: f(x) = {polynomial}")
print("Interval: ", interval)
print(f"Accuracy: {per}%")
print("No. of iterations: ", iterations)

soln,reg = graph_points(interval, x, iterations)  # function call for finding new intervals
print(f"\nThe solution for the given question is: {soln} at interval {reg}")
