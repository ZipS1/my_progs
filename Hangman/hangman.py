import pygame
import math
import random

pygame.init()

# setup display
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# setup buttons
RADIUS = 20
GAP = 15 
letters = []
startx = round((WIDTH - (RADIUS*2 + GAP)*13 ) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Words
words = ["HELLO", "PYTHON", "IDE", "SUBLIME", "DEVELOPER", "HANGMAN"]

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, ((WIDTH - text.get_width())/2, (HEIGHT - text.get_height())/2))
    pygame.display.update()
    pygame.time.delay(3000)

def draw():
    win.fill(WHITE)

    #draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, ((WIDTH - text.get_width())/2, 20))

    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400,200))

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def main():
    global hangman_status
    # setup game loop
    run = True

    # game loop
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("YOU WON!")
            return

        if hangman_status == 6:
            display_message("YOU LOST!")
            return

def draw_menu():
    win.fill(WHITE)
    text = LETTER_FONT.render('Would you like to play again?', 1, BLACK)
    win.blit(text, ((WIDTH - text.get_width())/2, 150))
    pygame.draw.rect(win, BLACK, (WIDTH/2 - 170, 200, 150, 50), 3)
    pygame.draw.rect(win, BLACK, (WIDTH/2 + 20, 200, 150, 50), 3)
    text = LETTER_FONT.render('YES', 1, BLACK)
    win.blit(text, ((WIDTH/2 - 95) - text.get_width()/2, 225 - text.get_height()/2))
    text = LETTER_FONT.render('NO', 1, BLACK)
    win.blit(text, ((WIDTH/2 + 95) - text.get_width()/2, 225 - text.get_height()/2))
    pygame.display.update()

# setup main loop
first = True
run = True
clock = pygame.time.Clock()
FPS = 60

# main loop
while True:
    if not first:
        while run:
            clock.tick(FPS)
            draw_menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    if m_x > WIDTH/2 - 170 and m_x < WIDTH/2 - 20 \
                             and m_y > 200 and m_y < 250:
                        run = False
                        break
                    if m_x > WIDTH/2 +20 and m_x < WIDTH/2 + 170 \
                             and m_y > 200 and m_y < 250:
                        pygame.quit()
    run = True

    #reset variables
    for letter in letters:
        letter[3] = True
    hangman_status = 0
    word = random.choice(words)
    guessed = []

    main()
    first = False
