#სახლი დასახატად.

from turtle import*

speed(120)

color("orange")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)
 
forward(200)
left(90)

forward(200)
left(90)

end_fill()

forward(130)
left(90)

color("brown")

begin_fill()
forward(100)
left(90)

forward(60)
left(90)

forward(100)
left(90)

forward(60)
end_fill()

penup()

goto(70,120)

pendown()

color("cyan")

begin_fill()
left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)
end_fill()

penup()
goto(130,120)
pendown()

color("cyan")
begin_fill()
forward(60)

left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)
end_fill()

penup()
goto(200,200)
pendown()

right(140)

color("green")

begin_fill()
forward(155)
left(100)

forward(155)
end_fill()

exitonclick()