import random

board = [""] * 9  # Supponendo una griglia 3x3

def reset():
    for i in range(len(board)):
        board[i] = ""
        
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
    # Tutte le possibili combinazioni vincenti
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # righe
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonne
        [0, 4, 8], [2, 4, 6]              # diagonali
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]  # "1" per player, "0" per CPU
    return ""