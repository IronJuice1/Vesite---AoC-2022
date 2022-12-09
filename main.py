# Run this file and enter input to run any of the other file, it will also print and save the runtime of the program

import sys
import time

while True:

    user_input = input("Enter the day you want to run (a number from 1 to 24):")

    # Print "Invalid input" if the input is wrong, break out if the input is correct
    try:
        user_number = int(user_input)
        if 1 <= int(user_input) <= 24:
            #Correct Input
            break
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("Invalid input. Please try again.")


file = user_input + "/" + user_input + ".py"
print("Running File: {}".format(file))

# Measure the time before the operation
start_time = time.perf_counter()

# Open and run the file
with open(file) as f:
    # Read the contents of the file
    script_contents = f.read()
exec(script_contents)

# Measure the time after the operation
end_time = time.perf_counter()
# Calculate the difference to find out how long the operation took
elapsed_time = end_time - start_time
# Print the elapsed time
result_string = "Day {} took {} seconds ({} Milliseconds) ({} Microseconds)".format(user_input, elapsed_time, elapsed_time*1000, elapsed_time*1000000)
print(result_string)

# Make a new file in the folder and store the results
file_name = user_input + "/time_result.txt"
with open(file_name, "w") as file:
    file.write(result_string)
