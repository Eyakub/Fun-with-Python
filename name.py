import turtle


def nm():
    window = turtle.Screen()
    window.bgcolor("black")

    # --------E-------
    e = turtle.Turtle()
    e.shape("arrow")
    e.color("white")
    e.speed(2)

    e.backward(80)
    e.right(90)
    e.forward(150)
    e.left(90)
    e.forward(80)
    e.backward(80)
    e.left(90)
    e.forward(75)
    e.right(90)
    e.forward(70)

    # ------ Y ------
    y = turtle.Turtle()
    y.setpos(30, 0)
    y.shape("arrow")
    y.color("blue")
    y.speed(2)

    y.right(60)
    y.forward(70)
    y.right(30)
    y.forward(88)
    y.backward(88)
    y.right(180)
    y.right(30)
    y.forward(65)

    # ------- A -------
    a = turtle.Turtle()
    a.setpos(140, 0)
    a.shape("arrow")
    a.color("white")
    a.speed(2)

    a.right(110)
    a.forward(160)
    a.backward(160)
    a.left(40)
    a.forward(160)
    a.backward(40)
    a.left(-110)
    a.forward(80)

    # -------- K ---------
    a = turtle.Turtle()
    a.setpos(210, 0)
    a.shape("arrow")
    a.color("white")
    a.speed(2)

    a.right(90)
    a.forward(150)
    a.backward(75)
    a.left(135)
    a.forward(90)
    a.backward(90)
    a.right(90)
    a.forward(90)

    # -------- U -------
    u = turtle.Turtle()
    u.setpos(290, 0)
    u.shape("arrow")
    u.color("white")
    u.speed(2)

    u.right(90)
    u.forward(150)
    u.left(90)
    u.forward(60)
    u.left(90)
    u.forward(150)

    # --------- B --------
    b = turtle.Turtle()
    b.setpos(360, 0)
    b.shape("arrow")
    b.color("blue")
    b.speed(2)

    b.right(90)
    b.forward(150)
    b.left(90)
    b.forward(50)
    b.left(90)
    b.forward(150)
    b.left(90)
    b.forward(50)
    b.left(90)
    b.forward(75)
    b.left(90)
    b.forward(50)


    window.exitonclick()

nm()