import sympy as sp
from tabulate import tabulate

#Defing function to calculate the index of fibbonacci series from series value.
def index_value_of_fib_series(series_value):
    if(series_value==1):
        return 0
    elif(series_value==2):
        return 2
    else:
        f0 = 1
        f1 = 1
        f2 = f1+f0
        n=2
        while(f2<series_value):
            f0=f1
            f1=f2
            f2=f0+f1
            n=n+1
        return n


#Defing function to generate List of fibbonacci series upto series value.
def generate_fibonacci(index_of_fib_series):

    fib_list = [0] * (index_of_fib_series + 1)
    
    # Handling the base cases
    if index_of_fib_series >= 1:
        fib_list[0] = 1
    if index_of_fib_series >= 2:
        fib_list[1] = 1
    
    # Filling the list with Fibonacci numbers
    for i in range(2, index_of_fib_series + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    
    return fib_list

def fib_Array(n):
    fib_array = generate_fibonacci(ittetration)
    return fib_array[n]

# Define the symbols
x = sp.symbols('x')

# Input function from user
f_expr_input = input("Enter the function containing x variables only: ")
f_expr = sp.sympify(f_expr_input)

# Get initial points and and Precision Percentage
a, b = map(float, input("Enter the value of initial point (comma-separated): ").strip().split(','))

# output precision percentage means, the output will lie between interval of that percentage of exact output.
percentage = float(input("Enter the output Precision Percentage: ")) 


series_value = 100/(2*percentage)
ittetration = index_value_of_fib_series(series_value)
# ittetration = 7

print("Given,")
print("Initial Point: (",a,",",b,")")
print("Precision Percentage(%) = ", percentage)
print("No. Of Itteration Needed: ",ittetration)
print("\n")
l0= b-a

# List to store results for table display
table_data = []

for i in range(2,ittetration+1):
    if(ittetration-i>=0):
        ittetrations = i-1
        l_star = (fib_Array(ittetration-i)/fib_Array(ittetration))*l0
        x2 = b-l_star
        x1 = a+l_star
        f_x1_eqn = f_expr.subs({x:x1})
        f_x1 = sp.simplify(f_x1_eqn)

        f_x2_eqn = f_expr.subs({x:x2})
        f_x2 = sp.simplify(f_x2_eqn)

        if(f_x1<=f_x2):
            result = "L"
        else:
            result= "R"

        table_data.append([ittetrations, l_star,a, b, x1, x2, f_x1, f_x2, result])
        if(x1<=x2):
            if(f_x1==f_x2):
                a=x1
                b=x2
                break
            elif(f_x1>f_x2):
                a=x1
            else:
                b=x2
        else:
            if(f_x1<f_x2):
                a=x1
            else:
                b=x2
optimal_point = (a+b)/2
optimal_eqn = f_expr.subs({x:optimal_point})
optimal_value = sp.simplify(optimal_eqn)

# Print the table
headers = ["Itterations","L*[f(n-i)/fn]","a", "b", "x1", "x2", "f(x1)", "f(x2)","L/R"]
print(tabulate(table_data, headers, tablefmt="grid"))

# Print the optimal point and value
print("The Optimal Point is :", optimal_point, "\nAnd The Optimal Value is: ", optimal_value)
