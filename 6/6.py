

# To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the data-stream
# Return the number of characters from the beginning of the buffer to the end of the first such four-character marker.

# Read the Input
with open('6/input.txt', 'r') as file:
    # read the file line by line
    moves = file.readlines()
    input_string = moves[0]

# Make a list where each element is a character
list = list(input_string)

# Will return the amount of characters until the start of the sequence is detected, or -1
def check_for_n_distinct_characters(_list, _n):
    counter = 0
    for index, element, in enumerate(_list):
        counter += 1
        if counter >= _n:

            temp_char_list = [] # Temp list of the previous n characters
            for i in range(_n):
                temp_char_list.append(_list[index - i])
            temp_set = set(temp_char_list)

            # Check if all n characters are unique
            if len(temp_char_list) == len(temp_set):
                # Then all n consecutive characters are unique
                return counter

    return -1

check_part_1 = check_for_n_distinct_characters(list, 4)
if check_part_1 != 0:
    characters_until_start_detected_1 = check_part_1

check_part_2 = check_for_n_distinct_characters(list, 14)
if check_part_2 != 0:
    characters_until_start_detected_2 = check_part_2

# Print Answers
print("There are {} characters before the first start-of-packet marker is detected".format(characters_until_start_detected_1))
print("There are {} characters before the first start-of-message marker is detected".format(characters_until_start_detected_2))

