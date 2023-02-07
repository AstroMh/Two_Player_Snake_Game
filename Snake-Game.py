# Don't touch, it works XD

# Mystery Boxes coming soon
# New bug fixes will be added
# level difficulty will also be added
# maybe changing some textures in the future

# 10% of the code below is from the internet that includes(the entire artwork and images, I didn't Design them)
# 4% of this game and its logics are from Stack-Overflow

# Snake-Game By Astr0

import pygame
from pygame.locals import *
import time
import random
import timer
import os
from time import sleep

Size = 40
BackGround_Color = (12, 145, 47)
joysticks = []

class Coin:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('C:/Users/MELAL/Downloads/Coin.png').convert_alpha()
        self.parent_screen = parent_screen
        self.x = random.randint(1, 1599)
        self.y = random.randint(1, 844)

    def draw(self):
        self.parent_screen.blit(pygame.transform.scale(self.image, (45, 45)), (self.x, self.y))

    def move(self):
        self.x = random.randint(1, 31) * Size
        self.y = random.randint(0, 15) * Size

class Coin2:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('C:/Users/MELAL/Downloads/star.png').convert_alpha()
        self.parent_screen = parent_screen
        self.x = random.randint(1, 1599)
        self.y = random.randint(1, 844)

    def draws(self):
        self.parent_screen.blit(pygame.transform.scale(self.image, (45, 45)), (self.x, self.y))

    def moves(self):
        self.x = random.randint(1, 31) * Size
        self.y = random.randint(0, 15) * Size

class Bomb:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('C:/Users/MELAL/Downloads/bomb.png')
        self.parent_screen = parent_screen
        self.x = random.randint(1, 1595)
        self.y = random.randint(1, 840)

    def drawb(self):
        self.parent_screen.blit(pygame.transform.scale(self.image, (50, 50)), (self.x, self.y))

    def moveb(self):
        self.x = random.randint(1, 31) * Size
        self.y = random.randint(0, 15) * Size

class Invader:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('C:/Users/MELAL/Downloads/cou.png')
        self.parent_screen = parent_screen
        self.x = random.randint(1, 1595)
        self.y = random.randint(1, 840)

    def drawI(self):
        self.parent_screen.blit(pygame.transform.scale(self.image, (55, 55)), (self.x, self.y))

    def moveI(self):
        self.x = random.randint(1, 31) * Size
        self.y = random.randint(0, 15) * Size

class Zap:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('C:/Users/MELAL/Downloads/Elec.png')
        self.parent_screen = parent_screen
        self.x = random.randint(1, 1599)
        self.y = random.randint(1, 844)

    def drawz(self):
        self.parent_screen.blit(pygame.transform.scale(self.image, (55, 55)), (self.x, self.y))

    def movez(self):
        self.x = random.randint(1, 31) * Size
        self.y = random.randint(0, 15) * Size

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('C:/Users/MELAL/Downloads/circle.png').convert_alpha()
        self.x = [Size] * length
        self.y = [Size] * length
        self.direction = 'down'

    def draw(self):
         for i in range(self.length):
            self.parent_screen.blit(pygame.transform.scale(self.block, (40, 40)), (self.x[i], self.y[i]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'
    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'left':
            self.x[0] -= Size
        if self.direction == 'right':
            self.x[0] += Size
        if self.direction == 'up':
            self.y[0] -= Size
        if self.direction == 'down':
            self.y[0] += Size
        self.draw()

class Snake2:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('C:/Users/MELAL/Downloads/Blue.png').convert_alpha()
        self.x = [Size] * 40
        self.y = [Size] * 40
        self.direction = 'right'

    def draw2(self):
        for i in range(self.length):
            self.parent_screen.blit(pygame.transform.scale(self.block, (40, 40)), (self.x[i], self.y[i]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'
    def walk2(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'left':
            self.x[0] -= Size
        if self.direction == 'right':
            self.x[0] += Size
        if self.direction == 'up':
            self.y[0] -= Size
        if self.direction == 'down':
            self.y[0] += Size
        self.draw2()

class Circle1:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('C:/Users/MELAL/Downloads/Green_Hexagon.png').convert_alpha()
        self.x = [1600] *  random.randint(1, 1599)
        self.y = [84] *  random.randint(1, 840)
        self.direction = 'left'

    def draw_circle1(self):
        for i in range(self.length):
            self.parent_screen.blit(pygame.transform.scale(self.block, (40, 40)), (self.x[i], self.y[i]))

    def walk_circle1(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'left':
            self.x[0] -= Size
        if self.direction == 'right':
            self.x[0] += Size
        if self.direction == 'up':
            self.y[0] -= Size
        if self.direction == 'down':
            self.y[0] += Size
        self.draw_circle1()

class Circle2:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('C:/Users/MELAL/Downloads/Green_Hexagon.png').convert_alpha()
        self.x = [1] *  random.randint(1, 1599)
        self.y = [500] *  random.randint(1, 840)
        self.direction = 'right'

    def draw_circle2(self):
        for i in range(self.length):
            self.parent_screen.blit(pygame.transform.scale(self.block, (40, 40)), (self.x[i], self.y[i]))

    def walk_circle2(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'left':
            self.x[0] -= Size
        if self.direction == 'right':
            self.x[0] += Size
        if self.direction == 'up':
            self.y[0] -= Size
        if self.direction == 'down':
            self.y[0] += Size
        self.draw_circle2()

class Portal:
    def __init__(self, parent_screen):
        self.image = pygame.image.load('C:/Users/MELAL/Downloads/portal1.png')
        self.parent_screen = parent_screen
        self.x = 10
        self.y = 32
    def drawP(self):
        self.parent_screen.blit(pygame.transform.scale(self.image, (70, 55)), (self.x, self.y))


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((1600, 845))
        self.caption = pygame.display.set_caption('Snake Game')
        self.bomb = Bomb(self.surface)
        self.zap = Zap(self.surface)
        self.circle1 = Circle1(self.surface, 3)
        self.circle2 = Circle2(self.surface, 3)
        self.invader = Invader(self.surface)
        self.snake = Snake(self.surface, 3)
        self.portal = Portal(self.surface)
        self.snake2 = Snake2(self.surface, 3)
        self.snake2.draw2()
        self.snake.draw()
        self.snake2.draw2()
        self.bomb.drawb()
        self.zap.drawz()
        self.invader.drawI()
        self.coin = Coin(self.surface)
        self.coin.draw()
        self.coin2 = Coin2(self.surface)
        self.coin2.draws()
        self.circle1.draw_circle1()
        self.music()
        self.render_background()

    def main_menu(self):
        menu = True
        selected = "start"
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            print("Start")
                        if selected == "quit":
                            pygame.quit()
                            quit()
                self.surface.fill(blue)
                title = text_format("Sourcecodester", font, 90, yellow)
                if selected == "start":
                    text_start = text_format("START", font, 75, white)
                else:
                    text_start = text_format("START", font, 75, black)
                if selected == "quit":
                    text_quit = text_format("QUIT", font, 75, white)
                else:
                    text_quit = text_format("QUIT", font, 75, black)
                title_rect = title.get_rect()
                start_rect = text_start.get_rect()
                quit_rect = text_quit.get_rect()
                screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
                screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 300))
                screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 360))
                pygame.display.update()
                clock.tick(FPS)
                pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

    def music(self):
        pygame.mixer.music.load('C:/Users/MELAL/Downloads/jungle.wav')
        pygame.mixer.music.play(-1, 0)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + Size:
            if y1 >= y2 and y1 <= y2 + Size:
                return True
        return False

    def reset1(self):
        self.snake = Snake(self.surface, 3)

    def reset2(self):
        self.snake2 = Snake2(self.surface, 3)

    def render_background(self):
        bg = pygame.image.load("C:/Users/MELAL/Downloads/LEr.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        #self.main_menu()
        self.render_background()
        self.snake2.walk2()
        self.snake.walk()
        self.coin.draw()
        self.coin2.draws()
        self.bomb.drawb()
        self.zap.drawz()
        self.invader.drawI()
        self.circle1.draw_circle1()
        self.circle1.walk_circle1()
        self.circle2.draw_circle2()
        self.circle2.walk_circle2()
        self.display_Score()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.coin.x, self.coin.y):
            sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/Ding.mp3')
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.coin.move()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.coin2.x, self.coin2.y):
            list = [-10, -8, -9, -3, -5, -4, 5, 3, 8, 1]
            Rlist = random.choice(list)
            self.snake.length = int(self.snake.length) + int(Rlist)
            self.coin2.moves()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.bomb.x, self.bomb.y):
            soundb = pygame.mixer.Sound('C:/Users/MELAL/Downloads/ex.wav')
            pygame.mixer.Sound.play(soundb)
            self.snake.length = int(self.snake.length) - 5
            self.bomb.moveb()

        if self.is_collision(self.snake2.x[0], self.snake2.y[0], self.bomb.x, self.bomb.y):
            soundb2 = pygame.mixer.Sound('C:/Users/MELAL/Downloads/ex.wav')
            pygame.mixer.Sound.play(soundb2)
            self.snake2.length = int(self.snake2.length) - 5
            self.bomb.moveb()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.zap.x, self.zap.y):
            soundz = pygame.mixer.Sound('C:/Users/MELAL/Downloads/zap.wav')
            pygame.mixer.Sound.play(soundz)
            self.snake.length = int(self.snake.length) - 2
            self.zap.movez()

        if self.is_collision(self.snake2.x[0], self.snake2.y[0], self.zap.x, self.zap.y):
            soundz2 = pygame.mixer.Sound('C:/Users/MELAL/Downloads/zap.wav')
            pygame.mixer.Sound.play(soundz2)
            self.snake2.length = int(self.snake2.length) - 2
            self.zap.movez()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.invader.x, self.invader.y):
            soundI =  pygame.mixer.Sound('C:/Users/MELAL/Downloads/ko.wav')
            pygame.mixer.Sound.play(soundI)
            self.snake.length = int(self.snake.length) - 3
            self.invader.moveI()

        if self.is_collision(self.snake2.x[0], self.snake2.y[0], self.invader.x, self.invader.y):
            soundI = pygame.mixer.Sound('C:/Users/MELAL/Downloads/ko.wav')
            pygame.mixer.Sound.play(soundI)
            self.snake2.length = int(self.snake2.length) - 3
            self.invader.moveI()

        if self.is_collision(self.circle1.x[0], self.circle1.y[0], self.zap.x, self.zap.y):
            self.zap.movez()
        if self.is_collision(self.circle2.x[0], self.circle2.y[0], self.zap.x, self.zap.y):
            self.zap.movez()
        if self.is_collision(self.circle1.x[0], self.circle1.y[0], self.invader.x, self.invader.y):
            self.invader.moveI()
        if self.is_collision(self.circle2.x[0], self.circle2.y[0], self.invader.x, self.invader.y):
            self.invader.moveI()
        if self.is_collision(self.circle1.x[0], self.circle1.y[0], self.bomb.x, self.bomb.y):
            self.bomb.moveb()
        if self.is_collision(self.circle2.x[0], self.circle2.y[0], self.bomb.x, self.bomb.y):
            self.bomb.moveb()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.snake.length = int(self.snake.length) - 1
                sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/Bip.wav')
                pygame.mixer.Sound.play(sound)

        for i in range(3, self.snake2.length):
            if self.is_collision(self.snake2.x[0], self.snake2.y[0], self.snake2.x[i], self.snake2.y[i]):
                self.snake2.length = int(self.snake2.length) - 1
                sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/Bip.wav')
                pygame.mixer.Sound.play(sound)

        if not (0 <= self.snake.x[0] <= 1600 and 0 <= self.snake.y[0] <= 845):
            self.snake.length = int(self.snake.length) - 1
            sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/Bip.wav')
            pygame.mixer.Sound.play(sound)
            if self.snake.length <= -1:
                self.reset1()
                sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/teleport.wav')
                pygame.mixer.Sound.play(sound)
                self.portal.drawP()

        if not (-1500 <= self.circle1.x[0] <= 2400  and 0 <= self.circle1.y[0] <= 880):
            self.circle1.x = random.randint(1, 1599) * [1600]
            self.circle1.length = int(self.circle1.length) + 2
            if int(self.circle1.length) >= 35:
                self.circle1.length = int(self.circle1.length) - 25

        if not (0 <= self.circle2.x[0] <= 3000 and 0 <= self.circle2.y[0] >= -880):
            self.circle2.x = random.randint(1, 1599) * [1]
            self.circle2.length = int(self.circle2.length) + 2
            if int(self.circle2.length) >= 35:
                self.circle2.length = int(self.circle2.length) - 25

        if self.is_collision(self.snake2.x[0], self.snake2.y[0], self.coin.x, self.coin.y):
            sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/Ding.mp3')
            pygame.mixer.Sound.play(sound)
            self.snake2.increase_length()
            self.coin.move()

        if self.is_collision(self.snake2.x[0], self.snake2.y[0], self.coin2.x, self.coin2.y):
            list = [-10, -8, -9, -3, -5, -4, 5, 3, 8, 1]
            Rlist = random.choice(list)
            self.snake2.length = int(self.snake2.length) + int(Rlist)
            self.coin2.moves()

        for i in range(1, self.circle2.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.circle2.x[i], self.circle2.y[i]):
                self.snake.length = int(self.snake.length) - 4
                sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/elx.wav')
                pygame.mixer.Sound.play(sound)

        for i in range(1, self.circle1.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.circle1.x[i], self.circle1.y[i]):
                self.snake.length = int(self.snake.length) - 4
                sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/elx.wav')
                pygame.mixer.Sound.play(sound)

        for i in range(1, self.circle1.length):
            if self.is_collision(self.snake2.x[0], self.snake2.y[0], self.circle1.x[i], self.circle1.y[i]):
                self.snake2.length = int(self.snake2.length) - 4
                sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/elx.wav')
                pygame.mixer.Sound.play(sound)

        for i in range(1, self.circle2.length):
            if self.is_collision(self.snake2.x[0], self.snake2.y[0], self.circle2.x[i], self.circle2.y[i]):
                self.snake2.length = int(self.snake2.length) - 4
                sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/elx.wav')
                pygame.mixer.Sound.play(sound)

        if not (0 <= self.snake2.x[0] <= 1600 and 0 <= self.snake2.y[0] <= 845):
            self.snake2.length = int(self.snake2.length) - 1
            sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/Bip.wav')
            pygame.mixer.Sound.play(sound)
            if self.snake2.length <= -1:
                self.reset2()
                sound = pygame.mixer.Sound('C:/Users/MELAL/Downloads/teleport.wav')
                pygame.mixer.Sound.play(sound)
                self.portal.drawP()

    def display_Score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f'Player 1 : {int(self.snake.length) - 3}', True, (232, 21, 28)).convert_alpha()
        self.surface.blit(score, (30, 10))
        if int(self.snake.length) - 3 > 1:
            score1 = font.render(f'Player 2 : {int(self.snake2.length) - 3}', True, (14, 114, 201)).convert_alpha()
            self.surface.blit(score1, (30, 50))
        else:
            score1 = font.render(f'Player 2 : {int(self.snake2.length) - 3}', True, (14, 114, 201)).convert_alpha()
            self.surface.blit(score1, (30, 50))

    def show_game_over(self):
        self.render_background()
        sound_gameover = pygame.mixer.Sound('C:/Users/MELAL/Downloads/Win2.wav')
        pygame.mixer.Sound.play(sound_gameover)
        font = pygame.font.SysFont('arial', 30)
        font2 = pygame.font.SysFont('arial', 50)

        if int(self.snake.length) > int(self.snake2.length):
            line1 = font2.render(f'Player 1 Won!', True, (255, 255, 255))
            self.surface.blit(line1, (635, 230))
        elif int(self.snake.length) < int(self.snake2.length):
            line1 = font2.render(f'Player 2 Won!', True, (255, 255, 255))
            self.surface.blit(line1, (635, 230))
        else:
            line1 = font2.render(f"That's a Tie!", True, (255, 255, 255))
            self.surface.blit(line1, (640, 230))
        line2 = font.render('To play again press Enter ... To exit press Escape', True, (255, 255, 255))
        self.surface.blit(line2, (500, 480))
        line3 = font.render(f'Player 1 Score is  ({int(self.snake.length) - 3})', True, (255, 255, 255))
        self.surface.blit(line3, (645, 350))
        line4 = font.render(f'Player 2 Score is  ({int(self.snake2.length) - 3})', True, (255, 255, 255))
        self.surface.blit(line4, (645, 400))
        pygame.mixer.music.pause()

    def reset(self):
        self.snake2 = Snake2(self.surface, 3)
        self.snake = Snake(self.surface, 3)
        self.coin = Coin(self.surface)

    def Help1(self):
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f'W: Move up', True, (255, 255, 255)).convert_alpha()
        line2 = font.render(f'A: Move left', True, (255, 255, 255)).convert_alpha()
        line3 = font.render(f'S: Move down', True, (255, 255, 255)).convert_alpha()
        line4 = font.render(f'D: Move right', True, (255, 255, 255)).convert_alpha()
        line5 = font.render(f'E,F: Change color', True, (255, 255, 255)).convert_alpha()
        self.surface.blit(line1, (30, 150))
        self.surface.blit(line2, (30, 180))
        self.surface.blit(line3, (30, 210))
        self.surface.blit(line4, (30, 240))
        self.surface.blit(line5, (30, 270))

    def Help2(self):
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f'[Arrow up]: Move up', True, (255, 255, 255)).convert_alpha()
        line2 = font.render(f'[Arrow left]: Move left', True, (255, 255, 255)).convert_alpha()
        line3 = font.render(f'[Arrow down]: Move down', True, (255, 255, 255)).convert_alpha()
        line4 = font.render(f'[Arrow right]: Move right', True, (255, 255, 255)).convert_alpha()
        line5 = font.render(f'P,L: Change color', True, (255, 255, 255)).convert_alpha()
        self.surface.blit(line1, (30, 330))
        self.surface.blit(line2, (30, 360))
        self.surface.blit(line3, (30, 390))
        self.surface.blit(line4, (30, 420))
        self.surface.blit(line5, (30, 450))

    def run(self):
        running = True
        pause = False
        time_limit = 5
        start_time = time.time()
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        pause = False
                    elif event.key == K_ESCAPE:
                        running = False
                    elif event.key == ord('h'):
                        self.Help1()
                    elif event.key == ord('m'):
                        self.Help2()
                    elif event.key == ord('w'):
                        self.snake.move_up()
                    elif event.key == K_UP:
                        self.snake2.move_up()
                    elif event.key == ord('s'):
                        self.snake.move_down()
                    elif event.key == K_DOWN:
                        self.snake2.move_down()
                    elif event.key == ord('a'):
                        self.snake.move_left()
                    elif event.key == K_LEFT:
                        self.snake2.move_left()
                    elif event.key == ord('d'):
                        self.snake.move_right()
                    elif event.key == K_RIGHT:
                        self.snake2.move_right()
                    elif event.key == ord('e'):
                        self.snake.block = pygame.image.load('C:/Users/MELAL/Downloads/Yellow.png').convert_alpha()
                    elif event.key == ord('f'):
                        self.snake.block = pygame.image.load('C:/Users/MELAL/Downloads/circle.png').convert_alpha()
                    elif event.key == ord('p'):
                        self.snake2.block = pygame.image.load('C:/Users/MELAL/Downloads/Pink.png').convert_alpha()
                    elif event.key == ord('l'):
                        self.snake2.block = pygame.image.load('C:/Users/MELAL/Downloads/Blue.png').convert_alpha()
                    elif event.type == QUIT:
                        running = False
            pygame.display.flip()

            try:
                if not pause:
                    self.play()
                    font = pygame.font.SysFont('arial', 30)
                    elapsed_time = time.time() - start_time
                    timer = font.render(f'Timer : {int(elapsed_time)} / 120s', True, (255, 255, 255)).convert_alpha()
                    self.surface.blit(timer, (750, 30))
                    if int(elapsed_time) >= 120:
                        self.show_game_over()
                        pause = True
                        self.reset()
                        elapsed_time = 0
                    if int(elapsed_time) % 20 == 1:
                        self.zap.movez()
            except Exception as e:
                pause = True
                self.reset()
            time.sleep(0.01)

if __name__ == '__main__':
    game = Game()
    game.run()