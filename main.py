from turtle import Turtle, Screen
from shapes import Shapes

screen = Screen() # Needs to be up here if I want to use rgb a bit annoying.
screen.colormode(255) # Needs to be up here if I want to use rgb a bit annoying.
tim = Turtle()
diff_shapes = Shapes()


tim.speed("slowest")
tim.shape("turtle")
tim.color(( diff_shapes.get_colors() ))

# TODO: 1. Challenge draw a square.
# for _ in range(4):
#   tim.forward(100)
#   tim.left(90)

# TODO: 2. Draw dashed lines.
# tim.pensize(5)
# for _ in range(15):
#   tim.fd(10)
#   tim.penup()
#   tim.fd(10)
#   tim.pendown()

# TODO: 3. Draw Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, and Decagon
#          Sides   3         4       5         6        7         8        9          10
while diff_shapes.track_side_turns():
  tim.fd(100)
  tim.right(diff_shapes.cal_angle())

  if diff_shapes.track_turns == diff_shapes.sides:
    tim.color(diff_shapes.change_color())

# screen = Screen()
# screen.colormode(255)
screen.exitonclick()