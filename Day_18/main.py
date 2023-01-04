import turtle as tortule_module
import random
import colorgram

tortule_module.colormode(255)

color_list = [(239, 246, 244), (248, 242, 246), (2, 13, 31), (52, 25, 17), (219, 127, 106), (10, 105, 159), (241, 213, 69), (149, 83, 39), (214, 87, 64), (164, 162, 32), (157, 7, 24), (156, 63, 102), (11, 63, 32), (97, 6, 19),
              (206, 74, 104), (11, 96, 57), (172, 135, 162), (1, 63, 145), (8, 173, 216), (156, 34, 24), (5, 212, 207), (8, 139, 86), (146, 227, 216), (122, 193, 148), (101, 219, 229), (221, 178, 216), (253, 196, 0), (80, 135, 179)]


# colors = colorgram.extract('Day_18\image.jpg', 30)
# for color in colors:
# r = color.rgb.r
# g = color.rgb.g
# b = color.rgb.b
# rgb_colors.append((r, g, b))
#
# print(rgb_colors)

turtle = tortule_module.Turtle()

turtle.hideturtle()
turtle.penup()
turtle.speed("fastest")

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

for _ in range(10):
    for _ in range(10):
        turtle.dot(50, random.choice(color_list))
        turtle.forward(50)

    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)


screen = tortule_module.Screen()
screen.exitonclick()
