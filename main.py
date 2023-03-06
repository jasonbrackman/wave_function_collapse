import random
from typing import Tuple

from constants import ALL, dirs, rules, BLANK


def build_cells():
    data = dict()
    for row in range(dim_row):
        for col in range(dim_col):
            data[row, col] = ALL
    return data


def min_count(cells):
    counts = [len(cells[pos]) for pos in cells if len(cells[pos]) > 1]
    if not counts:
        return 0
    return min(counts)


def collapse(cells, min_: int):
    # find the lowest entropy item and collapse
    choice = random.choices(
        [pos for pos, entropy in cells.items() if len(entropy) == min_]
    )[0]
    new_set = random.choices(list(cells[choice]))
    cells[choice] = list(set(cells[choice]).intersection(set(new_set)))

    update_neighbours(cells, choice)


def update_neighbours(cells, pos: Tuple[int, int]) -> None:
    collapsed_key = cells[pos][0]
    for d, key in zip(dirs, "wesn"):
        new_pos = pos[0] + d[0], pos[1] + d[1]
        if 0 <= new_pos[0] < dim_row and 0 <= new_pos[1] < dim_col:
            if len(cells[new_pos]) > 1:
                new_set = set(cells[new_pos]).intersection(rules[collapsed_key][key])
                if len(new_set) < 1:
                    raise AssertionError("Cell collapsed to less than 1; which should be impossible.")
                cells[new_pos] = list(new_set)


def pprint(cells):
    for row in range(dim_row):
        for col in range(dim_col):
            result = cells[row, col]
            if len(result) == 1:
                print(result[0], end="")
            else:
                print("*", end="")
        print()


def main():
    cells = build_cells()
    for i in range(dim_col):
        cells[(0, i)] = [BLANK, ]
        update_neighbours(cells, (0, i))
        
        cells[(dim_row-1, i)] = [BLANK, ]
        update_neighbours(cells, (dim_row-1, i))
    
    for i in range(dim_row):
        cells[(i, 0)] = [BLANK, ]
        update_neighbours(cells, (i, 0))
        
        cells[(i, dim_col-1)] = [BLANK, ]
        update_neighbours(cells, (i, dim_col-1))
            
    while (count := min_count(cells)) > 1:
        try:
            collapse(cells, count)
        except AssertionError as e:
            print(e)
            main()
    return cells


if __name__ == "__main__":
    dim_row = 10
    dim_col = 120
    
    cells = main()
    pprint(cells)