from random import randrange

def display_board(board):
    
    
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
   
    ok = False
    while not ok:
        move = input("Enter your move (1-9): ")
        if not (len(move) == 1 and move >= '1' and move <= '9'):
            print("Bad move - repeat your input!")
            continue
        
        move = int(move) - 1
        row = move // 3
        col = move % 3
        
        if board[row][col] in ['O', 'X']:
            print("Field already occupied - repeat your input!")
            continue
            
        board[row][col] = 'O'
        ok = True

def make_list_of_free_fields(board):
    
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['O', 'X']:
                free.append((r, c))
    return free

def victory_for(board, sign):
    
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

def draw_move(board):
    
    free = make_list_of_free_fields(board)
    if free:
        pick = randrange(len(free))
        row, col = free[pick]
        board[row][col] = 'X'


board = [[str(3 * j + i + 1) for i in range(3)] for j in range(3)]


board[1][1] = 'X'
display_board(board)

while True:
    
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break
    
    
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    
    print("Computer is thinking...")
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer won!")
        break

    
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break