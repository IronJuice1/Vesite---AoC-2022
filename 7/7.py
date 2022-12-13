
# Lines that begin with $ are commands you executed

# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes

# Read the Input
with open('7/input.txt', 'r') as file:
    # read the file line by line
    list = file.readlines()
    list = [line.strip() for line in list]

# Every time we run "ls", the next lines until another $ are the files in the directory

# Function that calculates the size of a directory
def size_of_directory(_directory):
    total_s = 0
    # Search through the input list until we find "$ cd _directory"
    match_string = "$ cd " + _directory
    for index, element, in enumerate(list):
        if element == match_string:
            # While statement that moves down the input_list
            # If a line starts with $ and is not 
            counter = 0
            while True:
                counter += 1
                index_to_check = index + counter
                
                # Leave if "index_to_check" is out of bounds
                if (len(list) - 1) < index_to_check:
                    break # Leave the while-statement
                
                # The Line we check what to do with
                line = list[index_to_check]

                if line == "$ ls":
                    continue # Skip

                if line.startswith("$"):
                    break # Leave the while-statement

                #Then we should have a file or a directory we need to calculate the size of
                if line.startswith("dir"):
                    split_string = line.split(" ")
                    new_directory = split_string[1]
                    total_s += size_of_directory(new_directory)
                else:
                    total_s += size_of_file(line)
            break # After the element matches the string we end looping through all lines
    return total_s

# Function that calculates the size of a file
def size_of_file(_file):
    # Return the first number in the "_file" string
    split_string = _file.split(" ")
    return int(split_string[0])

# Then loop through all directories, and run "size_of_directory" of all of them and add the results into a list
# I think the input only run the command "dir x" a single time for each directory
directory_size_list = []

for element in list:
    # find lines that start with "dir"
    if element.startswith("$ cd") and (element != "$ cd .."):
        split_string = element.split(" ")
        size_of_dir = size_of_directory(split_string[2]) # Calculate the size of the dir and all sub-directories
        directory_size_list.append(size_of_dir) # Add to the list of directory sizes

# Add all values below or equal 100000 to a new list
final_list = []
for element in directory_size_list:
    if element <= 100000:
        final_list.append(element)

# Print Answers
print("Final Sum: {}".format(sum(final_list))) # Wrong Answer?

print(directory_size_list)


