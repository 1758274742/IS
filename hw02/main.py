import turtle

def move(x, y):
      turtle.up()
      turtle.goto(x, y)
      turtle.down()

def ls(x,y,z):
      move(x, y)
      turtle.setheading(z)
      turtle.begin_fill()
      for i in range(5):
            turtle.forward(46.264)
            turtle.right(144)
      turtle.end_fill()


turtle.setup(width=0.9,height=0.9)
turtle.color('red','red')
turtle.speed(5)

move(-330,220)
turtle.begin_fill()
turtle.forward(660)
turtle.right(90)
turtle.forward(440)
turtle.right(90)
turtle.forward(660)
turtle.right(90)
turtle.forward(440)
turtle.right(90)
turtle.end_fill()

turtle.color('yellow','yellow')
move(-220,176)
turtle.right(72)
turtle.begin_fill()
for i in range(5):
         turtle.forward(138.793)
         turtle.right(144)
turtle.end_fill()
turtle.setheading(0)

ls(-128.865,164.681,53)

ls(-87.779,128.888,30)

ls(-87.154,72.044,5)

ls(-127.185,35.74,336)

turtle.hideturtle()
turtle.done()
