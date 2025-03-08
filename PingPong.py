import turtle,time,pygame
pygame.init()

class PingPongGame:
    
    def __init__(self):

        # Setup player names
        self.player1_name = ""
        self.player2_name = ""

         
        # Setup window
        self.window = turtle.Screen()
        self.window.title("Ping Pong Game By Fatima ikram Kawtar Ilham")
        self.window.setup(width=800, height=600)
        #eviter le retard
        self.window.tracer(0)
        self.window.bgcolor("black")
        
        # Game variables
        self.ball_dx, self.ball_dy = 1, 1
        self.ball_speed = 1 
        self.players_speed = 50
        self.p1_score, self.p2_score = 0, 0
        self.is_paused = False  #pause State

       #sound effect
        self.sound_hit = pygame.mixer.Sound("ball_bounce.mp3")
        self.sound_countdown = pygame.mixer.Sound("countdown.mp3")
        self.sound_winner = pygame.mixer.Sound("the_winner_is_sound.mp3")

       #players names
        self.player1_name = turtle.textinput("Player 1", "Enter name for Player 1:")
        self.player2_name = turtle.textinput("Player 2", "Enter name for Player 2:")
        

        # Setup game objects
        self.setup_objects()

       
        
       
        
        # Keyboard bindings
        self.window.listen()# tell the window to expect user inputs
        #players movement
        self.window.onkeypress(self.p1_move_up, "a")
        self.window.onkeypress(self.p1_move_down, "z")
        self.window.onkeypress(self.p2_move_up, "Up")
        self.window.onkeypress(self.p2_move_down, "Down")
        
        self.window.onkeypress(self.pause,"space")



        # Run the countdown and start the game loop
        self.countdown()
        self.game_loop()

    def setup_objects(self):
        # Ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("lightgreen")
        self.ball.shapesize(stretch_wid=1.0, stretch_len=1.0, outline=1.0)
        self.ball.penup()
        self.ball.goto(0, 0)
        
        # Center line
        self.center_line = turtle.Turtle()
        
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
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.goto(0, 260)
        self.score_display.write(f"{self.player1_name}:0 VS {self.player2_name}:0", align="center", font=("Courier", 14, "normal"))
        self.score_display.hideturtle()

      
        # Timer
        self.timer_display = turtle.Turtle()
        self.timer_display.color("white")
        self.timer_display.penup()
        self.timer_display.hideturtle()
        self.timer_display.goto(-300, 260)
        self.time_left = 20
       
        
        #pause text
        self.pause_text = turtle.Turtle()
        self.pause_text.color("lightBlue")
        self.pause_text.penup()
        self.pause_text.hideturtle()
        self.pause_text.goto(0,0)
        

         # Winner text
        self.winner_text = turtle.Turtle()
        self.winner_text.color("white")
        self.winner_text.penup()
        self.winner_text.hideturtle()
        self.winner_text.goto(0, 0)

  

   
    
    
    def p1_move_up(self):
        if not self.is_paused:
            self.player1.sety(self.player1.ycor() + self.players_speed)

    def p1_move_down(self):
        if not self.is_paused:
            self.player1.sety(self.player1.ycor() - self.players_speed)

    def p2_move_up(self):
        if not self.is_paused:
            self.player2.sety(self.player2.ycor() + self.players_speed)

    def p2_move_down(self):
        if not self.is_paused:
            self.player2.sety(self.player2.ycor() - self.players_speed)

    

    def countdown(self):
        self.countdown_turtle = turtle.Turtle()
        self.countdown_turtle.color("white")
        self.countdown_turtle.penup()
        self.countdown_turtle.hideturtle()
        self.countdown_turtle.goto(0, 0)

        pygame.mixer.Sound.play(self.sound_countdown)
        for i in range(3, 0, -1):
            self.countdown_turtle.clear()
            self.countdown_turtle.write(str(i), align="center", font=("Courier", 48, "normal"))
            self.window.update()
            time.sleep(1)

        self.countdown_turtle.clear()
        self.countdown_turtle.write("Go!", align="center", font=("Courier", 48, "normal"))
        self.window.update()
       
        time.sleep(1)
        self.countdown_turtle.clear()

        #start timer
        self.update_timer()


    def update_timer(self):
        if not self.is_paused:
            self.timer_display.clear()
            self.timer_display.write(f"Time Left: {self.time_left}", align="center", font=("Courier", 14, "normal"))
            self.time_left -= 1

            if self.time_left >= 0:
                self.window.ontimer(self.update_timer, 1000)
            else:
                self.check_winner()

    def display_winner(self, winner):
        self.winner_text.clear()
        pygame.mixer.Sound.play(self.sound_winner)
        self.winner_text.write(f"And the winner is {winner}", align="center", font=("Courier", 36, "normal"))
       
        self.window.update()
        time.sleep(3)
        self.winner_text.clear()   


    def check_winner(self):
        if self.time_left < 0:
            if self.p1_score > self.p2_score:
                winner = self.player1_name
            elif self.p2_score > self.p1_score:
                winner = self.player2_name

            else :   self.end_game()  
                   

                #   pygame.mixer.Sound.stop(self.sound_winner) 
                #  winner = "it's a tie!!"
                 # Stop the winner sound 

        self.display_winner(winner)
        self.end_game()  



    def end_game(self):

        self.pause_text.goto(0, 0)
        self.pause_text.write("Game Over! 💀", align="center", font=("Courier", 50, "normal"))
        self.window.update()
        time.sleep(3)
        self.window.bye()
          

    
    def pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_text.write("paused" , align="center", font=("courier" , 48, "normal"))
            self.update_timer(None)
           
           
        else:
            self.pause_text.clear() 
            self.update_timer()
 
    def update_ball_position(self):
        if self.is_paused:
            return  True #don't update the ball position if the game is paused
        else: 
            #met a jour la cordonnee x de la balle avec la nouvelle valeur calcule
                                              
            self.ball.setx(self.ball.xcor() + (self.ball_dx * self.ball_speed))
            self.ball.sety(self.ball.ycor() + (self.ball_dy * self.ball_speed))


        #les limites des objets pour le mouvement
        #l'axe Y
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball_dy *= -1
           
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball_dy *= -1
           
        #l'axe X
         #le contact de la balle avec la  raquette  j1
                                                #verifier si la balle se trouve dans la plage vertical de la raquette  
        if  -350 < self.ball.xcor() < -340  and (self.player1.ycor()+60) > self.ball.ycor()>(self.player1.ycor()-60):
            self.ball.setx(-340)
            self.ball_dx *= -1
            pygame.mixer.Sound.play(self.sound_hit)
        if  350 > self.ball.xcor() > 340 and (self.player2.ycor()+60 ) > self.ball.ycor() > (self.player2.ycor()-60):
            self.ball.setx(340)
            self.ball_dx *= -1
            pygame.mixer.Sound.play(self.sound_hit)

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball_dx *= -1
            self.p1_score += 1
            pygame.mixer.Sound.play(self.sound_hit)
            self.update_score()

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball_dx *= -1
            self.p2_score += 1
            pygame.mixer.Sound.play(self.sound_hit)
            self.update_score()

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"{self.player1_name}:{self.p1_score} VS {self.player2_name}:{self.p2_score}", align="center", font=("Courier", 14, "normal"))



    

   

    #def winner_name(self):

   
    def game_loop(self):
        while True:
            self.window.update()
            self.update_ball_position()

# Create an instance of the game to run it
PingPongGame()