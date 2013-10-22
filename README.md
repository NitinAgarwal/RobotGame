RobotGame
=========

CODE ORGANISATION 
   To implement the game of Robot Bomb Defuser using curses library
   I have made only one class named Robot and had defined three methods in it.
   The code organisation of my game is very easy to understand and implement.
   There is one class Robot which is being called by myrobot. In the class 
   of Robot, three are three methods defined for printing, checking and
   ending up the game which are later on being called. In class, some of the 
   fields has been declared such as size of the robot, size of the field,
   number of defuse codes, counting of the score.


CLASS DECOMPOSITION AND METHODS DEFINED IN THE CLASS
   I have made one class named Robot in which i have assigned some of the variables
   such as the size of the field, size of the robot, number of defuse codes to be placed
   in the area of the field,counting the score of the player whcih are being called 
   later on as of in main function.


class Robot:
  def __init__(self):
      self.size_field = 30
      self.size_robot = 5
      self.num_codes = 3
      self.d = 3
      self.brk = 0
      self.count = 0
      self.score = 10

AND THREE METHODS DEFINED BELOW


This is the method named delete declared in the class named Robot.
First the function of win.addstr is to reprint the initial contents with the strin and attributes defined in it
on the screen.this method is being used when the robot moves in the field. 
Over here the robot will move if the position of the current x and y coordinate
of the robot got not get touched by the obstacle in the path ie, mines in level 
else if it acquires the defuse code or the bomb it gets capture by the robot.
it will see over the four side of the robot with its area.
 
def delete(self, x_pos, y_pos):
      for i in range(self.size_robot): 
        win.addstr(x_pos+i, y_pos, " " * self.size_robot)



The function of this method being defined in the class is same as that of above but the only 
difference is that in this i have defined the size of the robot as my attribute.


def insert(self, x_pos, y_pos):
      for i in range(self.size_robot): 
        win.addstr(x_pos+i, y_pos, robot[i])



In this method I have defined the varoius possiblities whne the game ends.
If the robot goes out of the boundary, or if the robot captures all of the defuse codes
being placed in the size of the field and defuses the bomb, or if the robot approaches the bomb 
without being capturing the defuse codes, or when the robot approachs the mines placed in the size of the field,
or when the player presses the escape key, the game ends.


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




DESIGN OF MODULES AND CLASSES AND THEIR ADVANTAGES 

   In my class named Robot, i have declared the values of some variables such as the size of the field,
   number of defuse codes, counting the score, score earned by the robot after collecting the defuse code,
   and ones which are needed in the main function as of the global use.
   And there are three classes defined in the class which are used in the main function of moving the robot
   are being used as globally. these methods are called in main as and when needed.
   The class and the methods defined in it will definitely work for the other game if you want to make with the 
   same logic such as traversing the maze ie, if we want to make enter the robot from one direction and 
   will come out from the other direction while finding the path in the square field with the gates located at
   the two oppositely diagonal corners.
   And say in others games with the same logic the class and the methods defined in this game can be used.
   


PROGRAM CONTROL FLOW
   
Setting of the initial key 
   I have taken the right key as my default key this means that
   the robot will move towards at the starting when the game is 
   started.


Moving the Robot
   There are four keys to make the robot move key_down,key_up, key_right
   and key_left. With the help of these four keys i can make the robot move 
   in the field to collect the defuse codes and then with the help of defuse codes
   defusing the bomb.


Checking if the robot has apprached Defuse code
   If the robot approached the defuse code from either of its side
   say if my robot is of size 5*5 then if any of the four 
   sides of the robot touches the defuse code then the robot
   will capture get defuse code, i will delete that defuse code.


Placing mines in the field
   I have placed horizontal as well as vertical mines in the 
   path of the robot to collect the defuse codes and then 
   defuse the bomb in my level 2 so as to increase its 
   difficulty level.


Checking if the robot approached the Bomb
   There are two possibilites when the robot approaches the bomb, first it might be having all the 
   defuse code and secondly it might not be having all the defuse codes placed in the field.
   If my robot is having all the defuse codes and then appraches the bomb then the bomb will 
   get defused by the robot, ie,i will delete the bomb. Secondly if the robot is not having all the 
   defuse codes that were placed in the field and approaches the bomb, then the game ends
   informing the player that you have lost the game.


Checking if my robot appraches the mines in level2
   if my robot approaches the mines placed in the field , then the game simply ends
   informing the player that you have lost the game

Quiting the game
   If the user presses the Escape key then it will quit the game and will display 
   the score earned bu the player and the game will also end when the robot 
   goes out of the boundary, when all the three levels are over and the bomb is defused.

   
EXTRA FEATURES 
   In this game of Robot Bomb Defuser, i have implemented the three 
   levels in the game increasing the difficulty level and decreasing the 
   time as the level increases.I have made the difficulty level of the game by 
   placing the mines in the area of the field. So whenever the robot gets 
   touched with any of the mines the game ends.So the robot has to collect
   the defuse codes with touching the mines and then after collecting the 
   all the defuse codes lying in the area of the field, it has to defuse the 
   bomb.In the last level i.e., level number 3, the robot has to collect the
   defuse codes without touching any of the mines abd in lesser time.
   So i have made the difficulty level by decreasing the time. 




   
   



   
