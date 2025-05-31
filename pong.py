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

def draw_menu(selected_option):
    screen.fill("pink")
    font = pygame.font.Font(None, 74)
    text_play = font.render("Jouer", True, "white")
    text_options = font.render("Options", True, "white")
    text_quit = font.render("Quitter", True, "white")

    # Highlight selected option
    if selected_option == 0:
        text_play = font.render("Jouer", True, "yellow")
    elif selected_option == 1:
        text_options = font.render("Options", True, "yellow")
    elif selected_option == 2:
        text_quit = font.render("Quitter", True, "yellow")

    screen.blit(text_play, (screen_width // 2 - text_play.get_width() // 2, screen_height // 2 - 100))
    screen.blit(text_options, (screen_width // 2 - text_options.get_width() // 2, screen_height // 2 - 25))
    screen.blit(text_quit, (screen_width // 2 - text_quit.get_width() // 2, screen_height // 2 + 50))
    pygame.display.flip()

    return text_play, text_options, text_quit

# Menu
in_menu = True
selected_option = 0  # 0: Jouer, 1: Options, 2: Quitter
text_play, text_options, text_quit = draw_menu(selected_option)

while in_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_menu = False
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if selected_option == 0:
                    in_menu = False
                elif selected_option == 2:
                    in_menu = False
                    running = False
            if event.key == pygame.K_ESCAPE:
                in_menu = False
                running = False
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % 3
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (screen_width // 2 - text_play.get_width() // 2 <= mouse_x <= screen_width // 2 + text_play.get_width() // 2 and
                screen_height // 2 - 100 <= mouse_y <= screen_height // 2 - 100 + text_play.get_height()):
                in_menu = False
                running = True
            elif (screen_width // 2 - text_quit.get_width() // 2 <= mouse_x <= screen_width // 2 + text_quit.get_width() // 2 and
                  screen_height // 2 + 50 <= mouse_y <= screen_height // 2 + 50 + text_quit.get_height()):
                in_menu = False
                running = False

    text_play, text_options, text_quit = draw_menu(selected_option)

def reset():
    global in_menu, selected_option, running, ball_x, ball_y, ball_speed_x, ball_speed_y, left_paddle_y, right_paddle_y
    in_menu = True
    selected_option = 0
    running = True
    ball_x = screen_width // 2
    ball_y = random.randint(50, screen_height - 50)
    ball_speed_x = 7 * random.choice((1, -1))
    ball_speed_y = 7 * random.choice((1, -1))
    left_paddle_y = 310
    right_paddle_y = 310


while running:
    # pygame.QUIT lorsque le X button est pressé
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                in_menu = True
                running = True
                break
                

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