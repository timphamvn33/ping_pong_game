from turtle import Turtle
class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.left(90)
        self.move = 10
        self.new_move=10
        self.penup()
        self.goto(0, -200)
        self.y = self.ycor()
        self.t = 2



    def move_forward(self, range ):
        while self.y < range:

            if self.t % 2 == 0:
                self.pendown()
                self.y += self.new_move
                self.goto(0, self.y)
                self.t += 1

            else:
                self.penup()
                self.y += self.new_move
                self.goto(0, self.y)
                self.t += 1



