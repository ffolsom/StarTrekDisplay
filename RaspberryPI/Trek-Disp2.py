#Python computer simulation from Star Trek TOS
from graphics import *
import time					# For Sleep function
import random					# Random function library
random.seed()					# Uses time
G = 'Khaki4'					# OliveDrab4
Y = 'DarkGoldenRod3'
O = 'Tomato2'
B = 'Black'
col_tot = 15 
#[col #, x, xoff, cols,yoff, colorx8]
col0_15 = [[0,0,0.75,8,-0.75,G,B,B,B,B,B,B,O],
           [1,1,0.75,8,-0.75,G,B,Y,B,B,B,O,B],
           [2,2,0.75,8,-0.75,G,G,B,Y,B,O,B,B],    #First 2 G blink together
           [3,3,0.75,8,-0.75,G,B,B,B,Y,B,B,O],
           [4,4,0.75,8,-0.75,G,B,Y,B,B,B,O,B],
           [5,5,0.75,8,-0.75,G,B,B,Y,B,O,B,B],
           [6,6,0.75,8,-0.75,G,B,B,B,Y,B,B,O],
           [7,7,0.75,8,-0.75,G,B,Y,B,B,O,B,B],
           [8,8,0.75,8,-0.75,G,B,B,Y,B,O,B,B],
           [9,9,0.75,8,-0.75,G,B,B,B,Y,B,B,O],
           [10,10,0.75,8,-0.75,G,B,Y,B,B,B,O,B],
           [11,11,0.75,8,-0.75,G,B,B,Y,B,O,B,B],
           [12,12,0.75,8,-0.75,G,B,B,O,B,B,B,O],
           [13,13,0.75,8,-0.75,G,B,B,B,O,B,O,B],
           [14,14,0.75,8,-0.75,G,Y,B,Y,B,O,B,B],	#(thinner).  GY blink together
           [15,15,15,3,15.35,G,Y,O,B,B,B,B,B]]   	#Right most verticals x3
#col_ = [15,15,G,Y,O] #(special, 3 vert, top one is taller than matrix GGYYOO

win = GraphWin('Star Trek TOS Computer', 1055, 600) 	#1550,400 Define Window
win.setBackground('Black')				#Set window background color
win.setCoords(0, -12,16,2)				#Start (xll,yll,xur,yur) (0,-12,1,1)
prob1 = 0.6
prob2 = 0.8
lites_per_col = 18					#Rectangles / column
disp = [None]*20					#List of rectangle cpmmands / Spock's display

def win_setup():
	global d					#var for far right column
	for x in range(0,20):				#Fill list / matrix
		disp[x] = [None]*lites_per_col 		#List of lists (lites_per_col)

	for x in range(0,15):				#Data Down
		for y in range(5,13): 			#Data accross
			#x+q horiz size, y+r virt size. Rectange command list
			disp[x][y+5] = Rectangle(Point(x, -y+5),Point(x+.75, -y+5+-.75))
			disp[x][y+5].draw(win)		#Draw color/display
	d = x+1						#d=x coord for right column
	disp[x+1][5] = Rectangle(Point(15,-1.8), Point(15.35,0.85))
	disp[x+1][5].draw(win)
	disp[x+1][6] = Rectangle(Point(15,-4.7), Point(15.35,-2.1))
	disp[x+1][6].draw(win)
	disp[x+1][7] = Rectangle(Point(15,-8), Point(15.35,-5))
	disp[x+1][7].draw(win)
	return()

def blink_lites3():					#Blink lights at random
	global d
	a = int(random.random()*16)			#Column col0_15[x][]
	b = int(random.random()*8)+5			#Column col0_15[x][0] is num skip
	c = random.random()
	clr = col0_15[a][b]
	#if, elif, else == Case-like statement
	if True:
		if a in (2,14):				#3rd col, top 2 lights blink together
			if a == 2:			#if 2 use green for top pair
				col_a = G; col_b = G
			else:
				col_a = G; col_b = Y
			if b in (5,6):
				if c > prob1:		#if prob > p, blink off
					disp[a][5+5].setFill('Black') #Blink top pair off
					disp[a][6+5].setFill('Black') #Blink top pair off
				else:
					disp[a][5+5].setFill(col_a) #Blink top pair on
					disp[a][6+5].setFill(col_b) #Blink top pair on
			elif c > prob2:				#if not 5 or 6, different prob
				disp[a][b+5].setFill('Black')	#Blink 1 off
			else:
				disp[a][b+5].setFill(clr)	#Blink 1 on  

		elif a == 15:					#Right most colunn 3 virticals
			e = random.randint(5,7)			#virt 0-2 (1-3)
			clr2 = col0_15[15][e]			#col0_15 List only goes 0-15 for now
			if disp[d][e] !=None:			#If not empty
				if c > prob2:			#Sepcial cases: col 16, virtl-3
					disp[d][e].setFill('Black') #Blink off
				else:
					disp[d][e].setFill(clr2) #Blink on
			else:
				if disp[a][b+5] != None:	#if not blank
					if c > prob1:
						 disp[a][b+5].setFill('Black') #Blink off
					else:
						 disp[a][b+5].setFill(clr) #Blink on
		return()

def blink_lites2():					#Blink lights at random
	global d
	a = int(random.random()*16)			#Column col0_15[x][]
	b = int(random.random()*8)+5			#Column col0_15[x][0] is num skip
	c = random.random()
	clr = col0_15[a][b]

	if a in (2,14):			#3rd col, top 2 lights blink together
		if a == 2:			#if 2 use green for top pair
			col_a = G; col_b = G
		else:
			col_a = G; col_b = Y
		if b in (5,6):
			if c > prob1:		#if prob > p, blink off
				disp[a][5+5].setFill('Black') #Blink top pair off
				disp[a][6+5].setFill('Black') #Blink top pair off
			else:
				disp[a][5+5].setFill(col_a) #Blink top pair on
				disp[a][6+5].setFill(col_b) #Blink top pair on
		elif c > prob2:				#if not 5 or 6, different prob
			disp[a][b+5].setFill('Black')	#Blink 1 off
		else:
			disp[a][b+5].setFill(clr)	#Blink 1 on 

	elif a == 15:					#Right most colunn 3 virticals
			e = random.randint(5,7)			#virt 0-2 (1-3)
			clr2 = col0_15[15][e]			#col0_15 List only goes 0-15 for now
			if disp[d][e] !=None:			#If not empty
				if c > prob2:			#Sepcial cases: col 16, virtl-3
					disp[d][e].setFill('Black') #Blink off
				else:
					disp[d][e].setFill(clr2) #Blink on

	if disp[a][b+5] != None:	#if not blank - Blink main lights
		if c > prob1:
			disp[a][b+5].setFill('Black') #Blink off
		else:
		 	disp[a][b+5].setFill(clr) #Blink on

		return()

def test():
	global d
	a = int(random.random()*16)			#Column col0_15[x][]
	b = int(random.random()*8)+5			#Column col0_15[x][0] is num skip
	c = random.random()
	clr = col0_15[a][b]
	#if, elif, else == Case-like statement
	print('a,b,c', a,b,c )
	if a in (0,1,3,4,5,6,7,8,9,10,11,12,13):
		if b in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15):
			#disp[a][b].setFill('Red') #Blink on 
			print (disp[a][b])
	return()


## MAIN ##
win_setup()
while win.checkMouse() is None:
	#test()
	blink_lites2()			#Blink lites routine
	time.sleep(.007)		#Wait time for light changes
	#blink_lites2()			#Blink lites routine
win.getMouse()				#Wait for mouse click to get next set
win.close()

print('fcf-trek.py ended')
