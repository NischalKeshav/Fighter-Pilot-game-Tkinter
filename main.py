from tkinter import *
import random
#window set up 
window =  Tk()
window.title("Fighter Pilot Game")
width = 600 #window width
height = 600 #window height
window.minsize(width,height)



Canvas =Canvas(width=width,height=height,bg ="black")
Canvas.pack()
listOfObjects = []
class Bomber:
  def create_bomber(self,x=10,y=10,width=20,height=20):
    Canvas.create_rectangle(x,y,width+x,y+height,fill="white")
  def __init__(self,x,y,width,height):  
    self.create_bomber(x,y,width,height)
    self.x = x
    self.y = y
    self.WIDTH = width
    self.HEIGHT = height
    listOfAngles = [1,2,3,-1,-2,-3]
    self.xMove = random.choice(listOfAngles)
    self.yMove =random.choice(listOfAngles)/self.xMove
  def move(self,Canvas= Canvas):
    self.x+=10
    self.y+=10
    Canvas.move(self,10,10)
    Canvas.update()
    Canvas.update_idletasks()

    
    
Bomber1 = Bomber(20,20,80,50)

def run():
  Bomber1.move()
  Canvas.update()
  Canvas.update_idletasks()
  window.after(1,run)



window.after(10,run)
window.mainloop()
