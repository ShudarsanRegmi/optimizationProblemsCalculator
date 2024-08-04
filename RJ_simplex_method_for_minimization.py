def simplex_method(f, list_of_vertices):
    store_values = []
    removed_vertices = []



    for i in range(len(list_of_vertices)):
        f_x = f(list_of_vertices[i][0], list_of_vertices[i][1])
        store_values.append(f_x)

    print("Function values at vertices:", store_values)


    max_f_x = max(store_values)
    print("Maximum function value:", max_f_x)

	@@ -22,17 +17,20 @@ def simplex_method(f, list_of_vertices):
        f_x = f(vertex[0], vertex[1])
        if f_x == max_f_x:
            removed_vertices.append(vertex)
            list_of_vertices.remove(vertex)  

    if len(list_of_vertices) == 2:
        add_new_x = (list_of_vertices[0][0] + list_of_vertices[1][0] - removed_vertices[0][0])
        add_new_y = (list_of_vertices[0][1] + list_of_vertices[1][1] - removed_vertices[0][1])
        list_of_vertices.append([add_new_x, add_new_y])
    for k in range(len(removed_vertices)):
        if (f(removed_vertices[k][0], removed_vertices[k][1]) == max_f_x):
            mean_x1 = (list_of_vertices[0][0] + list_of_vertices[1][0]) / 2
            mean_x2 = (list_of_vertices[0][1] + list_of_vertices[1][1]) / 2
            return mean_x1, mean_x2

    return simplex_method(f,list_of_vertices)
