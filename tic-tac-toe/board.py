from tkinter import messagebox
import random

class Board:
	'''back-end of the program'''
	def __init__(self):
		'''initializes the board'''
		self.board = [" "]*9

	def __repr__(self):
		'''printing the "permanent board" on the terminal'''
		return "%s | %s | %s \n%s | %s | %s \n%s | %s | %s \n" % \
				(self.board[0], self.board[1], self.board[2], \
				self.board[3], self.board[4], self.board[5], \
				self.board[6], self.board[7], self.board[8])

	def check_win(self, y):
		''' checks if the player won

		input arguments:
			- self - checks the board
			- y - the player's character ('X' or 'O')
		returns True if that player won'''
		
		wins = (self.board[0] == y and self.board[1] == y and self.board[2] == y) or \
				(self.board[3] == y and self.board[4] == y and self.board[5] == y) or \
				(self.board[6] == y and self.board[7] == y and self.board[8] == y) or \
				(self.board[0] == y and self.board[3] == y and self.board[6] == y) or \
				(self.board[1] == y and self.board[4] == y and self.board[7] == y) or \
				(self.board[2] == y and self.board[5] == y and self.board[8] == y) or \
				(self.board[0] == y and self.board[4] == y and self.board[8] == y) or \
				(self.board[2] == y and self.board[4] == y and self.board[6] == y)
		return wins

	def check_draw(self, y, z):
		''' (called by the "temporary board" 
		checks if it's a draw only on the case if the board is full
		and neither the player nor the computer won the game'''
		if (self.empty_moves() == []) and (self.check_win(y)== False) and (self.check_win(z) == False):
			#messagebox.showinfo("tic tac toe", "IT'S A DRAW!")
			return True
		else:
			return False

	def check_full_draw(self):
		''' (called by the "permanent board" 
		checks if it's a draw only on the case if the board is full
		and neither the player nor the computer won the game'''
		if self.empty_moves() == []:
			print("DRAW!")
			messagebox.showinfo("tic tac toe", "IT'S A DRAW!")
			return True
		else:
			return False

	def is_empty(self, idx):
		'''checks if a node is empty
		returns True if it's empty'''

		if self.board[idx] == " ":
			return True
		else:
			return False 

	def empty_moves(self):
		'''generates a list of all empty moves'''

		moves = []
		for i in range(9):
			if self.is_empty(i):
				moves.append(i)
		return moves

	def move(self, y, idx):
		''' places a move on the "permanent board"
		returns True if y wins, and False otherwise'''
		check_empty = self.is_empty(idx)
		if idx >=0 and idx < 9 and check_empty == True:
			self.board[idx] = y
		else:
			print("Y: %s" % y)
			print(self)
			raise ValueError("Invalid move")

		print(self)

		if self.check_win(y) == True:
			messagebox.showinfo("tic tac toe", "%s WINS, Start New Game?" % y)
			print("%s WINS" % y)
			#self.clearBoard()
			return True

		else:
			return False

	def temp_move(self, y, idx):
		''' places a move on the "temporary board"
		returns True if y wins, and False otherwise'''
		check_empty = self.is_empty(idx)
		if idx >=0 and idx < 9 and check_empty == True:
			self.board[idx] = y

		win = self.check_win(y)
		#if win == True:
			#print("%s gen win.." % y)

	def copy_temp(self):
		'''makes a copy of the permanent board to a temporary board to be used to check
		the moves on each node'''
		b_buf = Board()
		for i in range(9):
			b_buf.board[i] = self.board[i]

		return b_buf

	def del_move(self, y, idx):
		'''removes a move on the node
		can only be called by the "temporary board" '''
		check_empty = self.is_empty(idx)
		if idx >=0 and idx <9 and check_empty == False:
			self.board[idx] = " "
		else:
			raise ValueError("Invalid delete")

	def clearBoard(self):
		'''Clears the board for a new game'''
		self.board = [" "]*9