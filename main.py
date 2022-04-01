import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(my_turtle=None):
  '''this function draws a sine curve
  args: my_turtle (turtle object)
  return: None'''
  my_turtle.up()
  my_turtle.goto(math.radians(-360),math.sin(math.radians(-360)))
  my_turtle.down()
  for angle in range(-360,361):
    x = math.radians(angle)
    y = math.sin(math.radians(angle))
    my_turtle.goto(x, y)

def setupWindow(my_window=None):
  '''This function sets the world coordinates and background color for the    window 
  args: my_window(screen)
  return: None'''
  my_window.setworldcoordinates(-math.radians(360),-1,math.radians(360),1)
  my_window.bgcolor("hotPink")

def setupAxis(my_turtle=None):
  '''This function draws an axis
  args: my_turtle (turtle object)
  return: None'''
  my_turtle.speed(10)
  my_turtle.down()
  my_turtle.forward(math.radians(360))
  my_turtle.backward(2*math.radians(360))
  my_turtle.forward(math.radians(360))
  my_turtle.right(90)
  my_turtle.forward(1)
  my_turtle.backward(2)

def drawCosineCurve(my_turtle=None):
  '''this function draws a cosine curve
  args: my_turtle (turtle object)
  return: None'''
  my_turtle.up()
  my_turtle.goto(math.radians(-360),math.cos(math.radians(-360)))
  my_turtle.down()
  for angle in range(-360,361):
    x = math.radians(angle)
    y = math.cos(math.radians(angle))
    my_turtle.goto(x, y)

def drawTangentCurve(my_turtle=None):
  '''this function draws a tangent curve
  args: my_turtle (turtle object)
  return: None'''
  my_turtle.up()
  my_turtle.goto(math.radians(-360),math.tan(math.radians(-360)))
  my_turtle.down()
  for angle in range(-360,361):
    x = math.radians(angle)
    y = math.tan(math.radians(angle))
    my_turtle.goto(x, y)  






##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
