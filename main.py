import pygame
class Food():
    def __init__(self, a, c, d):
        self.image = pygame.image.load(a)# загружаем картинку
        self.rect = self.image.get_rect()# получение прямоугольника от картинки
        self.x = c #свойство объекта, координата x
        self.y = d

    def move_plate(self): #
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
             self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5


    def draw_image(self):  #метод отрисовки картинки
        screen.blit(self.image, (self.x, self.y))


fon = Food('kitchen.jpg', 0, 0 ) #создание объекта класса food
f1 = Food('pelmen.png', 0, 0 )
f2 = Food('pelmen.png', 110, 0 )
f3 = Food('pelmen.png', 220, 0 )
f4 = Food('pelmen.png', 330, 0 )
f5 = Food('pelmen.png', 440, 0 )
plate = Food('plate.png', 380, 600)

pygame.init() #обязательная программа
window_size=(1000 , 700) #размеры окна
screen=pygame.display.set_mode(window_size) #создаем экран с размерами
pygame.display.set_caption("Doom eternal") #название игры
clock = pygame.time.Clock()

while True:
    fon.draw_image()#применение метода отрисовки картинки
    plate.move_plate()
    f1.draw_image()
    f2.draw_image()
    f3.draw_image()
    f4.draw_image()
    f5.draw_image()
    plate.draw_image()
    clock.tick(123)# считаем фпс
    for event in pygame.event.get(): # ходим по событиям
        if event.type == pygame.QUIT: # нажали на крестик
            pygame.QUIT() # вышли из игры
    pygame.display.update() # обнова экрана
