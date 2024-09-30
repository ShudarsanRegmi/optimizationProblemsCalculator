#Example 1
#Equation: x**3 + x - 1
#First guess: 0
#Second guess: 1
#Tolerance: 0.0001
#Output:Root of the given equation = 0.682328
#No. of iterations = 6


#Example 2:
#Equation: math.sin(x) - 0.5 
#First guess: 0
#Second guess: 1
#Tolerance: 0.0001
#Output:Root of the given equation = 0.523598
#No. of iterations = 6


import math

def f(x, equation):
    return eval(equation)

def secant(x1, x2, E, equation):
    n = 0
    xm = 0
    x0 = 0
    c = 0
    if f(x1, equation) * f(x2, equation) < 0:
        while True:

            x0 = ((x1 * f(x2, equation) - x2 * f(x1, equation)) /
                  (f(x2, equation) - f(x1, equation)))


            c = f(x1, equation) * f(x0, equation)


            x1 = x2
            x2 = x0


            n += 1


            if c == 0:
                break

            xm = ((x1 * f(x2, equation) - x2 * f(x1, equation)) /
                  (f(x2, equation) - f(x1, equation)))


            if abs(xm - x0) < E:
                break

        print("Root of the given equation =", round(x0, 6))
        print("No. of iterations =", n)
    else:
        print("Cannot find a root in the given interval")

equation = input("Enter the equation : ")
x1 = float(input("Enter the first guess: "))
x2 = float(input("Enter the second guess: "))
E = float(input("Enter the tolerance level: "))

secant(x1, x2, E, equation)
