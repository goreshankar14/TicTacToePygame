import pygame
import sys,time
pygame.init()
Screen_Width=300
Screen_Height=300
win=pygame.display.set_mode((Screen_Width,Screen_Height))
chance=0
pygame.display.set_caption(" XO ")
icon=pygame.image.load("xo.png")
pygame.display.set_icon(icon)
os=pygame.image.load("letter-o.png")
xs=pygame.image.load("letter-x.png")
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
clock=pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
row,col=0,0
occupied=[[0,0,0],[0,0,0],[0,0,0]]
winner=0
status=0
addition=0

def player_won():
	time.sleep(1)
	global chance
	win.fill(white)
	if chance==1:
		text = font.render(" O Won ", True, black)
		win.blit(text, (120,100))
		pygame.display.update()
	else:
		text = font.render(" X Won ", True, black)
		win.blit(text, (120,100))
		pygame.display.update()
	time.sleep(1)
	start()

def match_tied():
	time.sleep(1)
	win.fill(white)
	text = font.render(" Match Tied ", True, black)
	win.blit(text, (110,100))
	pygame.display.update()
	time.sleep(1)
	start()
	
def checkTieOrWin():
	global occupied,chance,winner
	if winner==0:
		for i in range(0,3):
			if (occupied[i][0]==occupied[i][1]==occupied[i][2]) and occupied[i][1]!=0:
				if i==0:
					winner=1
					break
				elif i==1:
					winner=1
					break
				elif i==2:
					winner=1
					break
			elif (occupied[0][i]==occupied[1][i]==occupied[2][i]) and occupied[1][i]!=0:
				if i==0:
					winner=1
					break
				elif i==1:
					winner=1
					break
				elif i==2:
					winner=1
					break
	if winner==0:
		if (occupied[0][0]==occupied[1][1]==occupied[2][2]) and occupied[0][0]!=0:
			winner=1

	if winner==0:
		if (occupied[0][2]==occupied[1][1]==occupied[2][0]) and occupied[1][1]!=0:
			winner=1
	return winner

def drawxo(row,col):
	global chance,occupied,status,addition
	if row==0:
		y=18
	elif row==1:
		y=119
	elif row==2:
		y=219
	if col==0:
		x=18
	elif col==1:
		x=119
	elif col==2:
		x=219
	occupied[row][col]=chance+2
	if chance==0:
		win.blit(os,(x,y))
		chance=1
	else:
		win.blit(xs,(x,y))
		chance=0
	pygame.display.update()
	status=checkTieOrWin()
	if status==1:
		player_won()
	elif sum(sum(occupied,[]))==22:
		match_tied()

def clicked():
	global row,col,occupied
	x=pygame.mouse.get_pos()[0]
	y=pygame.mouse.get_pos()[1]
	if y<99:
		row=0
	elif y>101 and y<199:
		row=1
	elif y>201:
		row=2
	if x<99:
		col=0
	elif x>101 and x<199:
		col=1
	elif x>201:
		col=2
	if (row in [0,1,2]) and (col in [0,1,2]) and occupied[row][col]==0:
		drawxo(row,col)

def start():
	global row,col,occupied,chance,winner,status,addition
	occupied=[[0,0,0],[0,0,0],[0,0,0]]
	row,col=0,0
	chance,winner,status,addition=0,0,0,0
	win.fill(white)
	pygame.draw.line(win,black,(Screen_Width//3,0),(Screen_Width//3, Screen_Height),3)
	pygame.draw.line(win,black,(Screen_Width//3*2,0),(Screen_Width//3*2, Screen_Height),3)
	pygame.draw.line(win,black,(0,Screen_Height//3),(Screen_Width, Screen_Height//3),3)
	pygame.draw.line(win,black,(0,Screen_Height//3*2),(Screen_Width, Screen_Height//3*2),3)
	pygame.display.update()

start()

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		if event.type==pygame.MOUSEBUTTONDOWN:
			if winner==0:
				clicked()
	pygame.display.update()
	clock.tick(30)
