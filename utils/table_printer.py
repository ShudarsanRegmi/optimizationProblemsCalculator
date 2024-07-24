from prettytable import PrettyTable


def print_tables(lists_of_rows, column_headers):
    """
    Prints multiple tables, each created from a sublist in the list of rows.

    Args:
        lists_of_rows (list of list of tuples): A list containing sublists, each representing rows for a table.
        column_headers (list of str): Column headers for the tables.
    """
    for sublist in lists_of_rows:
        table = PrettyTable()
        table.field_names = column_headers

        for row in sublist:
            table.add_row(row)

        print(table)  # Print the table
        table.clear_rows()


def print_table(rows, column_headers):
    """
    Prints a single table created from the list of rows.

    Args:
        rows (list of tuples): A list representing rows for a table.
        column_headers (list of str): Column headers for the table.
    """
    table = PrettyTable()
    table.field_names = column_headers

    for row in rows:
        table.add_row(row)

    print(table)  # Print the table
