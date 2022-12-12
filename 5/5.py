
import re

# Make the "stack" data-structure for each stack of crates
# I do not read it directly from the input
list_of_stacks_1 = []
list_of_stacks_1.append(["Q", "W", "P", "S", "Z", "R", "H", "D"])
list_of_stacks_1.append(["V", "B", "R", "W", "Q", "H", "F"])
list_of_stacks_1.append(["C", "V", "S", "H",])
list_of_stacks_1.append(["H", "F", "G"])
list_of_stacks_1.append(["P", "G", "J", "B", "Z"])
list_of_stacks_1.append(["Q", "T", "J", "H", "W", "F", "L"])
list_of_stacks_1.append(["Z", "T", "W", "D", "L", "V", "J", "N"])
list_of_stacks_1.append(["D", "T", "Z", "C", "J", "G", "H", "F"])
list_of_stacks_1.append(["W", "P", "V", "M", "B", "H"])

list_of_stacks_2 = []
list_of_stacks_2.append(["Q", "W", "P", "S", "Z", "R", "H", "D"])
list_of_stacks_2.append(["V", "B", "R", "W", "Q", "H", "F"])
list_of_stacks_2.append(["C", "V", "S", "H",])
list_of_stacks_2.append(["H", "F", "G"])
list_of_stacks_2.append(["P", "G", "J", "B", "Z"])
list_of_stacks_2.append(["Q", "T", "J", "H", "W", "F", "L"])
list_of_stacks_2.append(["Z", "T", "W", "D", "L", "V", "J", "N"])
list_of_stacks_2.append(["D", "T", "Z", "C", "J", "G", "H", "F"])
list_of_stacks_2.append(["W", "P", "V", "M", "B", "H"])

# Read the Input
with open('5/input.txt', 'r') as file:
    # read the file line by line
    moves = file.readlines()
    moves = [line.strip() for line in moves]

# Move crates in "list_of_stacks_1"
for element in moves:
    # Use regular expression to match patters in the string
    # Move 
    pattern = 'move (\w+) from (\w+) to (\w+)'
    match = re.search(pattern, element)
    repeat = int(match.group(1))
    start_stack = list_of_stacks_1[int(match.group(2)) - 1]
    target_stack = list_of_stacks_1[int(match.group(3)) - 1]

    # Repeat the process "repeat"-times
    i = 0
    while i < repeat:
        i += 1
        val = start_stack.pop() # Move from the start_stack
        target_stack.append(val) # Place it on the target_stack

# Move crates in "list_of_stacks_2"
for element in moves:
    # Use regular expression to match patters in the string
    # Move 
    pattern = 'move (\w+) from (\w+) to (\w+)'
    match = re.search(pattern, element)
    stack_size = int(match.group(1))
    start_stack = list_of_stacks_2[int(match.group(2)) - 1]
    target_stack = list_of_stacks_2[int(match.group(3)) - 1]

    # Make a "temp_list" from the first "stack_size" elements in "start_stack"
    temp_list = []
    i = 0
    while i < stack_size:
        stack_size -= 1
        val = start_stack.pop()
        temp_list.append(val)
    
    # Add "temp_list" to "target_stack"
    while len(temp_list) > 0:
        target_stack.append(temp_list.pop())

# Make a string from the top crates
end_string_1 = ""
for element in list_of_stacks_1:
    if len(element) > 0:
        end_string_1 += element[-1]
end_string_2 = ""
for element in list_of_stacks_2:
    if len(element) > 0:
        end_string_2 += element[-1]

# Print Answers
print("The top crates on the stacks are: {}".format(end_string_1))
print("The top crates on the stacks are: {}".format(end_string_2))
