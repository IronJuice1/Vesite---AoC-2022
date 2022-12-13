
import math

# Read the Input
with open('10/input.txt', 'r') as file:
    # read the file line by line
    input_list = file.readlines()
    input_list = [line.strip() for line in input_list]

# Process of each monkey throwing an item
round = 0

# Monkey n is list_of_monkeys[n][0]
# [[monkey_number(0), is_worry_level_mult, math_value, divisible_by_number_check, true_cond_monkey_number, false_cond_monkey_number, [inventory], times_inspected]]
# [(0),               (1),                 (2),        (3),                       (4),                     (5),                      (6)          (7)]
list_of_monkeys = []

list_of_monkeys.append([0, True, 2,         17, 2, 5,   [96, 60, 68, 91, 83, 57, 85],       0])
list_of_monkeys.append([1, False, 3,        13, 7, 4,   [75, 78, 68, 81, 73, 99],           0])
list_of_monkeys.append([2, False, 6,        19, 6, 5,   [69, 86, 67, 55, 96, 69, 94, 85],   0])
list_of_monkeys.append([3, False, 5,        7,  7, 1,   [88, 75, 74, 98, 80],               0])
list_of_monkeys.append([4, False, 8,        11, 0, 2,   [82],                               0])
list_of_monkeys.append([5, True, 5,         3,  6, 3,   [72, 92, 92],                       0])
list_of_monkeys.append([6, True, "old",     2,  3, 1,   [74, 61],                           0])
list_of_monkeys.append([7, False, 4,        5,  4, 0,   [76, 86, 83, 55],                   0])

# Count the total number of times each monkey inspects items over 20 rounds
# monkey_business is the two top monkeys multiplied
monkey_business = 0

# First read the input and store all needed information in list_of_monkeys as the format says

# Use the information in "list_of_monkeys" and simulate a round of monkeys throwing items
def simulate_a_round():
    for element in list_of_monkeys: # Loop through each monkey
        
        # Get values from the monkey
        monkey_inventory = element[6]
        do_multiplication = element[1]
        math_value = element[2]
        divisible_number = element[3]
        true_cond_monkey_number = element[4]
        false_cond_monkey_number = element[5]

        for item in monkey_inventory: # Loop through each inventory

            # Inspect the item and change the worry level
            if do_multiplication:
                if math_value == "old": # Weird solution to this one special case
                    item = item*item
                else:
                    item = item * math_value
            else:
                item = item + math_value
            item = item // 3

            # Count how many items the monkey has inspected
            element[7] += 1

            # Check what monkey to throw it to
            if item % divisible_number == 0:
                # Give the item to monkey "list_of_monkeys[true_cond_monkey_number]"
                monkey_new = list_of_monkeys[true_cond_monkey_number]
                monkey_new[6].append(item)
            else:
                # Give the item to monkey "list_of_monkeys[false_cond_monkey_number]"
                monkey_new = list_of_monkeys[false_cond_monkey_number]
                monkey_new[6].append(item)
            
        # Clear the inventory of the current monkey after it has thrown all its items
        element[6] = []

print("Start Data: ")
for element in list_of_monkeys: # Loop through each monkey
    print(element)

# Simulate 20 rounds of monkey
for i in range(20):
    simulate_a_round()

print("End Data: ")
for element in list_of_monkeys: # Loop through each monkey
    print(element)

inspected_amount_list = []
for element in list_of_monkeys: # Loop through each monkey
    inspected_amount_list.append(element[7])

# 692 is too low
inspected_amount_list.sort(reverse=True)
print(inspected_amount_list[0] * inspected_amount_list[1])
