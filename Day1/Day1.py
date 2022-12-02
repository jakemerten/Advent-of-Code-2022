# Open input file
# Designate file as read only
# Each new line comes out as a new integer

with open('input_Day1.txt', 'r') as infile:
    elves = [[int(c) for c in x.split("\n")] for x in infile.read()[:-1].split("\n\n")]

# Print the elf with the highest amount of calories being carried (max sum)

    print(f"Part A, Top Elf: {max(sum(x) for x in elves)}")

# Part B you sort highest to lowest calories and pick the top highest calories being carried by respective elves
    
    print(f"Part B, Top Three Elves Total Sum: {sum(sorted([sum(x) for x in elves])[-3:])}")