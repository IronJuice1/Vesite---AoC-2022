
# 999
# 929
# 999

# Will return True if the tree is visible from above
def check_tree_visible_from_above(_col, _row):

    current_tree_height = grid_list[_row][_col]

    # Check max n-times
    for i in range(grid_height):

        # Check if we are trying to index a invalid value
        row_to_check = _row - (i + 1)
        if (row_to_check) < 0: break

        # Compare heights
        compare_tree_height = grid_list[row_to_check][_col]
        if compare_tree_height >= current_tree_height:
            return False
    
    return True

# Will return True if the tree is visible from below
def check_tree_visible_from_below(_col, _row):

    current_tree_height = grid_list[_row][_col]

    # Check max n-times
    for i in range(grid_height):

        # Check if we are trying to index a invalid value
        row_to_check = _row + (i + 1)
        if (row_to_check) >= grid_height: break

        # Compare heights
        compare_tree_height = grid_list[row_to_check][_col]
        if compare_tree_height >= current_tree_height:
            return False
    
    return True

# Will return True if the tree is visible from the left
def check_tree_visible_from_left(_col, _row):

    current_tree_height = grid_list[_row][_col]

    # Check max n-times
    for i in range(grid_width):
        # Check if we are trying to index a invalid value
        col_to_check = _col - (i + 1)
        if (col_to_check) < 0: break

        # Compare heights
        compare_tree_height = grid_list[_row][col_to_check]
        if compare_tree_height >= current_tree_height:
            return False
    
    return True

# Will return True if the tree is visible from the right
def check_tree_visible_from_right(_col, _row):

    current_tree_height = grid_list[_row][_col]

    # Check max n-times
    for i in range(grid_width):
        # Check if we are trying to index a invalid value
        col_to_check = _col + (i + 1)
        if (col_to_check) >= grid_width: break

        # Compare heights
        compare_tree_height = grid_list[_row][col_to_check]
        if compare_tree_height >= current_tree_height:
            return False
    
    return True


def check_tree_visibility(_col, _row):

    if (check_tree_visible_from_above(_col, _row)
    or  check_tree_visible_from_below(_col, _row)
    or  check_tree_visible_from_left(_col, _row)
    or  check_tree_visible_from_right(_col, _row)):
        return 1
    else:
        return 0

# Read the Input
with open('8/input.txt', 'r') as file:
    # read the file line by line
    my_list = file.readlines()
    my_list = [line.strip() for line in my_list]

# Make the "grid_list"
grid_list = []
for element in my_list:
    grid_list.append(list(element))

# Find the grid size
grid_width = len(grid_list[0])
grid_height = len(grid_list)
print("Grid Width: {}".format(grid_width))
print("Grid Height: {}".format(grid_height))

# Can move though each tree and run "check_tree_visibility"
visible_trees = 0
for index_y, element_y, in enumerate(grid_list):                    # Go through each line
    for index_x, element_x, in enumerate(grid_list[index_y]):       # Go through the list in the line
        # Here we can check every single tree
        visible_trees += check_tree_visibility(index_x, index_y)

print("Visible Trees: {}".format(visible_trees))

