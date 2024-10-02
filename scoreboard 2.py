from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,250)
        self.write("Player1")
        self.goto(100,250)
        self.write("Player2")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write("Player 1",self.l_score, align="center", font=("Bahnschrift", 40, "normal"))
        self.goto(100, 200)
        self.write("Player 2",self.r_score, align="center", font=("Bahnschrift", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def display_winner(self, winner):
        self.goto(0, 0)
        self.write("{} wins!".format(winner), align="center", font=("Bahnschrift", 36, "bold"))