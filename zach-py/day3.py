prio_dict = {

    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
        'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
        'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
        'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}

file = open("input_day3.txt", "r")



def part1(input_file):
    total_prio = 0

    for line in file:
        backpack = line.strip()
        #Split the input string into two equal sized lists
        half = len(backpack)//2


        comp1 = line[:half]
        comp2 = line[half:]
 
        for char in comp1:
            if char in comp2:
                common_char = char

        prio = prio_dict[common_char]

        total_prio += prio
    print("total prio for part 1 is: ", total_prio)


def part2(input_file):
    total_prio = 0
    i = 1
    backpack_list = []
    for line in file:
        backpack = line
        backpack_list.append(backpack)
        
        #use modulo to get every 3 lines
        if i == 3:
            common = [char for char in backpack_list[0] if char in backpack_list[1] and char in backpack_list[2]]
            common_char = common[0]
            prio = prio_dict[common_char]
            total_prio += prio
            backpack_list.clear()
            i = 0
        i += 1

    print("total prio for part 2 is: ", total_prio)

part1(file)
file.close()

file = open("input_day3.txt", "r")
part2(file)
file.close()