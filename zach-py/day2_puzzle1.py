hand_scores = {

    "A": "1",
    "B": "2",
    "C": "3",
    "X": "1",
    "Y": "2",
    "Z": "3",

}

# Functions for winning scoring

# My move is a rock, so check their move and return proper score
def rock(their_move):
    if(their_move == 'A'):
        return 3
    elif(their_move == 'B'):
        return 0
    else:
        return 6

def paper(their_move):
    if(their_move == 'A'):
        return 6
    elif(their_move == 'B'):
        return 3
    else:
        return 0

def scissors(their_move):
    if(their_move == 'A'):
        return 0
    elif(their_move == 'B'):
        return 6
    else:
        return 3

    
# Part 2 Functions -- take my move and decide what to play

def rock_lose(their_move):  # I need to lose...
    if(their_move == 'A'):
        return 3  # returning scissors (to lose to their rock) and 0 for losing
    elif(their_move == 'B'):
        return 1  # returning rock to lose to their paper
    else:
        return 2  # returning paper to lose to their scissors
    
def paper_draw(their_move):
    if(their_move == 'A'):
        return 1 + 3                 # returning 1 for rock (to draw) + 3 for draw
    elif(their_move == 'B'):
        return 2 + 3
    else:
        return 3 + 3
    
def scissors_win(their_move):
    if(their_move == 'A'):
        return 2 + 6              # returning 2 for paper(to win)  + 6 for win
    elif(their_move == 'B'):
        return 3 + 6
    else:
        return 1 + 6
    





score = 0



file = open('input_rps.txt', 'r')

for line in range(2499):
    line1 = file.readline()
    line1 = line1.split()
    print(line1)
    my_move = hand_scores[line1[1]]
    print(my_move)
   # score += int(my_move)                                     ###used for part 1
    print(score)
    # 3 cases of my move use proper funciton
    
    if line1[1] == 'X':
        score += rock_lose(line1[0])                          ### use rock(line1[0]) for part 1
        print(score)
    elif line1[1] == 'Y':
        score += paper_draw(line1[0])
        print(score)
    else:
        score += scissors_win(line1[0])
        print(score)
print("score is: ", score) 


