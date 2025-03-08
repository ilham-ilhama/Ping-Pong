import turtle
import time

class PingPongGame:
    def __init__(self):
        # Setup window
        self.window = turtle.Screen()
        self.window.title("Ping Pong Game By Fatima ikram Kaoutar Ilham")
        self.window.setup(width=800, height=600)
        #eviter le retard
        self.window.tracer(0)
        self.window.bgcolor(0, 1, 0)
        
        # Game variables
        self.ball_dx, self.ball_dy = 1, 1
        self.ball_speed = .5
        self.players_speed = 50
        self.p1_score, self.p2_score = 0, 0

        # Setup game objects
        self.setup_objects()
        
        # Keyboard bindings
        #
        self.window.listen()#or tell the window to expect user inputs
        self.window.onkeypress(self.p1_move_up, "a")
        self.window.onkeypress(self.p1_move_down, "z")
        self.window.onkeypress(self.p2_move_up, "Up")
        self.window.onkeypress(self.p2_move_down, "Down")
# Run the countdown and start the game loop
        self.countdown()
        self.game_loop()

    def setup_objects(self):
        # Ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("yellow")
        self.ball.shapesize(stretch_wid=2.0, stretch_len=2.0, outline=3.0)
        self.ball.penup()
        self.ball.goto(0, 0)
        
        # Center line
        self.center_line = turtle.Turtle()
        self.center_line.speed(0)
        self.center_line.shape("square")
        self.center_line.color("white")
        self.center_line.shapesize(stretch_len=.1, stretch_wid=25)
        self.center_line.penup()
        self.center_line.goto(0, 0)
        
        # Player 1
        self.player1 = turtle.Turtle()
        self.player1.speed(0)
        self.center_line.shape("square")
        self.center_line.color("white")
        self.center_line.shapesize(stretch_len=.1, stretch_wid=25)
        self.center_line.penup()
        self.center_line.goto(0, 0)
        
        # Player 1
        self.player1 = turtle.Turtle()
        self.player1.speed(0)
        self.player1.shape("square")
        self.player1.shapesize(stretch_len=1, stretch_wid=5)
        self.player1.color("RED")
        self.player1.penup()
        self.player1.goto(-350, 0)
        
        # Player 2
        self.player2 = turtle.Turtle()
        self.player2.speed(0)
        self.player2.shape("square")
        self.player2.shapesize(stretch_len=1, stretch_wid=5)
        self.player2.color("BLUE")
        self.player2.penup()
        self.player2.goto(350, 0)
 
        # Score
        self.score_display = turtle.Turtle()
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.goto(-2, 260)
        self.score_display.write("player1:0 VS player2:0", align="center", font=("Courier", 14, "normal"))
        self.score_display.hideturtle()

    def p1_move_up(self):
        self.player1.sety(self.player1.ycor() + self.players_speed)

    def p1_move_down(self):
        self.player1.sety(self.player1.ycor() - self.players_speed)

    def p2_move_up(self):
        self.player2.sety(self.player2.ycor() + self.players_speed)

    def p2_move_down(self):
        self.player2.sety(self.player2.ycor() - self.players_speed)
    def countdown(self):
        countdown_turtle = turtle.Turtle()
        countdown_turtle.color("black")
        countdown_turtle.penup()
        countdown_turtle.hideturtle()
        countdown_turtle.goto(0, 0)
        
        for i in range(3, 0, -1):
            countdown_turtle.clear()
            countdown_turtle.write(str(i), align="center", font=("Courier", 48, "normal"))
            self.window.update()
            time.sleep(1)
        
        countdown_turtle.clear()
        countdown_turtle.write("Go!", align="center", font=("Courier", 48, "normal"))
        self.window.update()
        time.sleep(1)
        countdown_turtle.clear()

    def update_ball_position(self):
    #ball_dx=1              .7
        self.ball.setx(self.ball.xcor() + (self.ball_dx * self.ball_speed))
        self.ball.sety(self.ball.ycor() + (self.ball_dy * self.ball_speed))
    #l'axe Y
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball_dy *= -1
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball_dy *= -1
        #l'axe Y
        if  -350 < self.ball.xcor() < -340  and (self.player1.ycor()+60) > self.ball.ycor()>(self.player1.ycor()-60):
            self.ball.setx(-340)
            self.ball_dx *= -1
        if  350 > self.ball.xcor() > 340 and (self.player2.ycor()+60 ) > self.ball.ycor() > (self.player2.ycor()-60):
            self.ball.setx(340)
            self.ball_dx *= -1

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball_dx *= -1
            self.p1_score += 1
            self.update_score()

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball_dx *= -1
            self.p2_score += 1
            self.update_score()

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"player1:{self.p1_score} VS player2:{self.p2_score}", align="center", font=("Courier", 14, "normal"))

    def game_loop(self):
        while True:
            self.window.update()
            self.update_ball_position()

# Create an instance of the game to run it
PingPongGame()