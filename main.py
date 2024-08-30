# import colorgram
import turtle as t
import random
from turtle import Turtle

pen: Turtle = t.Turtle()
t.colormode(255)
#
# rgb_list = []
# extracted_colors = colorgram.extract('img.jpg', 6)
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list = (r,g,b)
#     rgb_list.append(color_list)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (174, 94, 97), (176, 192, 209)]
pen.speed('fastest')
pen.penup()
pen.hideturtle()
pen.setheading(225)
pen.forward(270)
pen.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    pen.dot(20, random.choice(color_list))
    pen.forward(50)

    if dot_count % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)


screen = t.Screen()
screen.exitonclick()