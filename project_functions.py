def table(width, height, table_color, turta):
   # Rectangle
    turta.pensize("2")
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.fd(width)
    turta.left(90)
    turta.fd(height*0.3)
    turta.left(90)
    turta.fd(width)
    turta.left(90)
    turta.fd(height*0.3)
    turta.end_fill()

    # Left Long Leg
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.fd(height)
    turta.left(90)
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(height)
    turta.end_fill()


    # Left Short Leg
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.right(90)
    turta.fd(width*0.1)
    turta.right(90)
    turta.fd(height*0.8)
    turta.left(90)
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(height*0.8)
    turta.end_fill()


    # Right Short Leg
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.right(90)
    turta.fd(width*0.4)
    turta.right(90)
    turta.fd(height*0.8)
    turta.left(90)
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(height*0.8)
    turta.end_fill()

    # Right Long Leg
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.right(90)
    turta.fd(width*0.1)
    turta.right(90)
    turta.fd(height)
    turta.left(90)
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(height)
    turta.end_fill()


    turta.up()
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(width*0.2)
    turta.right(90)
    turta.down()


    # Cake maker
def cake_maker(width, layer1_color, layer2_color, layer3_color, turta):
    # First Layer
    turta.begin_fill()
    turta.fillcolor(layer1_color)
    turta.fd(30)
    turta.left(90)
    turta.fd(width*0.6)
    turta.left(90)
    turta.fd(30)
    turta.end_fill()


    # Plate
    turta.pensize("5")
    turta.pencolor("white")
    turta.left(90)
    turta.fd(width*0.6)
    turta.left(90)
    turta.pensize("2")
    turta.pencolor("black")
    turta.fd(30)


    # Second Layer
    turta.begin_fill()
    turta.fillcolor(layer2_color)
    turta.left(90)
    turta.fd(width*0.1)
    turta.right(90)
    turta.fd(30)
    turta.left(90)
    turta.fd(width*0.4)
    turta.left(90)
    turta.fd(30)
    turta.end_fill()


    turta.bk(30)
    turta.left(90)
    turta.fd(width*0.1)


    # Third Layer
    turta.begin_fill()
    turta.fillcolor(layer3_color)
    turta.left(90)
    turta.fd(30)
    turta.right(90)
    turta.fd(width*0.2)
    turta.right(90)
    turta.fd(30)
    turta.end_fill()


    # Decoration
def cake_decorations(width, turta):
    turta.bk(30)
    turta.right(90)
    turta.fd(width*0.05)
    turta.left(180)
    turta.begin_fill()
    turta.fillcolor("light blue")
    turta.circle(width*0.05)
    turta.end_fill()
    turta.bk(width*0.15)


    # Candle
    turta.begin_fill()
    turta.fillcolor("red")
    turta.fd(width*0.025)
    turta.left(90)
    turta.fd(35)
    turta.right(90)
    turta.fd(width*0.025)
    turta.right(90)
    turta.fd(35)
    turta.end_fill()


    # Frosting
    turta.begin_fill()
    turta.fillcolor("white")
    turta.right(90)
    turta.fd(width*0.05)
    turta.left(90)
    turta.circle(10,180)
    turta.left(180)
    turta.circle(10,180)
    turta.end_fill()

