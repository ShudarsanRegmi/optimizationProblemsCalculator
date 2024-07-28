import sys
import json
from utils.input_parser import parse_simplex_input
import tempfile
import pickle

"""
 SOME NOTES WHILE WRITING CODE
- here mostly we're interested in both cell and comuted value. So don't calculate the value alone
"""

# Todo: Track the Entering and leaving variables

# Rows = No. of Constraintsi + 1(Obj)
# Cols = No. of vars + NO of constraints + 1 (RHS) + 1(Obj)

# for 2d

NO_OF_VARS = 2
NO_OF_CONS = 2


rows = NO_OF_CONS + 1
cols = NO_OF_VARS + NO_OF_CONS + 2

print(" rows = {}, cols = {}".format(rows,cols))


def index_of_most_negative_element(lst):
    # Initialize the most negative number and its index
    most_negative = None
    most_negative_index = -1

    for index, num in enumerate(lst):
        if num < 0 and (most_negative is None or num < most_negative):
            most_negative = num
            most_negative_index = index
    
    if most_negative is not None:
        return most_negative_index
    else:
        return False

def compute_ratios(table,key_col):
    ratios = []

    for row in table:
        if row[key_col]<=0:
            ratios.append(-1)
        else:
            print(row[cols-1], row[key_col])
            ratio = row[cols-1] / row[key_col]
            ratios.append(ratio)
            
            

    print("Ratios = ", ratios)
    return ratios


def compute_key_row(ratios):
    maxr = ratios[0]
    maxri = 0
    for i in range(len(ratios)):
        if ratios[i]<ratios[maxri] and ratios[i] != -1:
            maxri=i
            print("max ratio index changed")
        elif ratios[i] == ratios[maxri]:
            print("ratios are matching")
        else:
            pass

    return maxri
     

def check_optimality_condition(table):
    # DOUBT: whether this is to be checked for all the eoements in the Z row or it is to be checked for only decision and slack variables
    for col in range(cols-2):
            val = table[rows-1][col]
            if val < 0:
                return False
        
    return True
        
    # check the last row of the table and check if all the values are positive


def display_solution(table, basic_variables):
    Z = table[-1][-1]
    print("Z = {}".format(Z))

    for vari, var in enumerate(basic_variables):
        if var.startswith("x"):
            print(f"{var} = {table[basic_variables.index(var)][-1]}")


    # if ("x1" in basic_variables):
    #     x1 = table[basic_variables.index("x1")][-1]
    #     print("x1 = {}".format(x1))
    #
    # if ("x2" in basic_variables):
    #     x2 = table[basic_variables.index("x2")][-1]
    #     print("x2 = {}".format(x2))

def change_basic_vars(basic_variables, key_row, key_col):
    # Todo: Generalize this logic

    # change has to be done at the index of key row
    # variable corresponding to key column is entering
    basic_variables[key_row] = f"x{key_col}"
    return basic_variables


def initial_basic_variables_column():
    initial_basic_variables = []
    while len(initial_basic_variables) != NO_OF_CONS:
        initial_basic_variables.append(f"s{len(initial_basic_variables)}")
    initial_basic_variables.append("Z")
    print(initial_basic_variables)
    return initial_basic_variables


table = []

"""
Z = 5X + 4Y
3X + 4Y <= 78
4X + 1Y <= 36
X >= 0, Y >= 0
Solution Link: https://www.emathhelp.net/en/calculators/linear-programming/simplex-method-calculator/?z=5x_1+%2B+4x_2&max=on&c=3x_1+%2B+4x_2+%3C%3D+78%0D%0A4x_1+%2B+1x_2+%3C%3D+36%0D%0Ax_1+%3E%3D+0%2C+x_2+%3E%3D+0&m=m
"""

# tablne1 = [ [3, 4, 1, 0, 0, 78], [4, 1, 0, 1, 0, 36], [-5, -4, 0, 0, 1, 0]]

# table1 = [ [3, 5, 1, 0, 0, 78], [4, 1, 0, 1, 0, 36], [-5, -4, 0, 0, 1, 0]]
# table1 = [ [10, 20, 1, 0, 0, 120], [8, 8, 0, 1, 0, 80], [-12, -16, 0, 0, 1, 0]]
# table1 = [ [1, 1, 1, 0, 0, 12], [2, 1, 0, 1, 0, 16], [-40, -30, 0, 0, 1, 0]]

# When no. of constraints = 3
# table1 = [ [2, 1, 1, 0, 0, 0, 10], [3, 3, 0, 1, 0,0, 20],[2, 4, 0, 0, 1, 0 , 20], [-20, -30, 0, 0, 0, 1, 0]]

# table1 = [ [10, 2, 1, 1, 0, 0, 0, 100], [7, 3, 2, 0, 1, 0, 0, 77], [2, 4, 1, 0, 0, 1, 0, 80], [-12, -3, -1, 0, 0, 0, 1, 0] ]

# table1 = [ [18, 28, 4, 5, -2125, 0, 0, 0, 100], [7, 3, 2, 0, 1, 0, 0, 0, 77], [2, 4, 1, 0, 0, 1, 0, 0, 80], [-12, -3, -1, 0, 0, 0, 1, 0] ]


# Todo: To check  whether a 4 and 5 variable problems is working fine or not
# Example Problem with iteratio tables : https://www.emathhelp.net/en/calculators/linear-programming/simplex-method-calculator/?z=1500x_1+%2B+2500x_2+%2B+2000x_3+%2B+3000x_4&max=on&c=20x_1+%2B+30x_2+%2B+10x_3+%2B+15x_4+-+2000x_5+%3C%3D+0%0D%0A-10x_1+%2B+5x_2+%2B+5x_3+%2B+5x_4++%3C%3D+0%0D%0A5x_1+-+15x_2+%2B+5x_3+%2B+10x_4++%3C%3D+0%0D%0A10x_1+%2B+5x_2+-+20x_3+-+20x_4++%3C%3D+0%0D%0A30x_1+%2B+40x_2+%2B+50x_3+%2B+60x_4+%2B+3x_5+%3C%3D+25000%0D%0Ax_1+%3E%3D+0%2C+x_2+%3E%3D+0%2C+x_3+%3E%3D+0%2C+x_4+%3E%3D+0%2C+x_5+%3E%3D+0&m=m
# table1 = [
#     [20, 30, 10, 15, -2000, 1, 0, 0, 0, 0, 0, 2000],  # Constraint 1
#     [-10, 5, 5, 5, 0, 0, 1, 0, 0, 0, 0, 0],            # Constraint 2
#     [5, -15, 5, 10, 0, 0, 0, 1, 0, 0, 0, 0],            # Constraint 3
#     [10, 5, -20, -20, 0, 0, 0, 0, 1, 0, 0, 0],          # Constraint 4
#     [30, 40, 50, 60, 3, 0, 0, 0, 0, 0, 0, 25000],       # Constraint 5
#     [-1500, -2500, -2000, -3000, 0, 0, 0, 0, 0, 0, 1, 0] # Objective function Z
# ]
    # # Columns:  [ x1,    x2,    x3,    x4,     x5,    s1,  slack1, slack2, slack3, slack4, Z,    RHS]
#     table1 = [
#         [18,    28,    4,   5,        -2125,   1,    0,    0,      0,      0,      0,   0,    0],   # Constraint 1
#         [0,     0,     0,     0,      1,       0,   1,     0,      0,      0,      0,   0,  300],   # Constraint 2
#         [-0.8,  0.2,   0.2,   0.2,    0,       0,   0,     1,      0,      0,      0,   0,    0],   # Constraint 3
#         [0.1,  -0.9,   0.1,   0.1,    0,       0,   0,     0,      1,      0,      0,   0,    0],   # Constraint 4
#         [0.25,  0.25, -0.75, -0.75,   0,       0,   0,     0,      0,      1,      0,   0,    0],   # Constraint 5
#         [50,    70,   130,   160,     2,       0,   0,     0,      0,      0,      1,   0, 15000],  # Constraint 6
#         [-1000, -1900, -2700, -3400,  0,       0,   0,     0,      0,      0,      0,   1,    0]    # Objective function Z
#     ]


# table1 = [ [3, 5, 1, 0, 0, 78], [4, 1, 0, 1, 0, 36], [-5, -4, 0, 0, 1, 0]]
# if __name__ == "__main__":


# input_file = sys.argv[1]
# with open(input_file, 'r') as f:
#     data = json.load(f)

# json parser
# Example JSON input
# json_input = '{"objective": [5.0, 4.0], "constraints": [[3.0, 4.0, 78.0], [4.0, 1.0, 36.0]]}'

# Parse the input

def main(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    data_str = json.dumps(data)
    print(data_str)
    print("Printing table1")
    table1 = parse_simplex_input(data_str)
    print(table1)

    basic_variables = initial_basic_variables_column()
    tables = [table1]
    optimal = False
    current_iteration = 0

    while not optimal:
        current_table = tables[current_iteration]
        print(current_table)
        last_row = len(current_table) - 1
        key_col = index_of_most_negative_element(current_table[last_row])
        ratios = compute_ratios(current_table, key_col)
        key_row = compute_key_row(ratios)

        print("Key col = ", key_col)
        print("Key row = ", key_row)

        basic_variables = change_basic_vars(basic_variables, key_row, key_col)
        print("basic variables changed")
        print(basic_variables)

        key_elem = current_table[key_row][key_col]

        tables.append(current_table.copy())
        current_iteration += 1
        current_table = tables[current_iteration]

        key_elems = [elem / key_elem for elem in current_table[key_row]]

        print("After key row operation = ", key_elems)
        for row in range(len(current_table)):
            if row == key_row:
                current_table[row] = key_elems
                print("skipping, key row")
                continue
            else:
                print("not key row")
                multiplier = -(current_table[row][key_col])
                print("Multipler for this iteration = ", multiplier)
                print(row, key_col)
                print(current_table)
                for col in range(len(current_table[row])):
                    val = current_table[row][col]
                    elem_from_key_elems = key_elems[col]
                    new_elem = val + (multiplier) * key_elems[col]
                    current_table[row][col] = new_elem
        print(current_table)

        if check_optimality_condition(current_table):
            print("The solution is optimal")
            break

    print("Printing tables")
    print(tables)
    print(basic_variables)
    print(tables[-1])
    display_solution(tables[-1], basic_variables)

    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_file:
        pickle.dump(tables, temp_file)
        temp_filename = temp_file.name

    return temp_filename

#
# if __name__ == "__main__":
#     if sys.argc == 0:
#         pass
#     else:
#         input_file = sys.argv[1]
#         temp_filename = main(input_file)
#         print(f"Data has been written to temporary file: {temp_filename}")
#
