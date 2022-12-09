# Part 1
# Focus on transposing

data = open('day8input.txt').readlines()

forest = [[int(x) for x in row.strip()] for row in data]
forest2 = list(zip(*forest))

s = 0
for i in range(len(forest[0])):
    for j in range(len(forest)):
        tree = forest[i][j]
        if all(x < tree for x in forest[i][0:j]) or \
            all(x < tree for x in forest[i][j+1:]) or \
            all(x < tree for x in forest2[j][0:i]) or \
            all(x < tree for x in forest2[j][i+1:]):
            s += 1

print(s)

# Part 2

s = 0

def view_length(tree, view):
    view_length = 0
    for v in view:
        view_length += 1
        if v >= tree:
            break
    return view_length

for i in range(len(forest[0])):
    for j in range(len(forest)):
        tree = forest[i][j]

        s1 = view_length(tree, forest[i][0:j][::-1])
        s2 = view_length(tree, forest[i][j+1:])
        s3 = view_length(tree, forest2[j][0:i][::-1])
        s4 = view_length(tree, forest2[j][i+1:])
        score = s1 * s2 * s3 * s4
        if score > s:
            s = score

print(s)