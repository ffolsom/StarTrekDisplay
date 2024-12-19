## Another star trek display ##
## Fred Folsom (C)8/11/2024 V1.0
from graphics import *
import time
import random
random.seed()
colorZone1=['yellow','white','silver']
colorZone2=['yellow','green','blue','teal','orange']
colorZone3=['orange','red','green']

win = GraphWin('Star Trek Display 2',1055,600)
win.setBackground('black') 

def main():


	rand1 = (random.randint(0,100))
	x = (random.randint(0,6))*145
	y = (random.randint(0,10))*55
	w = x + 145
	h = y + 55

	if rand1 in range(0,50):								# turn on/ off one block at random duration 50%
		if y in range(0,200):
			colorx=(random.choice(colorZone1))
		if y in range(200,400):
			colorx=(random.choice(colorZone2))
		if y in range(400,600):
			colorx=(random.choice(colorZone3))	

		time.sleep(random.random())							#Turn on Blocks
		disp = Rectangle(Point(x+5,y+5), Point(w, h))
		disp.setFill(colorx)
		disp.draw(win)
		if rand1 in range(50,100):							# Turn off same block 25% of tehe time
			time.sleep(random.random())						
			disp = Rectangle(Point(x+5,y+5), Point(w, h))
			disp.setFill('black')
			disp.draw(win)

	if rand1 in range(50,100):								# Turn on one random block 50%
		if y in range(0,200):
			colorx=(random.choice(colorZone1))
		if y in range(200,400):
			colorx=(random.choice(colorZone2))
		if y in range(400,600):
			colorx=(random.choice(colorZone3))	
		time.sleep(random.random())							#Turn on Blocks
		disp = Rectangle(Point(x+5,y+5), Point(w, h))
		disp.setFill(colorx)
		disp.draw(win)

	if rand1 in range(25,75):								# Turn off one random block 50%
		time.sleep(random.random())						
		disp = Rectangle(Point(x+5,y+5), Point(w, h))
		disp.setFill('black')
		disp.draw(win)

	return()

while win.checkMouse() is None:
	main()
win.close()
print('display2.py V1.0 ended')


