import sympy as sp
from sympy.utilities.lambdify import lambdify

def simplex_method(f, list_of_vertices):
    store_values = []
    removed_vertices = [] # main problem was here every time when you the recursion call the function the removed_vertcies list will get empty and it will always contain last removed vertces
    for vertex in list_of_vertices: # modifeid to make simple
        f_x = f(vertex[0], vertex[1])
        store_values.append(f_x)
    
    print("Function values at vertices:", store_values)
    max_f_x = max(store_values)
    print("Maximum function value:", max_f_x)

    # Remove the vertex with the maximum function value
    for vertex in list(list_of_vertices):  
        f_x = f(vertex[0], vertex[1])
        if f_x == max_f_x:
            removed_vertices.append(vertex)
            list_of_vertices.remove(vertex)
            break # apply break to terminate the loop

    if len(list_of_vertices) == 2:
        add_new_x = (list_of_vertices[0][0] + list_of_vertices[1][0] - removed_vertices[0][0])
        add_new_y = (list_of_vertices[0][1] + list_of_vertices[1][1] - removed_vertices[0][1])
        list_of_vertices.append([add_new_x, add_new_y])
        
    if len(removed_of_vertices)>0:
        for vertex in removed_vertices:
            if (f(vertex[0], f(vertex[1]) == max_f_x):
                mean_x1 = (list_of_vertices[0][0] + list_of_vertices[1][0]) / 2
                mean_x2 = (list_of_vertices[0][1] + list_of_vertices[1][1]) / 2
                return mean_x1, mean_x2
    
    return simplex_method(f,list_of_vertices)

# Input for the objective function
func = input("Enter the objective function (e.g., 3*x1 + 2*x2): ")
x1, x2 = sp.symbols('x1 x2')
expr = sp.sympify(func)
f = lambdify((x1, x2), expr)

# Input for the vertices
list_of_vertices = []
print("Enter the three vertices:")
for i in range(3):
    vertex = list(map(float, input(f"Enter vertex {i + 1} (e.g., 1 2): ").split()))
    list_of_vertices.append(vertex)

print("Initial list of vertices:", list_of_vertices)

# Call the simplex method function
min_x,min_y = simplex_method(f, list_of_vertices)

print(f"The optimal point is: {min_x, min_y} and the value is {f(min_x, min_y)}")
