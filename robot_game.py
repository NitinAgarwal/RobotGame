
	
print ("enter the size of the field (>=30):" )
field = int(raw_input())

import curses
from curses import initscr, curs_set, newwin, endwin, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, start_color, init_pair, COLOR_RED, COLOR_BLACK, color_pair, beep
import random
from random import randrange
stdscr = initscr()
start_color()    
#curses.beep()		#for attenuating the sound 
curses.curs_set(0)

class Robot:
  def __init__(self):
      self.size_field = 30
      self.size_robot = 5
      self.num_codes = 3
      self.d = 3
      self.brk = 0
      self.count = 0
      self.score = 10
        
  def delete(self, x_pos, y_pos):
      for i in range(self.size_robot): 
         win.addstr(x_pos+i, y_pos, " " * self.size_robot)
      
  def insert(self, x_pos, y_pos):
      for i in range(self.size_robot): 
         win.addstr(x_pos+i, y_pos, robot[i])
   
  def quit_game(self, size):
      curses.endwin()
      if self.count == self.score * self.d and size is not 1 and level == 3:
		print("Congratulations!! You won the game")
		print("Your score is : " + str(countscore + self.score ))
		print("Thanks for playing!! Created by NITIN AGARWAL")
      elif self.count != self.score * self.d:
		print("You lost the game")
		print("Your score is : " + str(countscore))
		print("Thanks for playing!! Created by NITIN AGARWAL")
		self.brk = 1
      elif size == 1 or key == 27:
		self.brk = 1
		print("You lost the game")
		print("Your score is : " + str(countscore))
		print("Thanks for playing!! Created by NITIN AGARWAL")
         
level = 1
size = 0
countscore = 0

while level is not 3:    
    size = 0    
    myrobot = Robot()
    myrobot.brk = 0
    
    win = newwin(myrobot.size_field, myrobot.size_field, 0, 0)
    win.keypad(1)
    win.nodelay(1)
    win.border('!','!','=','=','+','+','+','+')

    robot  =  ['  ^  ',' @_@ ','/|O|\\',' ___ ',' d b ']
    key = KEY_RIGHT
    if level >= 2:
      hor_mines = [[4,2],[4,3],[4,4],[19,13],[19,12],[19,11],[12,13],[12,14],[12,15],[12,16],[6,21],[6,22],[6,23],[24,25],[24,24],[24,23]]
      for i in range(len(hor_mines)):
        win.addch(hor_mines[i][0], hor_mines[i][1], '$')
      
      ver_mines = [[5,4],[6,4],[7,4],[20,11],[21,11],[22,11],[7,22],[8,22],[9,22],[25,25],[26,25],[27,25]]
      for i in range(len(ver_mines)):
        win.addch(ver_mines[i][0],ver_mines[i][1], '$')
    bomb_pos = [[12,11]]
    bomb = "B"
    win.addstr(bomb_pos[0][0], bomb_pos[0][1], bomb)

    code_pos = [[(myrobot.size_field)/2,(myrobot.size_field)/2]]
    decode = "D"
    n = []
    n = [[1+3*level,4+2*level],[14+4*level,5+level],[9+2*level,8+2*level]]

    for i in range(myrobot.d):
        win.addstr(n[i][0], n[i][1],decode)
    for i in range (myrobot.size_robot):    
      win.addstr(code_pos[0][0]+i, code_pos[0][1],robot[i])

    x_pos = code_pos[0][0]
    y_pos = code_pos[0][1]

    while key != 27:
        win.addstr(0, 2,' Level No. : ' +  str(level) + ' Total codes taken: ' + str(myrobot.count) + ' ')
        if x_pos <= 0 or y_pos <= 0 or x_pos + myrobot.size_robot >= myrobot.size_field  or y_pos + myrobot.size_robot >= myrobot.size_field:
            size = size+1
            break

        win.timeout(180 - level * 30)
        getkey = win.getch()  
        key = key if getkey == -1 else getkey
        
        if key == 80 or key == 112:
            win.timeout(-2)
            getkey = win.getch()   
            key = key if getkey == -1 else getkey
           
        if key == KEY_RIGHT :
            myrobot.delete(x_pos,y_pos)
            y_pos = y_pos+1
            myrobot.insert(x_pos,y_pos)
        if key == KEY_LEFT :
            myrobot.delete(x_pos,y_pos)
            y_pos = y_pos-1
            myrobot.insert(x_pos,y_pos)
        if key == KEY_UP:
            myrobot.delete(x_pos,y_pos)
            x_pos = x_pos-1
            myrobot.insert(x_pos,y_pos)
        if key == KEY_DOWN:
            myrobot.delete(x_pos,y_pos)
            x_pos = x_pos+1
            myrobot.insert(x_pos,y_pos)

        flag = 0
        for i in range(myrobot.size_robot):
            for j in range(myrobot.size_robot):
                if bomb_pos[0][0] == x_pos+i and bomb_pos[0][1] == y_pos+j:
                 flag = flag + 1
                 break
            if flag is not 0:
                break
        if flag is not 0:
            break            

        flag = 0
        for i in range(myrobot.size_robot):
            for j in range(myrobot.size_robot):
                for k in range(myrobot.num_codes):
                    if n[k][0] == x_pos+i and n[k][1] == y_pos+j:
                        del(n[k])
                        myrobot.num_codes = myrobot.num_codes - 1
                        myrobot.count = myrobot.count + myrobot.score
                        flag = flag+1
                        break
                if flag is not 0:
                    break     
            if flag is not 0:
                    break
        
        if level >= 2:            
         flag = 0
         for i in range(myrobot.size_robot):
            for j in range(myrobot.size_robot):
                for k in range(len(hor_mines)):
                    if hor_mines[k][0]==x_pos+i and hor_mines[k][1]==y_pos+j:
                      size = size+1
                      flag = flag+1
                      break
                if flag is not 0:
                  break
            if flag is not 0:
              break
         if flag is not 0:
              break


         flag = 0
         for i in range(myrobot.size_robot):
            for j in range(myrobot.size_robot):
                for k in range(len(ver_mines)):
                    if ver_mines[k][0] == x_pos+i and ver_mines[k][1] == y_pos+j:
                                size = size+1
                                flag = flag+1
                                break
                if flag is not 0:
                    break
            if flag is not 0:
               break
         if flag is not 0:
               break
    countscore = countscore + myrobot.count
    level = level + 1   
    if flag != 0 or level == 4 or size == 1 or key == 27:
      myrobot.quit_game(size)
      if myrobot.brk == 1 or key == 27:
        break




