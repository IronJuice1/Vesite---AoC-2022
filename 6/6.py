

# To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the data-stream
# Return the number of characters from the beginning of the buffer to the end of the first such four-character marker.

# Read the Input
with open('6/input.txt', 'r') as file:
    # read the file line by line
    moves = file.readlines()
    input_string = moves[0]

# Make a list where each element is a character
list = list(input_string)

# Move through list 
counter = 0
for index, element, in enumerate(list):
    counter += 1
    if counter >= 4:
        temp_char_list = [] # Temp list of the previous 4 characters
        temp_char_list.append(list[index - 3]) 
        temp_char_list.append(list[index - 2])
        temp_char_list.append(list[index - 1])
        temp_char_list.append(list[index - 0])
        temp_set = set(temp_char_list)

        # Check if all 4 characters are unique
        if len(temp_char_list) == len(temp_set):
            # Then all 4 characters are unique
            characters_until_start_detected = counter
            break

# Print Answers
print("There are {} characters before the first start-of-packet marker is detected".format(characters_until_start_detected))


