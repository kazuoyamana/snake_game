from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 22, "normal")


class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(0, 265)
		self.update()

	def add_score(self):
		self.score += 1
		self.clear()
		self.update()

	def update(self):
		self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

	def gameover(self):
		self.goto(0, 0)
		self.write("GAME OVER", align="center", font=FONT)

