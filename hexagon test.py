import turtle

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)


turtle.speed(0)
turtle.bgcolor("black")
turtle.color("white")


num_polygons = 360
polygon_sides= 10
side_length = 20


for i in range(num_polygons):
    draw_polygon(polygon_sides, side_length)
    turtle.right(360 / num_polygons)


turtle.done()
