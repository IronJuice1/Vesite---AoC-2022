
with open('1/input.txt', 'r') as file:
    # read the file line by line
    lines = file.readlines()
    lines = [line.strip() for line in lines]

# Go through the list and add up numbers and add them to a new list, when there is a empty string i add temp_sum to the sum_list
sum_list = []
temp_sum = 0
for element in lines:
    if len(element) == 0:
        sum_list.append(temp_sum)
        temp_sum = 0
    else:
        temp_sum += int(element)

# Sort the sum_list
sum_list = sorted(sum_list,reverse=True)

# Print Answer
biggest_value = max(sum_list)
print("Most Calories: {}".format(biggest_value))
top_three_calories = sum_list[0] + sum_list[1] + sum_list[2]
print("Top Three Total Calories: {}".format(top_three_calories))
