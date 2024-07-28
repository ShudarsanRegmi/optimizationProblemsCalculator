import json

def parse_simplex_input(json_input):
    # Load data from JSON input
    data = json.loads(json_input)

    num_variables = data['num_of_vars']
    num_constraints = data['num_of_cons']

    # Initialize the table
    table = []

    # Add constraints to the table with slack variables
    for i in range(num_constraints):
        constraint = data['constraints'][i]
        row = constraint[:-1]  # Take all elements except the last one (RHS)
        row += [1 if j == i else 0 for j in range(num_constraints)]  # Add slack variables
        row.append(0)  # Z column
        row.append(constraint[-1])  # RHS
        table.append(row)

    # Add objective function to the table
    objective = [-coef for coef in data['objective']] + [0] * num_constraints + [1, 0]
    table.append(objective)

    print("The table is being printed by input_parser")
    print(table)
    return table

# Example usage
# json_input = '{"num_of_vars": 2, "num_of_cons": 2, "objective": [4.0, 4.0], "constraints": [[3.0, 4.0, 78.0], [4.0, 1.0, 36.0]]}'
# parse_simplex_input(json_input)
