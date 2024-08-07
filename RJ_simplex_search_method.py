import sympy as sp
from sympy.utilities.lambdify import lambdify
import math

def print_table(headers, data):
    # Find the maximum length of each column for formatting
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data, headers)]
    format_str = ' '.join([f"{{:<{w}}}" for w in col_widths])

    # Print the headers
    print(format_str.format(*headers))
    print('-' * (sum(col_widths) + len(headers) - 1))

    # Print the data rows
    for row in data:
        print(format_str.format(*row))


def simplex_method(f, list_of_vertices):
    iteration = 0
    removed_vertices = []
    all_vertices = list_of_vertices.copy()  # To store all vertices including newly generated ones
    derived_vertices = []
    while True:
        store_values = []

        # Evaluate function at each vertex
        for i in range(len(list_of_vertices)):
            f_x = float(f(list_of_vertices[i][0], list_of_vertices[i][1]))  # Ensure f_x is a float
            store_values.append(f_x)

        # Prepare data for table
        headers = ['Vertex', 'Function Value']
        data = [
            [f"({v[0]:.2f}, {v[1]:.2f})", f"{store_values[i]:.2f}"]
            for i, v in enumerate(list_of_vertices)
        ]

        print(f"\nIteration {iteration}")
        print_table(headers, data)

        # Find the maximum function value
        max_f_x = max(store_values)
        print(f"Maximum function value: {max_f_x:.2f}")

        # Remove the vertex with the maximum function value
        for j in range(len(list_of_vertices) - 1, -1, -1):  # Iterate in reverse order
            f_x = float(f(list_of_vertices[j][0], list_of_vertices[j][1]))  # Ensure f_x is a float
            if f_x == max_f_x:
                removed_vertices.append(list_of_vertices[j])
                vertex = list_of_vertices.pop(j)  # Remove vertex at index j
                # if this maximum yielding vertex is the derived vertex then terminate
                if vertex in derived_vertices:
                    print("Terminating...")
                    print(vertex)
                    mean_x = (list_of_vertices[0][0] + list_of_vertices[1][0]) / 2
                    mean_y = (list_of_vertices[0][1] + list_of_vertices[1][1]) / 2
                    final_value = float(f(mean_x, mean_y))  # Ensure final_value is a float
                    print(f"Termination Point: ({mean_x:.2f}, {mean_y:.2f}) with functional value {final_value:.2f}")
                    return
                break

                # Add a new vertex based on the remaining vertices
        if len(list_of_vertices) == 2:
            add_new_x = (list_of_vertices[0][0] + list_of_vertices[1][0] - removed_vertices[-1][0])
            add_new_y = (list_of_vertices[0][1] + list_of_vertices[1][1] - removed_vertices[-1][1])
            new_vertex = [add_new_x, add_new_y]

            derived_vertices.append(new_vertex)

            

            list_of_vertices.append(new_vertex)
            all_vertices.append(new_vertex)
            print(f"Added new vertex: ({new_vertex[0]:.2f}, {new_vertex[1]:.2f})")

        iteration += 1

    # Final table
    print("\nFinal list of vertices:")
    final_data = [
        [f"({v[0]:.2f}, {v[1]:.2f})", f"{float(f(v[0], v[1])):.2f}"]  # Ensure all final values are floats
        for v in list_of_vertices
    ]
    print_table(headers, final_data)

    if list_of_vertices:
        min_value = min(float(f(v[0], v[1])) for v in list_of_vertices)  # Ensure min_value is a float
        print(f"Minimum value found: {min_value:.2f}")
    else:
        print("No vertices left.")


# Input for the objective function
func = input("Enter the objective function (e.g., 3*x1 + 2*x2): ")
x1, x2 = sp.symbols('x1 x2')
expr = sp.sympify(func)
f = lambdify((x1, x2), expr)

# Input for the vertices
list_of_vertices = []
var=int(input("Enter the no of vertices max(3):"))
if var==2:
    print("Enter the two variable  on that must be on same line(ex: (2.5,4) (2.5,6)")
    for i in range(var):
        vertex = list(map(float, input(f"Enter vertex {i + 1} (e.g., 1 2): ").split()))
        list_of_vertices.append(vertex)
    small_y_coor=list_of_vertices[0][1] if list_of_vertices[0][1] <list_of_vertices[1][1] else list_of_vertices[1][1]
    large_y_coor=list_of_vertices[0][1] if list_of_vertices[0][1] >list_of_vertices[1][1] else list_of_vertices[1][1]
    
    y_coord=small_y_coor+(list_of_vertices[1][1]-list_of_vertices[0][1])/2
    x_coord=list_of_vertices[0][0]+(large_y_coor-small_y_coor)*math.sqrt(3)
    additional_vertex=[x_coord,y_coord]
    print(additional_vertex)
    list_of_vertices.append(additional_vertex)
else:
         for i in range(var):
            vertex = list(map(float, input(f"Enter vertex {i + 1} (e.g., 1 2): ").split()))
            list_of_vertices.append(vertex)



print("Initial list of vertices:")
initial_data = [
    [f"({v[0]:.2f}, {v[1]:.2f})", f"{float(f(v[0], v[1])):.2f}"]  # Ensure all initial values are floats
    for v in list_of_vertices
]
print_table(['Vertex', 'Function Value'], initial_data)

# Call the simplex method function
simplex_method(f, list_of_vertices)
# 5*x1 + x2 + 2*x1*x2

# Objective 2*x1**2+x2**2+2*x1*x2+x1-x2

"""
4 4
5 4
4 5
"""