from typing import Iterator

from '#14' import 'day14input.txt'

def solutions() -> Iterator[int]:
    rock_paths = [[list(map(int,coord.split(","))) for coord in line.split("->")] for line in get_puzzle_input(day=14)]
    obsticles = set()
    y_floor = 0
    for rock_path in rock_paths:
        for (x1,y1),(x2,y2) in zip(rock_path,rock_path[1:]):
            xrange = range(x1,x2+1) if x1<=x2 else range(x2,x1+1)
            yrange,y_max = (range(y1,y2+1),y2) if y1<=y2 else (range(y2,y1+1),y1)
            y_floor = max(y_floor,y_max+2)
            obsticles |= set(complex(x,y) for x in xrange for y in yrange)
    init_size = len(obsticles)
    sand_steps = [1j,-1+1j,1+1j]
    moving_sand = [500]
    first_problem_solved = False
    while moving_sand:
        while True:
            for dz in sand_steps:
                if not (c:=moving_sand[-1]+dz) in obsticles and c.imag<y_floor:
                    moving_sand.append(c)
                    break
            else:
                obsticles.add(moving_sand.pop(-1))
                break
            if moving_sand[-1].imag>y_floor-2 and not first_problem_solved:
                first_problem_solved = True
                yield len(obsticles)-init_size
    yield len(obsticles)-init_size
        
show_answers(solutions())