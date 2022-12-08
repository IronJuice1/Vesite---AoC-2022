
# A for Rock, B for Paper, and C for Scissors (Opponent)
# X for Rock, Y for Paper, and Z for Scissors (Me)
# 1 for Rock, 2 for Paper, and 3 for Scissors
# plus the score for the outcome of the round, 0 if you lost, 3 if the round was a draw, and 6 if you won

# Read the unput
with open('2/input.txt', 'r') as file:
    # read the file line by line
    lines = file.readlines()
    lines = [line.strip() for line in lines]

total_score_1 = 0
# Move through the list and add to the total_score variable one element at a time
for element in lines:
    opponent_play = element[0]
    my_play = element[2]

    # Add score for what I played
    if my_play == "X": total_score_1 += 1
    if my_play == "Y": total_score_1 += 2
    if my_play == "Z": total_score_1 += 3

    # Add score from round results
    #Draw Check
    if (my_play == "X" and opponent_play == "A") or (my_play == "Y" and opponent_play == "B") or my_play == "Z" and opponent_play == "C":
        total_score_1 += 3
    # Win Check
    elif (my_play == "X" and opponent_play == "C") or (my_play == "Y" and opponent_play == "A") or (my_play == "Z" and opponent_play == "B"):
        total_score_1 += 6
    # Don't need a lose check



# New Rules: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
total_score_2 = 0
for element in lines:
    opponent_play = element[0]
    round_result = element[2]
    # Add score from round results
    if (round_result == "Y"): total_score_2 += 3
    if (round_result == "Z"): total_score_2 += 6

    # Find out what we play, and set my_play based on that
    # Draw
    if (round_result == "Y"): my_play = opponent_play
    # Lose the round
    elif (round_result == "X" and opponent_play == "A"): my_play = "C"
    elif (round_result == "X" and opponent_play == "B"): my_play = "A"
    elif (round_result == "X" and opponent_play == "C"): my_play = "B"
    # Win the round
    elif (round_result == "Z" and opponent_play == "A"): my_play = "B"
    elif (round_result == "Z" and opponent_play == "B"): my_play = "C"
    elif (round_result == "Z" and opponent_play == "C"): my_play = "A"
    
    # Add score for what I played
    if my_play == "A": total_score_2 += 1
    if my_play == "B": total_score_2 += 2
    if my_play == "C": total_score_2 += 3

# Print Answer
print("Total Score using the given strategy (part 1): {}".format(total_score_1))

print("Total Score using the given strategy (part 2): {}".format(total_score_2))
