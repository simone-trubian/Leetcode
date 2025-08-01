def is_unique(line):
    elements = [x for x in line if x != "."]
    return len(elements) == len(set(elements))

def transpose(board):
    transposed_board = []
    for i in range(len(board)):
        transposed_board.append([x[i] for x in board])
        
    return transposed_board

def square_board(board):
    step = 3
    squared_board = []
    slices = [(x, x + step) for x in range(0, len(board), step)]
    
    # Create the slices for the horizontal scan
    for outer_start, outer_end in slices:
        # Create the loop for the vertical scan
        for inner_start, inner_end in slices:
            line = []
            # Create the loop flattening the 3X3 square in a 9-element list
            for index in range(inner_start, inner_end):
                line.extend(board[index][outer_start:outer_end])
        
            squared_board.append(line)

    return squared_board    
    

def isValidSudoku(board):
    is_correct = []
    across = list(map(is_unique, [x for x in board]))
    is_correct.extend(across)
    
    transposed_board = transpose(board)
    down = list(map(is_unique, [x for x in transposed_board]))
    is_correct.extend(down)

    squared_board = square_board(board)
    squared = list(map(is_unique, [x for x in squared_board]))
    is_correct.extend(squared)

    return len([x for x in is_correct if not x]) == 0