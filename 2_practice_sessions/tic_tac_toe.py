# Tic-Tac-Toe

from random import randrange
import time

def display_board(board):
    time.sleep(1) # Slower time improves immersion
    print("+-------" * 3, "+", sep = "")
    for row in range(3):
        print("|       " * 3, "|", sep = "")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end = "")
        print("|")
        print("|       " * 3, "|", sep = "")
        print("+-------" * 3, "+", sep = "")
        
         
def enter_move(board):
	ok = False	# fake assumption - we need it to enter the loop
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
		if not ok:
			print("Bad move - repeat your input!") # no, it isn't - do the input again
			continue
		move = int(move) - 1 	# cell's number from 0 to 8
		row = move // 3 	# cell's row
		col = move % 3		# cell's column
		sign = board[row][col]	# check the selected square
		ok = sign not in ['O','X'] 
		if not ok:	# it's occupied - to the input again
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O'
	
	        
def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O", "X"]:
                free.append((row, col))
    return free
    
    
def victory_for(board, sgn):
            if sgn == "X":
                who = "me"
            elif sgn == "O":
                who = "you"
            else:
                who = None
            cross1 = cross2 = True
            for rc in range(3):
                if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
                    return who
                if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
                    return who
                if board[rc][rc] != sgn:
                    cross1 = False
                if board[2 - rc][2 - rc] != sgn:
                    cross2 = False
            if cross1 or cross2:
                return who
            return None
            
            
def draw_move(board):
            free = make_list_of_free_fields(board)
            cnt = len(free)
            if cnt > 0:
                this = randrange(cnt)
                row, col = free[this]
                board[row][col] = "X"
                
                
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = "X"
free = make_list_of_free_fields(board)
human_turn = True

while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, "O")
    else:
        draw_move(board)
        victor = victory_for(board, "X")
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)
    
    
display_board(board)
if victor == "you":
    print("Congrats - You have bested me.")
elif victor == "me":
    print("It seems I've won. Do better next time.")
else:
    print("We reached a stalemate.")