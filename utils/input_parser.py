import json

def parse_simplex_input(json_input):
    # Load data from JSON input
    data = json.loads(json_input)

    num_variables = len(data['objective'])
    num_constraints = len(data['constraints'])

    # Initialize the table
    table = []

    # Add constraints to the table with slack variables
    for i in range(num_constraints):
        constraint = data['constraints'][i]
        row = constraint[:-1] + [0] * num_constraints + [constraint[-1]]
        row[num_variables + i] = 1
        table.append(row)

    # Add objective function to the table
    objective = [-coef for coef in data['objective']] + [0] * (num_constraints + 1)
    table.append(objective)

    return table
