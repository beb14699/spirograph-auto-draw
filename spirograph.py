import turtle

turtle.bgcolor('dark green')
turtle.pensize(2.5)
turtle.speed(0)

for i in range(6):
	for colors in ["red", "magenta", "blue", "cyan", "lawn green", "yellow", "white"]:
		turtle.color(colors)
		turtle.circle(100)
		turtle.left(10)

turtle.done()