import pygame
from pygame.locals import *
import random
import time

pygame.font.init()
pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 700, 400

MUS_WIN = pygame.mixer.Sound('Assets/win.wav')
MUS_LOSE = pygame.mixer.Sound('Assets/lose.wav')
pygame.mixer.music.set_volume(0.1)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing speed")

FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BACKGROUND = (200,200,200)
BUTTON_RES = pygame.Rect(WIDTH/2, WIDTH/2-50, 100, 40)
BUTTON_EX = pygame.Rect(WIDTH/3, WIDTH/2-50, 100, 40)
SCORE = 0

def rand_phrase():
    phrase = ['The future belongs to those who believe in the beauty of their dreams.', 'Tell me and I forget. Teach me and I remember. Involve me and I learn.',
              'Whoever is happy will make others happy too.', 'Always remember that you are absolutely unique. Just like everyone else.',
              'Whoever is happy will make others happy too.', 'You will face many defeats in life, but never let yourself be defeated.',
              'The purpose of our lives is to be happy.','Live in the sunshine, swim the sea, drink the wild air.',
              'May you live all the days of your life.','Life is a long lesson in humility.',
              'Love the life you live. Live the life you love.', 'I never dreamed about success, I worked for it.',
              'Before anything else, preparation is the key to success.', 'Winning isn\'t everything, but wanting to win is.']
    return random.choice(phrase)

def avr_speed(text, times):
    speed = '%.3f'%(times/len(text))
    global SCORE
    if times/len(text) <= 0.3:
        SCORE += 1
        pygame.mixer.Sound.play(MUS_WIN)
        return "You are very fast, your average speed is " + speed + " characters per second"
    else:
        SCORE = 0
        pygame.mixer.Sound.play(MUS_LOSE)
        return "You are very slow, your average speed is " + speed + " characters per second"

def draw_win(text):
    font = pygame.font.SysFont(text, 28)
    img = font.render(text, True, WHITE)
    place = img.get_rect(
        center=(WIDTH/2, 50))
    WIN.blit(img, place)
    pygame.display.update()
    pygame.time.delay(5000)

def butt_res():
    pygame.draw.rect(WIN, RED, BUTTON_RES)
    font = pygame.font.SysFont(None, 28)
    img = font.render("RESTART", True, (0, 0, 0))
    rect = img.get_rect(
        center=(WIDTH/2+50, HEIGHT-80))
    WIN.blit(img, rect)

def butt_ex():
    pygame.draw.rect(WIN, RED, BUTTON_EX)
    font = pygame.font.SysFont(None, 28)
    img = font.render("EXIT", True, (0, 0, 0))
    rect = img.get_rect(
        center=(WIDTH/3+50, HEIGHT-80))
    WIN.blit(img, rect)


def timer():
    font = pygame.font.SysFont(None, 100)
    img = font.render("GET READY!", True, WHITE)
    place = img.get_rect(
        center=(WIDTH/2, HEIGHT/2+60))
    WIN.blit(img, place)
    pygame.display.update()
    pygame.time.delay(1000)

def score(sc):
    text = "SCORE: " + str(sc)
    font = pygame.font.SysFont(text, 28)
    img = font.render(text, True, BLACK)
    rect = img.get_rect(
        center=(WIDTH / 2, HEIGHT - 40))
    WIN.blit(img, rect)


def main():
    start_ticks = pygame.time.get_ticks()
    global SCORE

    #A RANDOM PHRASE THAT WE SHOULD TO WRITE
    phrase = rand_phrase()
    font1 = pygame.font.SysFont(phrase, 28)
    img1 = font1.render(phrase, True, BLACK)
    rect1 = img1.get_rect(
        center=(WIDTH/2, 200))

    #WRITING A PHRASE
    text = ""
    font = pygame.font.SysFont(None, 28)
    img = font.render(text, True, BLACK)
    rect = img.get_rect(
        center=(rect1.x, 150))
    cursor = Rect(rect.topright, (3, rect.height))


    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]
                else:
                    text += event.unicode
                img = font.render(text, True, BLACK)
                rect.size = img.get_size()
                cursor.topleft = rect.topright

        if text == phrase:
            draw_win(avr_speed(phrase, seconds))
            timer()
            break

        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            if 350 < x < 450 and 300 < y < 335:
                SCORE = 0
                timer()
                break
            elif 231 < x < 330 and 300 < y < 335:
                pygame.quit()
                exit()


        WIN.fill(BACKGROUND)
        WIN.blit(img1, rect1)
        WIN.blit(img, rect)
        butt_ex()
        butt_res()

        score(SCORE)

        if time.time() % 1 > 0.5:
            pygame.draw.rect(WIN, BLACK, cursor)
        pygame.display.update()

    main()


if __name__ == "__main__":
    main()
