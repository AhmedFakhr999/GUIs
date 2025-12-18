# Python program to open the
# camera in Tkinter
# Import the libraries,
# tkinter, cv2, Image and ImageTk
#
# from tkinter import *
# import cv2
# from PIL import Image, ImageTk
#
# # Define a video capture object
# vid = cv2.VideoCapture(0)
#
# # Declare the width and height in variables
# width, height = 800, 600
#
# # Set the width and height
# vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#
# # Create a GUI app
# app = Tk()
#
# # Bind the app with Escape keyboard to
# # quit app whenever pressed
# app.bind('<Escape>', lambda e: app.quit())
#
# # Create a label and display it on app
# label_widget = Label(app)
# label_widget.pack()
#
# # Create a function to open camera and
# # display it in the label_widget on app
#
#
# def open_camera():
#
# 	# Capture the video frame by frame
# 	_, frame = vid.read()
#
# 	# Convert image from one color space to other
# 	opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#
# 	# Capture the latest frame and transform to image
# 	captured_image = Image.fromarray(opencv_image)
#
# 	# Convert captured image to photoimage
# 	photo_image = ImageTk.PhotoImage(image=captured_image)
#
# 	# Displaying photoimage in the label
# 	label_widget.photo_image = photo_image
#
# 	# Configure image in the label
# 	label_widget.configure(image=photo_image)
#
# 	# Repeat the same process after every 10 seconds
# 	label_widget.after(10, open_camera)
#
#
# # Create a button to open the camera in GUI app
# button1 = Button(app, text="Open Camera", command=open_camera)
# button1.pack()
#
# # Create an infinite loop for displaying app on screen
# app.mainloop()
# import turtle as t
# import random
# tim = t.Turtle()
# t.colormode(255)
# tim.pensize(15)
# tim.speed("fastest")
# colours=['CornflowerBlue', 'red', 'blue', 'yellow', 'cyan', 'black', 'gray']
#def draw_shape(num_sides):
#    angle=360/num_sides
 #   for _ in range(num_sides):
 #       tim.forward(100)
 #       tim.right(angle)
# from pickletools import read_stringnl_noescape
# from turtle import Turtle , Screen
import time
#for shape_side_n in range(3,11):
#    tim.color(random.choice(colours),)
 #   draw_shape(shape_side_n)
# directions=[0,90,180,270]
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
# timm=Turtle()
# screen =Screen()
# #---------------
# screen.setup(500,400)
# screen.exitonclick()
# screen.textinput("make your bet (haram by the way","enter a color")
#
# colors=['red','blue','yellow']
#
# for turtles in range(0,6):
#     timm=Turtle(shape='Turtle')
#     timm.color(colors[turtles])
#     timm.penup()
#     timm.goto(-100,200)
# from turtle import Turtle, Screen
#
# tim=Turtle('square')
# screen=Screen()
# screen.setup(width=500, height=500)
# screen.bgcolor("black")
# screen.title("Snaky waky")
#
# starting_position=[(0,0),(-20,0),(-40,0)]
#
#
#
# tim.color('white')
# tim.goto(-20,0)
#
#
# screen.exitonclick()
from turtle import Turtle,Screen
from paddal import Paddal
from ball import Ball
from scoreboard import Score
scr=Screen()

scr.bgcolor('black')
scr.setup(800,700)
scr.title('Pong')
scr.tracer(0)
scr.update()


r_paddle=Paddal((350,0))
l_paddle=Paddal((-350,0))
ball=Ball()
scory=Score()







scr.listen()

scr.onkey(r_paddle.go_down,"Down")

scr.onkey(r_paddle.go_up,"Up")

scr.onkey(l_paddle.go_down,"w")
scr.onkey(l_paddle.go_up,"s")
scr.onkey(scr.exitonclick,"q")



game_is_no = True
while game_is_no:
    time.sleep(ball.speedy)
    scr.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce()


    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.bounce_x()



    if ball.xcor()>340:
        ball.reset()
        scory.l_points()

    if ball.xcor()<-340:
        ball.reset()
        scory.r_points()





