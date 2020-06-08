import random

# Functions
def display_board(board):
	print('\n' *100)
	print('   |   | ')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   | ')
	print('-----------')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   | ')
	print('-----------')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   | ')

def player_input():
	marker = ''
	while marker!= 'X' and marker!= 'O':
		marker = input('Choose a marker: X or O: ').upper()
	player1 = marker
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'


	return(player1,player2)

def place_marker(board,marker,position):
	board[position] = marker

def choose_first():
	if random.randint(0,1) == 1:
		return 'Player 1'
	else:
		return 'Player 2'

def win_check(board,mark):
	# Check row
	return((board[1] == board[2] == board[3] == mark) or	     
	(board[4] == board[5] == board[6] == mark) or				 			
	(board[7] == board[8] == board[9] == mark) or
	# Check column
	(board[1] == board[4] == board[7] == mark) or
	(board[2] == board[5] == board[8] == mark) or
	(board[3] == board[6] == board[9] == mark) or
	# Check diagonal
	(board[1] == board[5] == board[9] == mark) or
	(board[7] == board[5] == board[3] == mark))

def space_check(board,position):
	return board[position] == ' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True

def player_choice(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9,10] or not space_check(board,position):
		position = int(input('Choose a Number(1-9):'))

	return position

def replay():
	play = input('Do you want to play again? Y/N').upper()
	return play == 'Y'

# Main code
print('Welcome to Tic Tac Toe!')

while True:
	# Set up game
	board = [' '] *10
	display_board(board)
	player1_marker, player2_marker = player_input()

	# Decide who goes first
	# turn = choose_first()
	# print(turn + ' Will go first')
	turn = 'Player 1'

	# Ask if ready
	ready = input('Are you ready to play? Y/N').upper()
	if ready == 'Y':
		on = True
	else:
		on = False

	while on == True:
		if turn == 'Player 1':
			# Player 1 turn
			display_board(board)
			# choose position
			position = player_choice(board)
			place_marker(board,player1_marker,position)
			# check for win
			if win_check(board,player1_marker):
				display_board(board)
				print('Player 1 has won!')
				on = False
			else:
				# check for tie
				if full_board_check(board):
					display_board(board)
					print('Game Tied')
					break
				else:
					turn = 'Player 2'

		else:
			if turn == 'Player 2':
				# player 2 turn
				display_board(board)
				# choose position
				position = player_choice(board)
				place_marker(board,player2_marker,position)
				# check for win
				if win_check(board,player2_marker):
					display_board(board)
					print('Player 2 has won!')
					on = False
				else:
					# check for tie
					if full_board_check(board):
						display_board(board)
						print('Game Tied')
						break
					else:
						turn = 'Player 1'
	if not replay():
		break









