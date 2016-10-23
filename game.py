from collections import defaultdict


def _get_neighbours(cell):
    x, y = cell
    cells_around = {(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)}
    cells_around.remove(cell)
    return cells_around


def _check_cell_survival(cell, neighbour_counts, next_grid):
    if neighbour_counts[cell] in (2, 3):
        next_grid.add(cell)


def _check_new_living_cells(neighbour_counts, next_grid):
    cells_with_three_neighbours = {cell for cell, count in neighbour_counts.iteritems() if count == 3}
    next_grid.update(cells_with_three_neighbours)


def _update_cell_neighbour_counts(cell, neighbour_counts):
    for neighbour in _get_neighbours(cell):
        neighbour_counts[neighbour] += 1


class Board(object):
    def __init__(self):
        self._grid = set()

    def seed(self, *cells):
        for x, y in cells:
            self._put_living_cell_at(x, y)

    def is_alive(self, x, y):
        return (x, y) in self._grid

    def next_generation(self):
        neighbour_counts = self._get_neighbour_counts()
        self._grid = self._get_next_grid(neighbour_counts)

    def _put_living_cell_at(self, x, y):
        self._grid.add((x, y))

    def _get_neighbour_counts(self):
        neighbour_counts = defaultdict(int)
        for cell in self._grid:
            _update_cell_neighbour_counts(cell, neighbour_counts)
        return neighbour_counts

    def _get_next_grid(self, neighbour_counts):
        next_grid = set()
        self._check_surviving_cells(neighbour_counts, next_grid)
        _check_new_living_cells(neighbour_counts, next_grid)
        return next_grid

    def _check_surviving_cells(self, neighbour_counts, next_grid):
        for cell in self._grid:
            _check_cell_survival(cell, neighbour_counts, next_grid)
