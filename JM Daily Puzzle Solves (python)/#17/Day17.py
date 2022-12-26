class Rock:
    def __init__(self, shape):
        self.landed = False
        self.space = [[0]*4 for y in range(4)]
        if shape == 'horizontal':
            self.space[0][0] = 1
            self.space[0][1] = 1
            self.space[0][2] = 1
            self.space[0][3] = 1
            self.width = 4
        elif shape == 'cross':
            self.space[0][1] = 1
            self.space[1][0] = 1
            self.space[1][1] = 1
            self.space[1][2] = 1
            self.space[2][1] = 1
            self.width = 3
        elif shape == 'L':
            self.space[0][0] = 1
            self.space[0][1] = 1
            self.space[0][2] = 1
            self.space[1][2] = 1
            self.space[2][2] = 1
            self.width = 3
        elif shape == 'vertical':
            self.space[0][0] = 1
            self.space[1][0] = 1
            self.space[2][0] = 1
            self.space[3][0] = 1
            self.width = 1
        elif shape == 'square':
            self.space[0][0] = 1
            self.space[0][1] = 1
            self.space[1][0] = 1
            self.space[1][1] = 1
            self.width = 2

    def move(self, direction, x, y, space):
        can_move = True
        if direction == 'v':
            for i in range(4):
                for j in range(4):
                    if self.space[i][j] == 1 and space[i+y-1][j+x] == 1:
                        can_move = False
            if can_move == True:
                return x, y-1
            self.landed = True
            return x, y

        if direction == '<':
            x_diff = -1
        elif direction == '>':
            x_diff = 1
        for i in range(4):
            for j in range(4):
                if self.space[i][j] == 1 and space[i+y][j+x+x_diff] == 1:
                    can_move = False
        if can_move == True:
            return x+x_diff, y
        return x, y

def trial(iterations):
    shape_count = len(order)
    jet_count = len(jets)
    space = [[1]*9] + [[1,0,0,0,0,0,0,0,1] for i in range(iterations*4)]
    top_rock = 0
    jet = 0
    starts = {}
    for k in range(iterations):
        jet = jet % jet_count
        if k % shape_count == 0 and space[top_rock][5] == 1:
            if jet in starts:
                starts[jet] += [k]
            else:
                starts[jet] = [k]
        rock = Rock(order[k%shape_count])
        initial = jets[jet] + jets[(jet+1)%jet_count] + jets[(jet+2)%jet_count]
        x = 3
        y = 4 + top_rock
        while not rock.landed:
            x, y = rock.move(jets[jet%jet_count], x, y, space)
            x, y = rock.move('v', x, y, space)
            jet += 1
        for i in range(4):
            for j in range(4):
                if rock.space[i][j] == 1:
                    space[i+y][j+x] = 1
                    top_rock = max(top_rock, i+y)
    return (top_rock, starts)

order = ['horizontal','cross','L','vertical','square']
count = 1000000000000
with open('day17input.txt','r') as f:
    jets = [jet for jet in f.readline().strip()]

    print(trial(2022)[0])

    lcm = len(jets) * len(order)
    _, starts = trial(lcm)
    biggest = max([jet for jet, iteration_counts in starts.items()])
    repetition = starts[biggest][-1] - starts[biggest][-2]
    growth = trial(starts[biggest][-1])[0] - trial(starts[biggest][-2])[0]
    start = count % repetition + lcm//repetition*repetition
    top_rock = trial(start)[0] + growth * (count-start)//repetition

    print(top_rock)