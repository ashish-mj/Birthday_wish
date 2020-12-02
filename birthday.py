import turtle

name = input("Enter Name")
age = input("Enter Age")


bg = turtle.Screen()
turtle.title("Happy Birthday "+name)
bg.bgcolor("black")

turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(260)

########################################cake
turtle.penup()
turtle.goto(-120,-120)
turtle.color("yellow")
turtle.begin_fill()
turtle.pendown()
turtle.forward(200)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.goto(-95,-30)
turtle.color("yellow")
turtle.begin_fill()
turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

#######################################################candles
turtle.penup()
turtle.goto(-80,65)
turtle.color("orange")
turtle.width(5)
turtle.left(180)
turtle.pendown()
turtle.forward(25)

turtle.penup()
turtle.goto(50,65)
turtle.color("purple")
turtle.width(5)
turtle.pendown()
turtle.forward(25)

turtle.penup()
turtle.goto(-50,65)
turtle.color("blue")
turtle.width(5)
turtle.pendown()
turtle.forward(30)

turtle.penup()
turtle.goto(10,65)
turtle.color("green")
turtle.width(5)
turtle.pendown()
turtle.forward(30)

turtle.penup()
turtle.goto(-20,65)
turtle.color("white")
turtle.width(5)
turtle.pendown()
turtle.forward(35)


#cherry
turtle.penup()
turtle.goto(-80,15)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill() 

turtle.penup()
turtle.goto(-70,-55)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill()

turtle.penup()
turtle.goto(-90,-95)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill()

turtle.penup()
turtle.goto(-60,45)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill() 

turtle.penup()
turtle.goto(0,0)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill()

turtle.penup()
turtle.goto(30,45)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill()

turtle.penup()
turtle.goto(60,-75)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill()

turtle.penup()
turtle.goto(-20,-25)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill()

turtle.penup()
turtle.goto(60,-35)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill()

turtle.penup()
turtle.goto(0,-75)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(5) 
turtle.end_fill()



###############################design

turtle.penup()
turtle.home()
turtle.forward(200)
turtle.pendown()
turtle.color("hotpink")
turtle.width(2)
turtle.speed(0)


def square(length, angle):
    
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length)
    turtle.right(angle)
   
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length)
    turtle.right(angle)

square(40, 90)

for i in range(36):
      turtle.right(10)
      square(40, 90)

turtle.penup()
turtle.home()
turtle.backward(250)
turtle.pendown()
turtle.color("hotpink")
turtle.width(2)
turtle.speed(0)

square(40, 90)

for i in range(36):
      turtle.right(10)
      square(40, 90)



# Happy Birthday message

turtle.penup()
turtle.goto(-280,170 )
turtle.color("pink")
turtle.pendown()
wish = "Happy Birthday "+name+" !"
turtle.write(wish,font=('Courier', 30, 'italic'))


turtle.penup()
turtle.goto(-80,-250 )
turtle.color("pink")
turtle.pendown()
turtle.write("21",font=('Courier', 100, 'italic'))

turtle.penup()
turtle.goto(-80,95)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(3) 
turtle.end_fill()

turtle.penup()
turtle.goto(50,95)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(3) 
turtle.end_fill()

turtle.penup()
turtle.goto(-50,105)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(3) 
turtle.end_fill()

turtle.penup()
turtle.goto(10,105)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(3) 
turtle.end_fill()

turtle.penup()
turtle.goto(-20,115)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(3) 
turtle.end_fill()

turtle.pendown()
turtle.penup()
turtle.goto(-280,-270 )
turtle.color("black")
turtle.pendown()
turtle.write("",font=('Courier', 30, 'italic'))