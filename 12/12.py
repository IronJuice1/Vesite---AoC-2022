
# Read the Input
with open('12/input.txt', 'r') as file:
    # read the file line by line
    input_list = file.readlines()
    input_list = [line.strip() for line in input_list]

# Map where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

# Turn in into a list of lists
for i, element, in enumerate(input_list):
    input_list[i] = list(input_list[i])


print(input_list)








