"""
 SOME NOTES WHILE WRITING CODE
- here mostly we're interested in both cell and comuted value. So don't calculate the value alone
"""

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
    
    


table = []

"""
Z = 5X + 4Y
3X + 4Y <= 78
4X + 1Y <= 36
X >= 0, Y >= 0
"""


# table1 = [ [3, 5, 1, 0, 0, 78], [4, 1, 0, 1, 0, 36], [-5, -4, 0, 0, 1, 0]]
table1 = [ [10, 20, 1, 0, 0, 120], [8, 8, 0, 1, 0, 80], [-12, -16, 0, 0, 1, 0]]

# Generalizing
tables = [table1]
optimal = False
current_iteration = 0


while not optimal:
    # table1 = [[3, 5, 1, 0, 0, 78], [4, 1, 0, 1, 0, 36], [-5, -4, 0, 0, 1, 0]]

    current_table = tables[current_iteration]
    print(current_table)
    last_row = len(current_table) - 1
    key_col = index_of_most_negative_element(current_table[last_row])
    ratios = compute_ratios(current_table, key_col)
    key_row = compute_key_row(ratios)

    print("Key col = ", key_col)
    print("Key row = ", key_row)

    key_elem = current_table[key_row][key_col]

    # creating new table for next iteration
    tables.append(current_table.copy())
    current_iteration+=1
    current_table = tables[current_iteration] # T O D O: fix the above redundant line


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
            print(row,key_col)
            print(current_table)
            for col in range(len(current_table[row])):
                val = current_table[row][col]
                elem_from_key_elems = key_elems[col]
                # print(val, multiplier, elem_from_key_elems)
                new_elem = val + (multiplier) * key_elems[col]
                # print("new elem = ", new_elem)
                current_table[row][col] = new_elem
    print(current_table)

    # checking for optimality condition
    if check_optimality_condition(current_table):
        print("The solution is optimal")
        break

print("Printing tables")
print(tables)
