#!/usr/bin/python
import pygame

#Define some colors
WHITE = 0xffffff
BLACK = 0x000000

#Define some sizes
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 120
BALL_SIZE = 10




#set w some pygame stuff
pygame.font.init()
font = pygame.font.Font(None,36)

#set w x and y for paddles

def wait():
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return

def reset_ball():
    ballX = 400
    ballY = 300
    ball_x_magnitude = 0.3
    ball_x_direction = 1
    ball_y_magnitude = 0.3
    ball_y_direction = 1



#def displayPaddle(paddle):
#    if paddle.bottom > HEIGHT - 10:
#        paddle.bottom = HEIGHT - 10
#    elif paddle.top < 10:
#        paddle.top = 10
#    pygame.draw.rect(surface, WHITE, paddle)

#main game logic
def main():


    #sets w the 2 paddles
    p1x = 10
    p1y = (HEIGHT / 2) - 40
    p2x = 780
    p2y = (HEIGHT / 2) - 40
    ballX = 400
    ballY = 300
    ball_x_magnitude = 0.3
    ball_x_direction = 1
    ball_y_magnitude = 0.3
    ball_y_direction = 1
    can_move = False
    point_scored = True


    w_pressed = None
    s_pressed = None
    up_pressed = None
    down_pressed = None


    pygame.init()

    surface = pygame.display.set_mode((WIDTH,HEIGHT))

    player1Score = 0
    player2Score = 0

    #Waits for the player to hit space to start
    text = font.render('Press Space To Start', False, (255,255,255))
    surface.blit(text, (0,0))
    pygame.display.update()


    wait()
    pygame.time.wait(1000)
    can_move = True

    player_text = font.render(' ' + str(player1Score) + ' | ' + str(player2Score), False, (255,255,255))
    surface.blit(player_text, (400,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    w_pressed = False
                elif event.key == pygame.K_s:
                    s_pressed = False
                elif event.key == pygame.K_UP:
                    up_pressed = False
                elif event.key == pygame.K_DOWN:
                    down_pressed = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_pressed = True
                elif event.key == pygame.K_s:
                    s_pressed = True
                elif event.key == pygame.K_UP:
                    up_pressed = True
                elif event.key == pygame.K_DOWN:
                    down_pressed = True

        #keys = pygame.key.get_pressed()
        if(can_move == True):
            if w_pressed == True:
                if(p1y > 1):
                    p1y -=1
            if s_pressed == True:
                if(p1y < HEIGHT - PADDLE_HEIGHT - 1):
                    p1y +=1

            if up_pressed == True:
                if(p2y > 1):
                    p2y -=1
            if down_pressed == True:
                if(p2y < HEIGHT - PADDLE_HEIGHT - 1):
                    p2y +=1
            ballX += (ball_x_magnitude * ball_x_direction)
            ballY += (ball_y_magnitude * ball_y_direction)

        #paddle collision


        #ball physics
        if ballY < BALL_SIZE:
            ball_y_direction *= -1
        if ballY > HEIGHT - BALL_SIZE:
            ball_y_direction *= -1

        #point scored
        if ballX > (WIDTH - (BALL_SIZE /2)):
            player1Score += 1
            ballX = 400
            ballY = 300
            ball_x_magnitude = 0.3
            ball_x_direction = 1
            ball_y_magnitude = 0.3
            ball_y_direction = 1
            #wait(3000)
            point_scored = True
        elif ballX < (BALL_SIZE / 2):
            player2Score += 1
            ball_x_magnitude = 0.3
            ball_x_direction = 1
            ball_y_magnitude = 0.3
            ball_y_direction = 1
            ballX = 400
            ballY = 300
            #wait(3000)
            point_scored = True


        paddle1 = pygame.Rect(p1x,p1y,PADDLE_WIDTH,PADDLE_HEIGHT)
        paddle2 = pygame.Rect(p2x,p2y,PADDLE_WIDTH,PADDLE_HEIGHT)
        ball = pygame.Rect(ballX, ballY, BALL_SIZE, BALL_SIZE)
        #if point scored, reset
        if paddle1.colliderect(ball):
            #increment speed
            ball_x_magnitude *= 1.2
            ball_x_direction *= -1
            #calculate new angle of ball
            temp = abs(ballY - p1y)
            temp = abs(PADDLE_HEIGHT / 2 - temp)
            ball_y_direction = temp / 15
        if paddle2.colliderect(ball):
            ball_x_magnitude *= 1.2
            ball_x_direction *= -1
            #calculate new angle of ball
            temp = abs(ballY - p2y)
            temp = abs(PADDLE_HEIGHT / 2 - temp)
            ball_y_direction = temp / 15












        pygame.display.update()
        surface.fill(BLACK)
        player_text = font.render(' ' + str(player1Score) + ' | ' + str(player2Score), False, (255,255,255))

        surface.blit(player_text, (HEIGHT/2 + 50,0))
        pygame.draw.rect(surface, WHITE, paddle1)
        pygame.draw.rect(surface, WHITE, paddle2)
        pygame.draw.rect(surface, WHITE, ball)





main()
print("helloworld")
input('Press ENTER to exit')
