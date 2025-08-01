import pytest
import soudoku

@pytest.fixture
def sudoku_board():
    return [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

@pytest.fixture
def squared_board():
    return [
       ["5", "3", ".", "6", ".", ".", ".", "9", "8"],
       ["8", ".", ".", "4", ".", "6", "7", ".", "."],
       [".", "6", ".", ".", ".", ".", ".", ".", "."],
       [".", "7", ".", "1", "9", "5", ".", ".", "."],
       [".", "6", ".", "8", ".", "3", ".", "2", "."],
       [".", ".", ".", "4", "1", "9", ".", "8", "."],
       [".", ".", ".", ".", ".", ".", ".", "6", "."],
       [".", ".", "3", ".", ".", "1", ".", ".", "6"],
       ["2", "8", ".", ".", ".", "5", ".", "7", "9"]
    ]

@pytest.fixture
def transposed_board():
    return [
        ["5", "6", ".", "8", "4", "7", ".", ".", "."],
        ["3", ".", "9", ".", ".", ".", "6", ".", "."],
        [".", ".", "8", ".", "6", ".", ".", ".", "."],
        [".", "1", ".", ".", "8", ".", ".", "4", "."],
        ["7", "9", ".", "6", ".", "2", ".", "1", "8"],
        [".", "5", ".", ".", "3", ".", ".", "9", "."],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", "6", ".", ".", ".", "8", ".", "7"],
        [".", ".", ".", "3", "1", "6", ".", "5", "9"]
    ]

def test_is_unique(sudoku_board):
    assert soudoku.is_unique(sudoku_board[0]) == True
    assert soudoku.is_unique(["5", "3", ".", ".", "7", ".", ".", ".", "."]) == True
    assert soudoku.is_unique(["5", "3", "5", ".", "7", ".", ".", ".", "."]) == False

def test_transpose(sudoku_board, transposed_board):
    assert soudoku.transpose(sudoku_board) == transposed_board

def test_square_board(sudoku_board, squared_board):
    # Assuming square_board is implemented to convert the board into a square format
    calculated_squared_board = soudoku.square_board(sudoku_board) 
    assert len(calculated_squared_board[0]) == len(squared_board[0]) 
    assert len(calculated_squared_board[1]) == len(squared_board[1]) 
    assert len(calculated_squared_board[2]) == len(squared_board[2]) 
    assert calculated_squared_board[0] == squared_board[0]
    assert calculated_squared_board[1] == squared_board[1]
    assert calculated_squared_board[2] == squared_board[2]
    assert len(calculated_squared_board) == len(squared_board)
    assert calculated_squared_board == squared_board

def test_is_valid_soudoku(sudoku_board):
    assert soudoku.isValidSudoku(sudoku_board) == True