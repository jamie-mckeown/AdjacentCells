def get_adjacent (row, col, array) :
    '''Takes a cell in a 2D array of shape (num_rows, num_cols) given by its row and column indexes, and returns a list of the adjacent cells' values.'''
    neighbours = []

    num_rows = len(array)
    num_cols = len(array[0]) # each row of the array is the same length (= the num of cols)

    #   Check if near edges
    if row == 0:
        row_min = row
        row_max = row + 1
    elif row == num_rows - 1:
        row_min = row - 1
        row_max = row
    else:
        row_min = row - 1
        row_max = row + 1

    if col == 0:
        col_min = col
        col_max = col + 1
    elif col == num_cols - 1:
        col_min = col - 1
        col_max = col
    else:
        col_min = col - 1
        col_max = col + 1

    #   Now find the neighbours
    for i in range(row_min, row_max + 1):
        for j in range(col_min, col_max + 1):
                if i == row and j == col:
                    pass
                else:
                    neighbours.append(array[i,j])

    return neighbours