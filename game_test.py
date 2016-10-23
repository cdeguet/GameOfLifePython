import pytest

from game import Board


@pytest.fixture
def board():
    return Board()


def test_empty_board_has_no_living_cell(board):
    assert not board.is_alive(2, 3)


def test_put_one_living_cell(board):
    board.seed((2, 3))
    assert board.is_alive(2, 3)


def test_cell_with_one_neighbour_should_die(board):
    board.seed((2, 3))
    board.next_generation()
    assert not board.is_alive(2, 3)


def test_cells_with_two_or_three_neighbours_should_survive(board):
    board.seed((2, 1), (2, 2), (2, 3), (3, 2))
    board.next_generation()
    assert board.is_alive(2, 1)
    assert board.is_alive(2, 2)


def test_cell_with_four_neighbours_should_die(board):
    board.seed((2, 2), (2, 3), (3, 2), (1, 2), (2, 1))
    board.next_generation()
    assert not board.is_alive(2, 2)


def test_empty_cell_with_three_neighbours_should_become_alive(board):
    board.seed((2, 3), (3, 2), (1, 2))
    board.next_generation()
    assert board.is_alive(2, 2)
