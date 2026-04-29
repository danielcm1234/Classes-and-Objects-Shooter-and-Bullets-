from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.playercolor = color
        self.colors = ["dead", "red", "yellow", color]
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.fire_key = fire_key
        self.health = 3
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())

    def fire(self):
        self.bullets.append(Bullet(self))

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.pu()
        self.speed(0)
        self.player = player
        self.color(player.playercolor)
        self.setheading(player.heading())
        self.goto(player.xcor(), player.ycor())
        self.st()
        self.move()

    def move(self):
        self.forward(8)
        if self.xcor() > 230 or self.xcor() < -230:
            self.player.bullets.remove(self)
            self.ht()
        if self.ycor() > 230 or self.ycor() < -230:
            self.player.bullets.remove(self)
            self.ht()



screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()


playing_area()

p1 = Player(-100, 0, "red",screen, "d", "a", "w")
p2 = Player(100,0,"blue",screen, "Right","Left", "Up")

while p1.alive and p2.alive:
    p1.move()
    p2.move()
    for bullet in p1.bullets:
        bullet.move()
        if p2.distance(bullet) < 20:
            p2.health -= 1
            if p2.health >0:
                p2.color(p2.colors[p2.health])
            else:
                p2.hideturtle()
                p2.alive = False
    for bullet in p2.bullets:
        bullet.move()
        if p1.distance(bullet) < 20:
            p1.health -= 1
            if p1.health >0:
                p1.color(p1.colors[p1.health])
            else:
                p1.hideturtle()
                p1.alive = False

screen.exitonclick()