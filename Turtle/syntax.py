import turtle

screen=turtle.Screen()
screen.setup(600,600) #set screen size 600x600
screen.bgcolor('blue') #set screen background to blue

turtle.pensize(10) #set pen size 10 pixels
turtle.speed(10) #0~10,10 is tha fastest,0 means no animation
turtle.shape('turtle') #set pen shape

turtle.pendown() #start drawing
turtle.penup() #stop drawing

turtle.color('green') #set line color to green
turtle.color('yellow', 'red') #set yellow frame and red background

turtle.goto(-200,-200) #move to (-200,-200)
turtle.left(90) #turn left 90 degrees
turtle.right(90) #turn right 90 degrees
turtle.setheading(90) #change direction,west:0;north:90;east:180;south:270
turtle.forward(200) #drawing 

turtle.begin_fill() #start flag of filling background
turtle.circle(100) # draw a circle with a radius of 100
turtle.end_fill() #stop flag of filling background

screen.exitonclick() #close canvas until click it
