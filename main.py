
import turtle as trtl
#move turtle to starting position
trtl.penup()
trtl.setposition(60,0)
trtl.pendown()

# fuction to turn left
def turn_left():
  trtl.left(90)

#begin drawing/filling house
for i in range (2):
  trtl.fillcolor("tan")
  trtl.begin_fill()
  trtl.forward(75)
  turn_left()
  trtl.forward(90)
  turn_left()
  trtl.end_fill()





wn = trtl.Screen()
wn.mainloop()
