

# Read the Input
with open('9/input.txt', 'r') as file:
    # read the file line by line
    list = file.readlines()
    list = [line.strip() for line in list]

start_coords = [0, 0]
head_coords = [0, 0]
tail_coords = [0, 0]
tail_positions_unique = set()

def move(_dir):
    if _dir == "L":
        change = [-1, 0]
    if _dir == "R":
        change = [1, 0]
    if _dir == "D":
        change = [0, -1]
    if _dir == "U":
        change = [0, 1]

    # Move the head
    head_coords[0] += change[0]
    head_coords[1] += change[1]

    #Then change the tail_coords based on where the head_coords are
    # Check if the tail coords are far away from the head_coords?
    x_pos_difference = abs(head_coords[0] - tail_coords[0])
    if x_pos_difference >= 2:
        if tail_coords[0] > head_coords[0]:     # If the tail is bigger, move negative direction
            tail_coords[0] -= 1
        else:                                   # Otherwise, move positive direction
            tail_coords[0] += 1
        
        # Here, when the tail gets dragged in a horizontal direction, we make the y-position match
        tail_coords[1] = head_coords[1]
    
    y_pos_difference = abs(head_coords[1] - tail_coords[1])
    if y_pos_difference >= 2:
        if tail_coords[1] > head_coords[1]:     # If the tail is bigger, move negative direction
            tail_coords[1] -= 1
        else:                                   # Otherwise, move positive direction
            tail_coords[1] += 1
        
        # Here, when the tail gets dragged in a vertical direction, we make the x-position match
        tail_coords[0] = head_coords[0]

    return tail_coords

# Calculate one move at a time
for element in list:

    # Get data
    split_string = element.split(" ")
    direction = split_string[0]
    repeat_times = int(split_string[1])
    # Do the moves
    for i in range(repeat_times):
        tail_coords = move(direction)
        tail_positions_unique.add(tuple(tail_coords)) # Save the tail position, convert the tail coords to a tuple

# Answer 1997 is too low
# Answer 2377 is too low
print("The tail has visited {} unique tiles".format(len(tail_positions_unique)))

