


# The clock circuit ticks at a constant rate; each tick is called a cycle.
# register X: starts with value 1, has 2 instructions

# Read the Input
with open('10/input.txt', 'r') as file:
    # read the file line by line
    input_list = file.readlines()
    input_list = [line.strip() for line in input_list]

x = 1
current_cycle = 1
# Signal strength (the cycle number multiplied by the value of the X register)
signal_strength_list = []

def check():
    global current_cycle # Get the global variable so we know the one we are talking about
    if (current_cycle - 20) % 40 == 0:
        signal_strength_list.append(current_cycle * x)

def instruction_noop():
    global current_cycle
    current_cycle += 1
    check()

def instruction_addx(_add_value):
    global current_cycle, x
    current_cycle += 1
    check()
    current_cycle += 1
    x += _add_value
    check()

for element in input_list:

    if element == "noop":
        instruction_noop()
    elif element.startswith("addx"):
        split_string = element.split(" ")
        add_value = int(split_string[1])
        instruction_addx(add_value)

print("The sum of all the collected signal strengths are: {}".format(sum(signal_strength_list)))
