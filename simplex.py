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
     



table = []

"""
Z = 5X + 4Y
3X + 4Y <= 78
4X + 1Y <= 36
X >= 0, Y >= 0
"""


table = [ [3, 5, 1, 0, 0, 78], [4, 1, 0, 1, 0, 36], [-5, -4, 0, 0, 1, 0]]

last_row = len(table)-1

key_col = index_of_most_negative_element(table[last_row])

print("Key col = ", key_col)

# find the key column

ratios = compute_ratios(table, key_col)


key_row = compute_key_row(ratios)

print("Key row = ", key_row)


# Now in next table teh keyrow should be divided by key element

key_elem = table[key_row][key_col]

table2 = table.copy() 
print(table)

# for i in range(cols):
#     elem = table2[key_row][i]
#     table2[key_row][i] = elem / key_elem  

# print(table2)

key_elems = [elem/key_elem for elem in table2[key_row]] 

print("After key row operation = ", key_elems)
for row in range(len(table2)):
    if row == key_row:
        table2[row] = key_elems
        print("skipping, key row")
        continue
    else:
        print("not key row")
        multiplier = -table2[row][key_col]
        for col in range(len(table2[row])):
            val = table2[row][col]
            elem_from_key_elems = key_elems[col]
            # print(val, multiplier, elem_from_key_elems)
            new_elem =  val + (multiplier)*key_elems[col]
            # print("new elem = ", new_elem)
            table2[row][col] = new_elem 
print(table2)


