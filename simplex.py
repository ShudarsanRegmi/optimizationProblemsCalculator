"""
 SOME NOTES WHILE WRITING CODE
- here mostly we're interested in both cell and comuted value. So don't calculate the value alone
"""

# Rows = No. of Constraintsi + 1(Obj)
# Cols = No. of vars + NO of constraints + 1 (RHS)

# for 2d



NO_OF_VARS = 2
NO_OF_CONS = 2


rows = NO_OF_CONS + 1
cols = NO_OF_VARS + NO_OF_CONS + 1


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

def compute_ratios(table,key_row):
    ratios = []
    # rhs = [ i[cols-1] for i in table]
    # ratios = [ i[cols-1]/i[key_row] for i in table]

    for i in table:
        if i[key_row]<=0:
            ratios.append(-1)
        else:
            ratio = i[cols-1] / i[key_row]
            ratios.append(ratio)
            
            

    print(ratios)
    return ratios

    
def compute_key_column(ratios):
    maxr = ratios[0]
    maxri = 0
    for i in range(len(ratios)):
        if ratios[i]>ratios[maxri]:
            maxri=i

    return maxri
     



table = []

"""
Z = 5X + 4Y
3X + 4Y <= 78
4X + 1Y <= 36
X >= 0, Y >= 0
"""


table = [ [3, 4, 1, 0,78], [4, 1, 0, 1, 36], [-5, -4, 0, 0, 1]]

last_row = len(table)-1

key_row = index_of_most_negative_element(table[last_row])

print("Key row = ", key_row)

# find the key column

ratios = compute_ratios(table, key_row)


key_column = compute_key_column(ratios)

print("Key Column = ", key_column)



