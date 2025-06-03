import random
import pygame

# pygame setup
pygame.init()
#screen = pygame.display.set_mode((1920, 1080))

screen_height = 720
screen_width = 1280
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = False
pygame.display.set_caption("Pong")

# dimension paddle variable
paddle_width = 20
paddle_height = 150
left_paddle_x = 50
right_paddle_x = screen_width - 50
left_paddle_y = 310
right_paddle_y = 310
paddle_speed = 7

# Ball variable dimension & speed
ball_x = screen_width // 2
ball_y = random.randint(50, screen_height - 50)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
ball_radius = 30

# Score variable
left_score = 0
right_score = 0

# Global variables for options
ball_speed = 7

def update_ball_speed():
    global ball_speed_x, ball_speed_y
    ball_speed_x = ball_speed * random.choice((1, -1))
    ball_speed_y = ball_speed * random.choice((1, -1))

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

def draw_options(selected_option):
    global ball_speed, paddle_height
    screen.fill("pink")
    font = pygame.font.Font(None, 74)
    text_ball_speed = font.render(f"Vitesse: {ball_speed}", True, "white")
    text_paddle_height = font.render(f"Longueur: {paddle_height}", True, "white")
    text_back = font.render("Retour", True, "white")

    # Highlight selected option
    if selected_option == 0:
        text_ball_speed = font.render(f"Vitesse: {ball_speed}", True, "yellow")
    elif selected_option == 1:
        text_paddle_height = font.render(f"Longueur: {paddle_height}", True, "yellow")
    elif selected_option == 2:
        text_back = font.render("Retour", True, "yellow")

    screen.blit(text_ball_speed, (screen_width // 2 - text_ball_speed.get_width() // 2, screen_height // 2 - 100))
    screen.blit(text_paddle_height, (screen_width // 2 - text_paddle_height.get_width() // 2, screen_height // 2 - 25))
    screen.blit(text_back, (screen_width // 2 - text_back.get_width() // 2, screen_height // 2 + 50))

    pygame.display.flip()

    return text_ball_speed, text_paddle_height, text_back

def ball_animation():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, left_score, right_score

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Screen animation
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_speed_y *= -1
    if ball_x - ball_radius <= 0:
        right_score += 1
        reset()
    if ball_x + ball_radius >= screen_width:
        left_score += 1
        reset()

    # Paddle animation with ball
    if (left_paddle_y <= ball_y <= left_paddle_y + paddle_height and
        left_paddle_x <= ball_x - ball_radius <= left_paddle_x + paddle_width):
        ball_speed_x *= -1

    if (right_paddle_y <= ball_y <= right_paddle_y + paddle_height and
        right_paddle_x <= ball_x + ball_radius <= right_paddle_x + paddle_width):
        ball_speed_x *= -1

def reset():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, left_paddle_y, right_paddle_y, left_score, right_score
    ball_x = screen_width // 2
    ball_y = random.randint(50, screen_height - 50)
    update_ball_speed()
    left_paddle_y = 310
    right_paddle_y = 310

# Menu
in_menu = True
selected_option = 0  # 0: Jouer, 1: Options, 2: Quitter
text_play, text_options, text_quit = draw_menu(selected_option)

while running or in_menu:
    if in_menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if selected_option == 0: # Jouer
                        in_menu = False
                        running = True
                    elif selected_option == 1: # Options
                        in_options = True
                        selected_option_options = 0  # 0: Vitesse, 1: Longueur, 2: Retour

                        # Option
                        while in_options:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        in_options = False
                                    elif event.key == pygame.K_UP:
                                        selected_option_options = (selected_option_options - 1) % 3
                                    elif event.key == pygame.K_DOWN:
                                        selected_option_options = (selected_option_options + 1) % 3
                                    elif event.key == pygame.K_LEFT: #Minimum
                                        if selected_option_options == 0:
                                            ball_speed = max(ball_speed - 1, 1)
                                        elif selected_option_options == 1:
                                            paddle_height = max(paddle_height - 10, 50)
                                    elif event.key == pygame.K_RIGHT: #Maximum
                                        if selected_option_options == 0:
                                            ball_speed = min(ball_speed + 1, 15)
                                        elif selected_option_options == 1:
                                            paddle_height = min(paddle_height + 10, 300)
                                    elif event.key == pygame.K_SPACE and selected_option_options == 2: # Retour
                                        in_options = False
                                        in_menu = True
                                        text_play, text_options, text_quit = draw_menu(selected_option)
                            text_ball_speed, text_paddle_height, text_back = draw_options(selected_option_options)

                    elif selected_option == 2: # Quitter
                        in_menu = False
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Echap
                        in_menu = False
                        running = False

                # Option suivante, et précédente
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % 3
                    if event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % 3

            # Mouse position code
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
        print(f"in_menu: {in_menu}, running : {running}")
        continue

    # pygame.QUIT lorsque le X button est pressé
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                in_menu = True
                text_play, text_options, text_quit = draw_menu(selected_option)
                running = False
                left_score = 0
                right_score = 0
                reset()

    # Afficher l'état des variables in_menu et game_run
    print(f"in_menu: {in_menu}, running : {running}, Score Left : {left_score}, Score Right : {right_score}")

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

    # Draw scores
    font = pygame.font.Font(None, 74)
    left_score_text = font.render(str(left_score), True, "white")
    right_score_text = font.render(str(right_score), True, "white")
    screen.blit(left_score_text, (screen_width // 4, 20))
    screen.blit(right_score_text, (3 * screen_width // 4, 20))

    # screen work
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60