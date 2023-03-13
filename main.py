import random
from typing import Tuple, Dict, List

from constants import ALL, dirs, rules, BLANK

Cells = Dict[Tuple[int, int], List[str]]
Pos = Tuple[int, int]


def build_cells() -> Cells:
    data = dict()
    for row in range(dim_row):
        for col in range(dim_col):
            data[row, col] = ALL
    return data


def min_count(cells: Cells) -> int:
    counts = [len(cells[pos]) for pos in cells if len(cells[pos]) > 1]
    if counts:
        return min(counts)
    return 0


def collapse(cells: Cells, min_: int) -> None:
    # find the lowest entropy item and collapse
    choice = random.choices(
        [pos for pos, entropy in cells.items() if len(entropy) == min_]
    )[0]

    cells[choice] = random.choices(list(cells[choice]))
    update_neighbours(cells)


def update_neighbours(cells: Cells) -> None:
    for row in range(dim_row):
        for col in range(dim_col):
            choices = set(cells[(row, col)])
            if len(choices) > 1:
                # should reduce if we can find items currently at 1 item
                for d, key in zip(dirs, 'ewns'):
                    neighbour = row + d[0], col + d[1]
                    
                    # if on the board and only have one option in the neighbour -- opportunity to reduce.
                    if 0 <= neighbour[0] < dim_row and 0 <= neighbour[1] < dim_col:
                        if len(cells[neighbour]) == 1:
                            # find the key
                            collapsed_key = cells[neighbour][0]
                            
                            # reduce the current choices by the neighbours key's options 
                            choices = choices.intersection(rules[collapsed_key][key])
                            if len(choices) < 1:
                                raise AssertionError("Cell collapsed to less than 1; which should be impossible.")
                            
                cells[(row, col)] = list(choices)


def pprint(cells: Cells) -> None:
    for row in range(dim_row):
        for col in range(dim_col):
            result = cells[row, col]
            if len(result) == 1:
                print(result[0], end="")
            else:
                print("*", end="")
        print()


def main() -> Cells:
    cells = build_cells()
    for i in range(dim_col):
        cells[(0, i)] = [BLANK, ]
        cells[(dim_row-1, i)] = [BLANK, ]
        
    for i in range(dim_row):
        cells[(i, 0)] = [BLANK, ]
        cells[(i, dim_col-1)] = [BLANK, ]
    
    update_neighbours(cells)   
    
    while (count := min_count(cells)) > 1:
        try:
            collapse(cells, count)
        except AssertionError as e:
            print(e)
    
    return cells


if __name__ == "__main__":
    dim_row = 6
    dim_col = 12
    
    cells_ = main()
    pprint(cells_)
