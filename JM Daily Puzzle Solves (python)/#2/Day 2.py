with open('inputDay2.txt', 'r') as f:
    GAMES = f.read().split('\n')

# ROCK = A ; X
# PAPER = B ; Y
# SCISSORS = C ; Z

WIN = 6
DRAW = 3
LOSE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

# Every possible combination for win/loss/draw

GAME_SCORE = {
    'A X': DRAW + ROCK,
    'A Y': WIN + PAPER,
    'A Z': LOSE + SCISSORS,
    'B X': LOSE + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': WIN + ROCK,
    'C Y': LOSE + PAPER,
    'C Z': DRAW + SCISSORS,  
}

print(f'Part A: {sum([GAME_SCORE.get(game, 0) for game in GAMES])}')

# X = You must lose this hand
# Y = You must draw this hand
# Z = You must win this hand

GAME_SCORE = {
    'A X': LOSE + SCISSORS,
    'A Y': DRAW + ROCK,
    'A Z': WIN + PAPER,
    'B X': LOSE + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': LOSE + PAPER,
    'C Y': DRAW + SCISSORS,
    'C Z': WIN + ROCK,
}

print(f'Part B: {sum([GAME_SCORE.get(game, 0) for game in GAMES])}')