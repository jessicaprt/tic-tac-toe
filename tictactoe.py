'''
Jessica Prieto and Irene Gao

##### THE IMPOSSIBLE TIC TAC TOE GAME! #####

the goal is to generate moves for the computer such that the
computer is undefeated: either it always wins, or the game
results in a draw

nodes: (for reference)
	 0 | 1 | 2 
	 3 | 4 | 5
	 6 | 7 | 8

'''

from board import Board
from tkinter import *
from tkinter import messagebox
import board
import tkinter
import random


root = Tk()
root.title("tic tac toe (AN IMPOSSIBLE GAME)")


''' INITIALIZE GLOBAL VARIABLES '''
#if player = True: x
#if player = False: y
#initialized to True, will be changed after select
player = True

b = Board()
var = IntVar()
strn = StringVar()
strn2 = StringVar()
strn.set("Step 1: SELECT A PLAYER")
strn2.set("Step 2: Choose who starts")

class Application(Frame):
	'''front-end of the program'''	
	def sel(self):
		''' helper function for the radio buttons '''
		global player
		label = Label(root)

		#ater choosing a player in step 1, disable radio buttons
		self.X["state"] = "disabled"
		self.O["state"] = "disabled"

		#enable the board for playing!
		if self.play["state"] == "disabled":
			self.move0["state"] = "normal"
			self.move1["state"] = "normal"
			self.move2["state"] = "normal"
			self.move3["state"] = "normal"
			self.move4["state"] = "normal"
			self.move5["state"] = "normal"
			self.move6["state"] = "normal"
			self.move7["state"] = "normal"
			self.move8["state"] = "normal"

		if var.get() == 1: #playre "X" is selected
			player = True
			strn.set("Your player : X")
		elif var.get() == 2: #player "O" is selected
			player = False
			strn.set("Your player : O")

	def initmove(self):
		global player
		label2 = Label(root)

		if player == True:
			y = "X"
		else:
			y = "O"

		#disable radio buttons after player selects who goes first
		self.play["state"] = "disabled"
		self.comp["state"] = "disabled"
		if self.X["state"] == "disabled":
			#enable board for playing!
			self.move0["state"] = "normal"
			self.move1["state"] = "normal"
			self.move2["state"] = "normal"
			self.move3["state"] = "normal"
			self.move4["state"] = "normal"
			self.move5["state"] = "normal"
			self.move6["state"] = "normal"
			self.move7["state"] = "normal"
			self.move8["state"] = "normal"

		if var.get() == 3: #player starts
			strn2.set("You start")
		elif var.get() == 4: #computer starts
			strn2.set("Computer starts")
			self.comp_player(9)

	def makemove(self, node):
		global player
		global b

		print(node)
		if node == 0:
			button = self.move0
		elif node == 1:
			button = self.move1
		elif node == 2:
			button = self.move2
		elif node == 3:
			button = self.move3
		elif node == 4:
			button = self.move4
		elif node == 5:
			button = self.move5
		elif node == 6:
			button = self.move6
		elif node == 7:
			button = self.move7
		elif node == 8:
			button = self.move8

		if player == True and button["text"] == "  ":
			y = "X"
		elif player == False and button["text"] == "  ":
			y = "O"
		else:
			raise ValueError("choose another button")

		button["text"] = y

		check = b.move(y, node)
		if (check == True) or (b.check_full_draw == True):
			self.newgame()
		else:
			self.comp_player(node)


	def comp_player(self, node):
		''' generates the move in the input node for the computer'''

		global player
		global b

		player = not player
		if player == True:
			y = 'X'
		else:
			y = 'O'

		check = False

		#node = 9 if the player asks the computer to do the first move
		if node == 9:
			#generate random move
			move = random.randrange(9)
		else:
			# CALL MINIMAX TO CALCULATE NEXT MOVE
			move = self.minimax(b, node, player)
		if move == 0:
			self.move0["text"] = y
			check = b.move(y, 0)
		elif move == 1:
			self.move1["text"] = y
			check = b.move(y, 1)
		elif move == 2:
			self.move2["text"] = y
			check = b.move(y, 2)
		elif move == 3:
			self.move3["text"] = y
			check = b.move(y, 3)
		elif move == 4:
			self.move4["text"] = y
			check = b.move(y, 4)
		elif move == 5:
			self.move5["text"] = y
			check = b.move(y, 5)
		elif move == 6:
			self.move6["text"] = y
			check = b.move(y, 6)
		elif move == 7:
			self.move7["text"] = y
			check = b.move(y, 7)
		elif move == 8:
			self.move8["text"] = y
			check = b.move(y, 8)
		elif move == -1:
			#draw
			messagebox.showinfo("tic tac toe", "IT'S A DRAW!")
			self.newgame()

		if (check == True) or (b.check_full_draw == True): #player wins
			self.newgame()
		else:
			player = not player	

	def empty_board(self):
		''' clears the GUI '''

		global player 
		self.move0["text"] = "  "
		self.move1["text"] = "  "
		self.move2["text"] = "  "
		self.move3["text"] = "  "
		self.move4["text"] = "  "
		self.move5["text"] = "  "
		self.move6["text"] = "  "
		self.move7["text"] = "  "
		self.move8["text"] = "  "

		b.clearBoard()
		
	def newgame(self):
		''' starts a new game 
		also a helper function for the 'NEW GAME' button '''

		global player
		global var
		
		self.empty_board()
		self.move0["state"] = "disabled"
		self.move1["state"] = "disabled"
		self.move2["state"] = "disabled"
		self.move3["state"] = "disabled"
		self.move4["state"] = "disabled"
		self.move5["state"] = "disabled"
		self.move6["state"] = "disabled"
		self.move7["state"] = "disabled"
		self.move8["state"] = "disabled"
		strn.set("Setp 1: SELECT A PLAYER")
		strn2.set("Step 2: Choose who starts")
		self.X["state"] = "active"
		self.O["state"] = "active"
		self.play["state"] = "active"
		self.comp["state"] = "active"

	def minimax(self, board, node, player):
		'''MINIMAX ALGORITHM
		calculates the score generated each time through depth first search:
		if player wins : score = depth - 10
		if computer wins : score = 10 - depth
		'''

		def getmaxscore(val):
			'''helper function for max_val'''
			#print(val)
			curr_max = -100
			best = 0

			if val == []:
				return (-1,-1)

			for succ in val: #(succ, score)
				curr_max = max(curr_max, succ[1])
				if curr_max == -100:
					raise ValueError("max error")
				if succ[1] == curr_max:
					best = succ

			return best

		def getminscore(val): #val = (succ, score)
			'''helper function foe min_val'''
			#print(val)
			curr_min = 100
			best = 0

			if val == []:
				return (-1,-1)

			for succ in val:
				curr_min = min(curr_min, succ[1])
				if curr_min == 100:
					raise ValueError("min error")
				if succ[1] == curr_min:
					best = succ

			return best


		def max_val(board, node, y, z, score, depth):
			b_buf = Board()
			b_buf = board.copy_temp()
			m_buf = b_buf.empty_moves()

			all_val = []
			for succ in m_buf:
				b_buf.temp_move(z, succ)
				if b_buf.check_win(z):
					score = 10-depth
					val = (succ, score)
					all_val.append(val)
					b_buf.del_move(z,succ)

				elif b_buf.check_draw(y,z):
					val = (succ, 0)
					all_val.append(val)
					b_buf.del_move(z,succ)

				else:
					depth = depth + 1
					buf = min_val(b_buf, succ, y, z, score, depth)
					val = (succ, buf[1])
					all_val.append(val)
					b_buf.del_move(z,succ)

			maxscore = getmaxscore(all_val)


			return maxscore

		def min_val(board, node, y, z, score, depth):
			#initialize temporary board for checking the moves
			b_buf = Board()
			b_buf = board.copy_temp()
			m_buf = b_buf.empty_moves()

			all_val = [] #list of tuples: (succ, score)
			for succ in m_buf:
				b_buf.temp_move(y, succ)
				if b_buf.check_win(y):
					score = depth - 10
					val = (succ, score)
					all_val.append(val)
					b_buf.del_move(y,succ)
				elif b_buf.check_draw(y,z):					
					val =(succ, 0)
					all_val.append(val)
					b_buf.del_move(y,succ)
				else:
					depth = depth + 1
					buf = max_val(b_buf, succ, y, z, score, depth) #(succ, score)
					val = (succ, buf[1]) #succ : the next node, buf[1] : max score generated by max_val
					all_val.append(val)

			minscore = getminscore(all_val)

			return minscore #tuple with minimum score : (next node, minimum score)

		if player == True:
			y = "X"
			z = "O"
		else:
			y = "O"
			z = "X"

		minimax_val = max_val(b, node, y, z, 0, 0)

		#print("NEXT MOVE:")
		#print(minimax_val[0])
		return minimax_val[0]

	def createWidgets(self):
		'''GUI properties'''

		fnt = 'Arial 30 bold'
		pad = 30
		w = 5
		h = 3

		#initialize nodes on the board
		self.move0 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")
		self.move1 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")
		self.move2 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")
		self.move3 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")
		self.move4 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")
		self.move5 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")
		self.move6 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")
		self.move7 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")
		self.move8 = Button(self, text = "  ", height = h, width = w, font = fnt, \
			activebackground = 'black', activeforeground = 'green', state = "disabled")

		#for node 0
		self.move0["command"] = lambda: self.makemove(0)
		self.move0.config(bg ='black', fg = 'green')
		self.move0.grid({"row" : 1, "column" : 0})

		#for node 1
		self.move1["command"] = lambda: self.makemove(1)
		self.move1.config(bg ='black', fg = 'green')
		self.move1.grid({"row" : 1, "column" : 1})

		#for node 2
		self.move2["command"] = lambda: self.makemove(2)
		self.move2.config(bg ='black', fg = 'green')
		self.move2.grid({"row" : 1, "column" : 2})

		#for node 3
		self.move3["command"] = lambda: self.makemove(3)
		self.move3.config(bg ='black', fg = 'green')
		self.move3.grid({"row" : 2, "column" : 0})

		#for node 4
		self.move4["command"] = lambda: self.makemove(4)
		self.move4.config(bg ='black', fg = 'green')
		self.move4.grid({"row" : 2, "column" : 1})

		#for node 5
		self.move5["command"] = lambda: self.makemove(5)
		self.move5.config(bg ='black', fg = 'green')
		self.move5.grid({"row" : 2, "column" : 2})

		#for node 6
		self.move6["command"] = lambda: self.makemove(6)
		self.move6.config(bg ='black', fg = 'green')
		self.move6.grid({"row" : 3, "column" : 0})

		#for node 7
		self.move7["command"] = lambda: self.makemove(7)
		self.move7.config(bg ='black', fg = 'green')
		self.move7.grid({"row" : 3, "column" : 1})

		#for node 8
		self.move8["command"] = lambda: self.makemove(8)
		self.move8.config(bg ='black', fg = 'green')
		self.move8.grid({"row" : 3, "column" : 2})

		#for the radio buttons (choosing a player)
		label_text = Label(root, textvariable = strn, relief=RAISED)
		label_text["relief"] = "flat"
		label_text["pady"] = 10
		label_text.pack()
		self.X = Radiobutton(root, text="X", variable=var, value=1,
                  command=self.sel)
		self.X.pack( anchor = CENTER )
		self.O = Radiobutton(root, text="O", variable=var, value=2,
                  command=self.sel)
		self.O.pack( anchor = CENTER )

		#for the radio buttons (choosing who starts first)
		label2_text = Label(root, textvariable = strn2, relief=RAISED)
		label2_text["relief"] = "flat"
		label2_text["pady"] = 10
		label2_text.pack()
		self.play = Radiobutton(root, text="I start", variable=var, value=3,
                  command=self.initmove)
		self.play.pack( anchor = CENTER )
		self.comp = Radiobutton(root, text="Comp starts", variable=var, value=4,
                  command=self.initmove)
		self.comp.pack( anchor = CENTER )

		#QUIT BUTTON
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit
		self.QUIT["width"] = 10
		self.QUIT.grid({"row" : 5, "column" : 0})

		#NEW GAME BUTTON
		self.NEWGAME = Button(self)
		self.NEWGAME["text"] = "New Game"
		self.NEWGAME["fg"] = "blue"
		self.NEWGAME["command"] = self.newgame
		self.NEWGAME["width"] = 10
		self.NEWGAME.grid({"row" : 5, "column" : 2})
		

	def __init__(self, master = None):
		label = Label(root)
		Frame.__init__(self, master)

		self.pack()
		self.createWidgets()


root.geometry("450x620")
app = Application(master=root)
app.mainloop()