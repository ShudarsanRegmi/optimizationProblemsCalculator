import streamlit as st
import pandas as pd
import sympy as sp
from tabulate import tabulate

st.write("# Golden Search Method Calculator")

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
data = st.text_input("Enter the function (e.g., x**2 + 3*x + 2):", "x**2 + 3*x + 2")
f_expr_input = data.strip()
if f_expr_input:
    try:
        f_expr = sp.sympify(f_expr_input)
    except (sp.SympifyError, SyntaxError) as e:
        st.error(f"Error in input: {e}")
        st.stop()  # Stop execution if input is invalid
else:
    st.warning("Please enter a valid equation.")
    st.stop()  # Stop execution if input is empty

# Get initial points and and Precision Percentage
col1, col2, col3 = st.columns(3)
a=col1.number_input("Enter Initial Point", value=0)
b=col2.number_input("Enter Final Point", value=1)

# output precision percentage means, the output will lie between interval of that percentage of exact output.
percentage=col3.number_input("Enter the Initial Point", value=1.0, min_value=0.1)


series_value = 100/(2*percentage)
ittetration = index_value_of_fib_series(series_value)

st.write(" ")
st.write("#### Solution,")
st.write("Given,")
st.write("Initial Point: (", a, ",", b, ")")
st.write("Precision Percentage(%) = ", percentage)

# List to store results for table display
table_data = []

for i in range(1,ittetration+1):
    ittetrations = i
    l0= b-a
    x2 = a+(0.618)*l0
    x1 = (a+b)-x2
    f_x1_eqn = f_expr.subs({x:x1})
    f_x1 = sp.simplify(f_x1_eqn)

    f_x2_eqn = f_expr.subs({x:x2})
    f_x2 = sp.simplify(f_x2_eqn)

    if(x1<=x2 and (ittetration-i)>0):
        if(f_x1>=f_x2):
            a=x1
            leftOrRight = "R"
            # print("Eliminating a \nPreserving b ")
        else:
            b=x2
            leftOrRight = "L"
            # print("Eliminating b \nPreserving a ")
    table_data.append([ittetrations, a, b, x1, x2, f_x1, f_x2, leftOrRight])
optimal_point = (a+b)/2
optimal_eqn = f_expr.subs({x:optimal_point})
optimal_value = sp.simplify(optimal_eqn)

# Print the table
# Convert to a DataFrame for better handling
df = pd.DataFrame(table_data, columns=["Iterations", "a", "b", "x1", "x2", "f(x1)", "f(x2)", "L/R"])

# Format the numbers to 2 decimal places
df = df.round(2)

# Display the formatted table in the Streamlit app
st.write(df)

# Print the optimal point and value
st.write("The Optimal Point is :", optimal_point, "\nAnd The Optimal Value is: ", optimal_value)
