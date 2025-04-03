import pygame
class Food():
    def __init__(self,a, c, d):
        self.image = pygame.image.load(a)# загружаем картинку
        self.rect = self.image.get_rect()# получение прямоугольника от картинки
        self.x = c
        self.y = d

    def draw_image(self):  #метод отрисовки картинки
        screen.blit(self.image, (self.x, self.y))


fon = Food('kitchen.jpg', 0, 0 )
f1 = Food('pelmen.png', 0, 0 )

pygame.init() #обязательная программа
window_size=(1000 , 700)#размеры окна
screen=pygame.display.set_mode(window_size)#создаем экран с размерами
pygame.display.set_caption("Моя игра")#название игры
clock = pygame.time.Clock()

while True:
    fon.draw_image()#применение метода отрисовки картинки
    f1.draw_image()
    clock.tick(123)# считаем фпс
    for event in pygame.event.get(): # ходим по событиям
        if event.type == pygame.QUIT: # нажали на крестик
            pygame.QUIT() # вышли из игры
    pygame.display.update() # обнова экрана