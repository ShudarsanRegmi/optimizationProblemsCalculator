import streamlit as st
import numpy as np
import pandas as pd
import subprocess
import json


# Function to call your simplex.py script
def call_simplex(data):
    # Save the data to a json file
    with open('simplex_input.json', 'w') as f:
        json.dump(data, f)

    # Call the simplex.py script
    result = subprocess.run(['python', 'simplex.py', 'simplex_input.json'], capture_output=True, text=True)
    return result.stdout


st.title("Linear Programming Calculator")

# Input: Number of Variables and Constraints
num_variables = st.number_input('Number of Variables', min_value=1, step=1)
num_constraints = st.number_input('Number of Constraints', min_value=1, step=1)

if num_variables > 0 and num_constraints > 0:
    st.subheader("Objective Function Coefficients")
    objective = []
    for i in range(num_variables):
        coeff = st.number_input(f'Coefficient for x{i + 1}', key=f'obj_{i}')
        objective.append(coeff)

    st.subheader("Constraints")
    constraints = []
    for i in range(num_constraints):
        st.write(f'Constraint {i + 1}')
        constraint = []
        for j in range(num_variables):
            coeff = st.number_input(f'Coefficient for x{j + 1} in Constraint {i + 1}', key=f'con_{i}_{j}')
            constraint.append(coeff)
        rhs = st.number_input(f'Right-hand side for Constraint {i + 1}', key=f'rhs_{i}')
        constraint.append(rhs)
        constraints.append(constraint)

    if st.button('Calculate'):
        # Prepare data for simplex.py
        data = {
            'objective': objective,
            'constraints': constraints
        }
        result = call_simplex(data)
        st.subheader("Result")
        st.write(result)