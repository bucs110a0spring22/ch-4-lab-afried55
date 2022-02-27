import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(my_turtle):
  my_turtle.up()
  my_turtle.goto(math.radians(-360),math.sin(math.radians(-360)))
  my_turtle.down()
  for angle in range(-360,361):
    x = math.radians(angle)
    y = math.sin(math.radians(angle))
    my_turtle.goto(x, y)

def setupWindow(my_window):
  turtle.setworldcoordinates(-math.radians(360),-1,math.radians(360),1)
  my_window.bgcolor("hotPink")

def setupAxis(turtle_object):
  turtle_object.speed(10)
  turtle_object.down()
  turtle_object.forward(math.radians(360))
  turtle_object.backward(2*math.radians(360))
  turtle_object.forward(math.radians(360))
  turtle_object.right(90)
  turtle_object.forward(1)
  turtle_object.backward(2)

def drawCosineCurve(my_turtle):
  my_turtle.up()
  my_turtle.goto(math.radians(-360),math.cos(math.radians(-360)))
  my_turtle.down()
  for angle in range(-360,361):
    x = math.radians(angle)
    y = math.cos(math.radians(angle))
    my_turtle.goto(x, y)

def drawTangentCurve(my_turtle):
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
