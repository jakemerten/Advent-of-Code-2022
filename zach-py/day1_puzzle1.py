# Day 1 - Calories

# Function for part 2 -- Getting the sum of the top 3 calories
# Takes that list of all elves' calories - sorts it descendingly - sums the top 3
def sum_top_three(cal_list):
    top_three_cals = 0
    cal_list.sort(reverse=True)
    for calories in range(3):
        top_three_cals += cal_list[calories]
    return top_three_cals


# My handy Vars
calories = 0
max = 0
big_list = []

# Part 1
# Go through file line by line, if not whitespace add it up
# If whitespace, put the sum of that elf's cals into a list
# Check and update max as you go

with open('input_calories.txt') as file:

    for line in file:
        line1 = line
        
        
        if line1.strip():
            calories += int(line1)
        else:
            big_list.append(calories)
            calories = 0
            continue
           
    
        if calories > max:
            max = calories
            print ("new max = ", max)
    

print("final max: ", max)
print("Sum of the top 3: ", sum_top_three(big_list))
