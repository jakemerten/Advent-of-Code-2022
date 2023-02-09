# Elves need to clean up camp - each section has a unique ID
# Each elf is assigned to a range of section ID's
# Find and remove overlapping sections

file = open("input_day4.txt", "r")
c = 0
ass_pairs = 0
for line in file:

    comma_split = line.split(',')
        
    first_pair = comma_split[0]
    first_pair_split = first_pair.split('-')
    first_floor = first_pair_split[0]
    first_roof = first_pair_split[1]

    second_pair = comma_split[1]
    second_pair_split = second_pair.split('-')
    second_floor = second_pair_split[0]
    second_roof = second_pair_split[1]

    if (first_floor <= second_floor and first_roof >= second_roof):  # second is contained by first
        ass_pairs += 1
        
    elif (first_floor >= second_floor and first_roof <= second_roof):  #first is contained by second
        ass_pairs += 1

    print(ass_pairs)
file.close()
print(ass_pairs)

