import turtle

def draw_petal():
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)

def draw_rose():
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(6):  # Số cánh hoa
        draw_petal()
        turtle.left(60)
    turtle.end_fill()

def draw_stem():
    turtle.right(90)
    turtle.color("green")
    turtle.pensize(5)
    turtle.forward(200)

def main():
    turtle.speed(2)
    turtle.bgcolor("white")

    draw_rose()
    draw_stem()

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
