from turtle import Turtle

# WriteState Class (Unchanged)
class WriteState(Turtle):
    def __init__(self, text, x, y, color="black"):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.color(color)
        self.make_text(self.text, self.x, self.y)

    def make_text(self, text, x, y):
        self.penup()
        self.goto(x, y)
        self.write(arg=text, align="center", font=("Arial", 8, "bold"))
        self.hideturtle()  # Hide the turtle after writing the text
