import pygame
class Food():
    def __init__(self,a, b, c):
        self.image = pygame.image.load(a)
        self.rect = self.image.get_rect()
        self.x = b
        self.y = c

fon = Food('kitchen.jpg', )

pygame.init() #запомнить
x = 20
y = 20
weight = 100
height = 70
window_size=(1000 , 700)#размеры окна
screen=pygame.display.set_mode(window_size)#создаем экран с размерами
pygame.display.set_caption("Моя игра")#название игры
background_color = (16, 205, 200)#cоздаем цвет фона
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 10)
text = font.render('', True, 371)

while True:
    screen.blit(image, (0, 0))
    r = pygame.Rect(x, y, weight, height)
    pygame.draw.rect(screen, 123456789, r)
    screen.blit(text, (110, 125))
    clock.tick(123)# считаем фпс
    pygame.display.update() # обнова экрана
    for event in pygame.event.get(): # ходим по событиям
        if event.type == pygame.QUIT: # нажали на крестик
            pygame.QUIT() # вышли из игры
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # если клавиша а
        x -= 3
    elif keys[pygame.K_RIGHT]:  # если клавиша а
        x += 3
    elif keys[pygame.K_UP]:  # если клавиша а
        y -= 3
    elif keys[pygame.K_DOWN]:  # если клавиша а
        y += 3
