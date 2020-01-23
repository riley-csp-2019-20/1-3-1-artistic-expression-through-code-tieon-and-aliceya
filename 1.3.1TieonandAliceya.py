
#import required libraries
import turtle as trtl
import random 
#create turtle
head = trtl.Turtle()
body = trtl.Turtle()
# bubbles = trtl.Turtle()
segments = []

# game configuration 
score = 0

timer = 15
counter_interval = 1000
timer_up = False

#movement functions
def tiger_up():
    head.setheading(90)
    head.forward(10)
    move()
+
def tiger_down():
    head.setheading(270)
    head.forward(10)
    move()

def tiger_left():
    head.setheading(180)
    head.forward(10)
    move()

def tiger_right():
    head.setheading(0)
    head.forward(10)
    move()

def tiger_clear():
    head.clear()
    
def move():
    #up
    if head.heading() == 90:
        body.goto(head.xcor(), head.ycor() - 20)
    #down
    if head.heading() == 270:
        body.goto(head.xcor(), head.ycor() + 20)
    #right
    if head.heading() == 0:
        body.goto(head.xcor(), head.ycor() - 20)
    #left
    if head.heading() == 180:
        body.got(head.xcor(), head.ycor()  + 20




#Making the turtle color and shape and size
    if head.filling()
       head.pensize()
        else:
            head.pensize()
            head.penup()
            head.pendown()
            head.shapesize()
            head.shape("circle")





#score 
# def update_score():
#     global score
#     score += 1
#     print(score)
#     score_writer.clear()
#     score_writer.write(score, font = font_setup) 


# def countdown():
#     global timer, timer_up
#     counter.clear()
#     if timer <= 0:
#         counter.write("Game over!", font = font_setup)
#         timer_up = True
#         manage_leaderboard()
        
      
#     else:
#         counter.write("Timer: " + str(timer), font = font_setup)
#         timer =  -1
#         counter.getscreen().ontimer(countdown, counter_interval)

#create screen
wn = trtl.Screen()
wn.bgcolor("purple")

#bind to keypresses
#Making the turtle move with the arrow keys
wn.onkeypress(tiger_up, "Up")
wn.onkeypress(tiger_down, "Down")
wn.onkeypress(tiger_left, "Left")
wn.onkeypress(tiger_right, "Right")
wn.onkeypress(tiger_clear, "space")






#listen
wn.listen()

#mainloop
wn.mainloop()
