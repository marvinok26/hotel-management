# lib/debug.py

def print_table(table):
    """
    Print the contents of a database table.

    Args:
        table: SQLAlchemy table object.

    Returns:
        None
    """
    for row in table:
        print(row)
