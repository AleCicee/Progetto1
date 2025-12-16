import random

board = [""] * 9  # Supponendo una griglia 3x3

def reset():
    board.clear()
        
def printBoard():
    for element in board:
        print(element)

def make_move(playerMove):
    if board[playerMove] == "":
        board[playerMove] = "1"
    else:
        print("Mossa non valida!")
        return
    
    empty_cells = []
    
    # Mossa del computer (sceglie una cella vuota a caso)
    for i,k in enumerate(board):
        if k == "":
            empty_cells.append(i)
            
    if empty_cells:
        cpuMove = random.choice(empty_cells)
        board[cpuMove] = "0"
        print(f"Il computer ha mosso in posizione {cpuMove}")
        return cpuMove
    else:
        print("Nessuna mossa disponibile per il computer.")
        return ""
    
    # 0 1 2
    # 3 4 5
    # 6 7 8
    
def check_win():
    check_win = ""
    
    if board[0] == "1" and board[1] == "1" and board[2] == "1":
        check_win = "1"
    if board[3] == "1" and board[4] == "1" and board[5] == "1":
        check_win = "1"
    if board[6] == "1" and board[7] == "1" and board[8] == "1":
        check_win = "1"
    if board[0] == "1" and board[3] == "1" and board[6] == "1":
        check_win = "1"
    if board[1] == "1" and board[4] == "1" and board[5] == "1":
        check_win = "1"
    if board[2] == "1" and board[5] == "1" and board[8] == "1":
        check_win = "1"
    if board[0] == "1" and board[4] == "1" and board[8] == "1":
        check_win = "1"
    if board[2] == "1" and board[4] == "1" and board[6] == "1":
        check_win = "1"
        
    if board[0] == "0" and board[1] == "0" and board[2] == "0":
        check_win = "0"
    if board[3] == "0" and board[4] == "0" and board[5] == "0":
        check_win = "0"
    if board[6] == "0" and board[7] == "0" and board[8] == "0":
        check_win = "0"
    if board[0] == "0" and board[3] == "0" and board[6] == "0":
        check_win = "0"
    if board[1] == "0" and board[4] == "0" and board[5] == "0":
        check_win = "0"
    if board[2] == "0" and board[5] == "0" and board[8] == "0":
        check_win = "0"
    if board[0] == "0" and board[4] == "0" and board[8] == "0":
        check_win = "0"
    if board[2] == "0" and board[4] == "0" and board[6] == "0":
        check_win = "0"
        
    return check_win