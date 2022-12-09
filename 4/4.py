
# Section has ID number


# Read the Input
with open('4/input.txt', 'r') as file:
    # read the file line by line
    lines = file.readlines()
    lines = [line.strip() for line in lines]

new_input_list = []
# Make a big list of lists, where each inner list has 2 elements
for index, element, in enumerate(lines):
    parts = element.split(",")
    new_input_list.append(parts)

complete_overlap_counter = 0
any_overlap_counter = 0
# Check how many times one range fully contains the other
for element in new_input_list:

    numbers_first = element[0].split("-")
    number_f_1 = int(numbers_first[0])
    number_f_2 = int(numbers_first[1])

    numbers_second = element[1].split("-")
    number_s_1 = int(numbers_second[0])
    number_s_2 = int(numbers_second[1])

    # Check for complete overlap
    if ((number_f_1 <= number_s_1 and number_f_2 >= number_s_2)   # Check if the first one contains the second one
    or  (number_s_1 <= number_f_1 and number_s_2 >= number_f_2)): # Check if the second one contains the first one
        complete_overlap_counter += 1

    # Check for any overlap
    if not ((number_f_2 < number_s_1)   # All in the first is smaller than all in the second
    or      (number_s_2 < number_f_1)): # All in the second is smaller than all in the first
        any_overlap_counter += 1
        


# 6-7    1-2

# Print Answers
print("The ranges overlap completely {} Times".format(complete_overlap_counter))
print("The ranges overlap in any way {} Times".format(any_overlap_counter))
