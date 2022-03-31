import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(my_turtle=None, min_x = None, max_x = None):
  '''this function draws a sine curve
  args: my_turtle (turtle object)
  return: None'''
  my_turtle.up()
  my_turtle.goto(math.radians(min_x),math.sin(math.radians(min_x)))
  my_turtle.down()
  for angle in range(min_x,max_x+1):
    x = math.radians(angle)
    y = math.sin(math.radians(angle))
    my_turtle.goto(x, y)
    

def setupWindow(my_window=None, min_x = None, max_x = None):
  '''This function sets the world coordinates and background color for the    window 
  args: my_window(screen)
  return: None'''
  my_window.setworldcoordinates(math.radians(min_x),-1,math.radians(max_x),1)
  my_window.bgcolor("skyBlue")

def setupAxis(my_turtle=None, min_x = None, max_x = None):
  '''This function draws an axis
  args: my_turtle (turtle object)
  return: None'''
  my_turtle.speed(10)
  my_turtle.up()
  my_turtle.goto(math.radians(max_x),0)
  my_turtle.down()
  my_turtle.goto(math.radians(min_x),0)
  my_turtle.up()
  my_turtle.goto(0,1)
  my_turtle.down()
  my_turtle.goto(0,-1)
  my_turtle.up()

def drawCosineCurve(my_turtle=None, min_x = None, max_x = None):
  '''this function draws a cosine curve
  args: my_turtle (turtle object)
  return: None'''
  my_turtle.up()
  my_turtle.goto(math.radians(min_x),math.cos(math.radians(min_x)))
  my_turtle.down()
  for angle in range(min_x,max_x+1):
    x = math.radians(angle)
    y = math.cos(math.radians(angle))
    my_turtle.goto(x, y)
    
      

def drawTangentCurve(my_turtle=None, min_x = None, max_x = None):
  '''this function draws a tangent curve
  args: my_turtle (turtle object)
  return: None'''
  my_turtle.up()
  my_turtle.goto(math.radians(min_x),math.tan(math.radians(min_x)))
  my_turtle.down()
  for angle in range(min_x,max_x+1):
    x = math.radians(angle)
    y = math.tan(math.radians(angle))
    my_turtle.goto(x, y) 

def chartOfSineValues(min_x=None, max_x=None):
  """"""
  chart = f"Sine values \n"
  for i in range(min_x,max_x+1):
    chart += f"X-value = {i} Y-value = {math.sin(math.radians(i))} \n"
  return chart

def areaUnderTheSineCurve(my_turtle=None, min_x = None, max_x = None):
  ''''''
  riemannSum = 0
  my_turtle.color("red","blue")
  my_turtle.up()
  my_turtle.goto(math.radians(min_x),0)
  my_turtle.down()
  my_turtle.begin_fill()
  my_turtle.goto(math.radians(min_x),math.sin(math.radians(min_x)))
  my_turtle.down()
  
  for angle in range(min_x,max_x+1):
    x = math.radians(angle)
    y = math.sin(math.radians(angle))
    if y <0:
      riemannSum = riemannSum - y*math.radians(1)
    else:
      riemannSum = riemannSum + y*math.radians(1)
    my_turtle.goto(x, y)
  my_turtle.goto(math.radians(max_x),0)
  my_turtle.end_fill()
  my_turtle.up()
  return riemannSum
    
  
  





##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    min_x = int(input("What is the minimum x value of the function in degrees?"))
    max_x = int(input("What is the maximum x value of the function in degrees?"))
    while min_x > max_x:
      print("Your min is greater than your max.")
      min_x = int(input("What is the minimum x value of the function in degrees?"))
      max_x = int(input("What is the maximum x value of the function in degrees?"))
    drawSineCurve(dart,min_x, max_x)

    #Part B
    setupWindow(wn, min_x, max_x)
    setupAxis(dart, min_x, max_x)
    dart.speed(0)
    drawSineCurve(dart, min_x, max_x)
    drawCosineCurve(dart, min_x, max_x)
    drawTangentCurve(dart, min_x, max_x)
    print(chartOfSineValues(min_x, max_x))
    dart.clear()
    setupWindow(wn, min_x, max_x)
    setupAxis(dart, min_x, max_x)
    dart.speed(0)
    approximatedArea = areaUnderTheSineCurve(dart, min_x, max_x)
    print(f"The area between the Sine curve and the x-axis from {min_x} degrees to {max_x} degrees is approximatly {approximatedArea}")
    wn.exitonclick()
main()
