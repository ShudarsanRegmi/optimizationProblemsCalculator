import sympy as sp

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
        return n+1


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
print("\n")

for i in range(1,ittetration+1):
    print("a =", a)
    print("b =", b)
    l0= b-a
    x2 = a+(0.618)*l0
    x1 = (a+b)-x2
    f_x1_eqn = f_expr.subs({x:x1})
    f_x1 = sp.simplify(f_x1_eqn)

    f_x2_eqn = f_expr.subs({x:x2})
    f_x2 = sp.simplify(f_x2_eqn)

    print("x1 : ", x1)
    print("x2 : ", x2)
    print("f(x1) : ", f_x1)
    print("f(x2) : ", f_x2)
    if(x1<=x2 and (ittetration-i)>0):
        if(f_x1>=f_x2):
            a=x1
            print("Eliminating a \nPreserving b ")
        else:
            b=x2
            print("Eliminating b \nPreserving a ")
    print("\n")
print("a =", a)
print("b =", b)
optimal_point = (a+b)/2
optimal_eqn = f_expr.subs({x:optimal_point})
optimal_value = sp.simplify(optimal_eqn)
print("The Optimal Point is :", optimal_point, "\nAnd The Optimal Value is: ", optimal_value)
