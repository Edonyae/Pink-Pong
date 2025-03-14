import random
import pygame

# pygame setup
pygame.init()
#screen = pygame.display.set_mode((1920, 1080))

screen_height = 720
screen_width = 1280
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Pong")


# dimension paddle variable

paddle_width = 20
paddle_height = 150
left_paddle_x = 50
right_paddle_x = screen_width - 50
left_paddle_y = 310
right_paddle_y = 310
paddle_speed=7

# Ball variable dimension & speed

ball_x = screen_width // 2
ball_y = random.randint(50, screen_height - 50)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
ball_radius = 30

def ball_animation():
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Screen animation
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_speed_y *= -1
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_speed_x *= -1

    # Paddle animation with ball
    if (left_paddle_y <= ball_y <= left_paddle_y + paddle_height and
        left_paddle_x <= ball_x - ball_radius <= left_paddle_x + paddle_width):
        ball_speed_x *= -1

    if (right_paddle_y <= ball_y <= right_paddle_y + paddle_height and
        right_paddle_x <= ball_x + ball_radius <= right_paddle_x + paddle_width):
        ball_speed_x *= -1

# Draw menu

def drawmenu ():
    screen.fill("pink")
    font = pygame.font.Font(None, 74)
    text_play = font.render("Jouer", True, "white")
    text_quit = font.render("Quitter", True, "white")
    screen.blit(text_play, (screen_width // 2 - text_play.get_width() // 2, screen_height // 2 - 50))
    screen.blit(text_quit, (screen_width // 2 - text_quit.get_width() // 2, screen_height // 2 + 50))
    pygame.display.flip()

# Menu

in_menu = True
while in_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_menu = False
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                in_menu = False
                running = True
            if event.key == pygame.K_ESCAPE:
                in_menu = False
                running = False

    drawmenu()
    clock.tick(60)

while running:
    # pygame.QUIT lorsque le X button est pressé
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get the key
    
    keys = pygame.key.get_pressed()
    
    # Left paddle move
    
    if keys[pygame.K_z] and left_paddle_y - paddle_speed >= 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y + paddle_speed <= screen_height - paddle_height:
        left_paddle_y += paddle_speed
        
    # Right paddle move
    
    if keys[pygame.K_UP] and right_paddle_y - paddle_speed >= 0:
        right_paddle_y -= paddle_speed

    if keys[pygame.K_DOWN] and right_paddle_y + paddle_speed <= screen_height - paddle_height:
        right_paddle_y += paddle_speed

    
    
    ball_animation()


    # Game Render
    screen.fill("pink")

    # Paddle Draw
    pygame.draw.rect(screen, (255, 255, 255), (left_paddle_x, left_paddle_y, paddle_width, paddle_height)) # left paddle
    pygame.draw.rect(screen, (255, 255, 255), (right_paddle_x, right_paddle_y, paddle_width, paddle_height)) # right paddle
    
    # draw circle
    ball = pygame.draw.circle(screen, (255,255,255), (ball_x, ball_y), ball_radius)
        
    for i in range(10, 720, 20):  # Draws a dashed line from top to bottom
        pygame.draw.rect(screen, (255, 255, 255), (638, i, 4, 10))
    
    # screen work
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()