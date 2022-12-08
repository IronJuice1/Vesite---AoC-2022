
with open('3/input.txt', 'r') as file:
    # read the file line by line
    lines = file.readlines()
    lines = [line.strip() for line in lines]

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def get_priority_from_character(_char):
    if _char.isupper():
        char_numerical_val = ord(_char)
        return char_numerical_val - (65) + 27
    else:
        char_numerical_val = ord(_char)
        return char_numerical_val - (97) + 1

# Loop through each element
sum_priority_1 = 0
for element in lines:
    #Split each element
    if len(element) % 2 == 0: # Each element should be even, should not need this check
        midpoint = len(element)//2
        first_half = element[:midpoint]
        second_half = element[midpoint:]
        set1 = set(first_half)
        set2 = set(second_half)
        common_chars_set = set1.intersection(set2) # Should only be one common character, I assume this is only one character
        common_chars_string = common_chars_set.pop() # Convert to string
        sum_priority_1 += get_priority_from_character(common_chars_string)
    else:
        print("value is not even")

# Loop through each third element, use an enumerator so we know the index
sum_priority_2 = 0
for index, element, in enumerate(lines):
    # Check if the index is a multiple of 3
    if index % 3 == 0:
        sack1 = lines[index]
        sack2 = lines[index + 1]
        sack3 = lines[index + 2]
        set1 = set(sack1)
        set2 = set(sack2)
        set3 = set(sack3)
        common_chars_set = set1.intersection(set2, set3) # Should only be one common character, I assume this is only one character
        common_chars_string = common_chars_set.pop() # Convert to string
        sum_priority_2 += get_priority_from_character(common_chars_string)

# Print Answers
print("Sum of all priorities (part 1): {}".format(sum_priority_1))
print("Sum of all priorities (part 2): {}".format(sum_priority_2))
