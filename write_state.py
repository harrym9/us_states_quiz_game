from turtle import Turtle


class WriteState(Turtle):
    def __init__(self, text, x, y):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.make_text(self.text, self.x, self.y)

    def make_text(self, text, x, y):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(arg=text, align="center", font=("Arial", 8, "bold"))
