# Part 1
from string import ascii_uppercase

itxt = open("day5input.txt", mode='r').read()
itxt, moves = itxt.split('\n\n')
moves = list(filter(lambda e: e not in ['move', 'from', 'to'], moves.split()))
moves = list(map(int, moves))
itxt = itxt.splitlines()

stack_pos = itxt.pop(-1)
itxt.reverse()

stacks = dict()

for i, e in enumerate(list(stack_pos)):
    if e != ' ':
        stacks.update({ int(e): 
            [j[i] for j in itxt if j[i] in ascii_uppercase]})
        
while len(moves):
    n = moves.pop(0)
    f = moves.pop(0)
    t = moves.pop(0)
    
    for _ in range(n):
        stacks[t].append(stacks[f].pop(-1))

for i in stacks.values():
    print(i[-1], end='')

# Part 2

itxt = open("day5input.txt", mode='r').read()
itxt, moves = itxt.split('\n\n')
moves = list(filter(lambda e: e not in ['move', 'from', 'to'], moves.split()))
moves = list(map(int, moves))
itxt = itxt.splitlines()

stack_pos = itxt.pop(-1)
itxt.reverse()

stacks = dict()

for i, e in enumerate(list(stack_pos)):
    if e != ' ':
        stacks.update({ int(e): 
            [j[i] for j in itxt if j[i] in ascii_uppercase]})

while len(moves):
    n = moves.pop(0) #number of crates
    f = moves.pop(0) #from stack
    t = moves.pop(0) #to stack
    
    h = [stacks[f].pop(-1) for _ in range(n)]
    h.reverse()
    
    stacks[t].extend(h)
    

for i in stacks.values():
    print(i[-1], end='')