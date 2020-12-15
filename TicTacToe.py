# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent
# Eric Broadbent
# 11/20

# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


# Build Functions
#################################################
def display_instruct():
    """Display game instructions. to use simply type (display_instruct())"""
    print("""
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a number, 0 - 8.  The number 
    will correspond to the board position as illustrated:
    
                    \t0 | 1 | 2
                    \t---------
                    \t3 | 4 | 5
                    \t---------
                    \t6 | 7 | 8

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """)

def next_turn(turn):
    """this function switches the turn in the game. to use (turn = next_turn(turn))"""
    if turn == X:
        return O
    else:
        return X

def pieces():
    """Determine if player or computer goes first. to use ( computer,human = pieces() )"""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y" or go_first == "yes":
        print("\nThen take the first move.  You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        human = O
        computer = X
    return computer, human


def ask_yes_no(questions):
    """Ask a yes or no question and get back a yes or no naswer.to use (answer = ask_yes_no(questions)) """
    response = None
    while response not in ("y", "n","no","yes"):
        response = input(questions).lower()
    return response

def new_board():
    """Create new game board. to use ( board = new_board())"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display game board on screen. to use ( display_board(board) )"""
    print("\t",board[0],"|",board[1],"|",board[2])
    print("\t", "---------")
    print("\t",board[3],"|",board[4],"|",board[5])
    print("\t", "---------")
    print("\t",board[6],"|",board[7],"|",board[8])

def legalMoves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
            
def human_move(board, human) :
    """Get human move. to use ( move = human_move(board, human)""" 
    legal = legalMoves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nN O. The square is already taken.\n")
    return move

def ask_number(question, low, high):
    """Ask for a number within a range. to use (answer = ask_number(question, low, high))"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response    
def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN = ( (0, 1, 2) ,
                                      (3, 4, 5),
                                      (6, 7, 8),
                                      (0, 4, 8),
                                      (2, 4, 6),
                                      (0, 3, 6),
                                      (2, 5, 8),
                                      (1, 4, 7))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None
def computerMove(board, computer, human):
    """Make computer move."""
    cboard = board[:]
    # ^ make board copy ^
    # v best moves            v
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I'll take square number", end = " ")
    # if computer can win, take that move
    for move in legalMoves(board):
        cboard[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking, undo it
        cboard[move] = EMPTY
    for move in legalMoves(board):
        cboard[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking, undo it
        cboard[move] = EMPTY
    for move in BEST_MOVES:
        if move in legalMoves(board):
            print(move)
            return move
    
            
##################################################
# main game
def main():
    display_instruct()# testing display_instruct
    turn = X
    computer,human = pieces()
    board = new_board()
    display_board(board)
    win = None
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move]= human
        else:
            move = computerMove(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    win = winner(board)
    print(win)
    
        




main()
