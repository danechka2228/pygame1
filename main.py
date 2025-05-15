from random import *
import pygame # импортируем библеотеку ыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы
class Demon(): # создание класса
    def __init__(self, a, c, d): # создание конструктора в нем создаются свойства , вызывается при создании объекта
        self.image = pygame.image.load(a)# загружаем картинку, это свойство
        self.rect = self.image.get_rect()# получение прямоугольника от картинки , тоже свойство
        self.rect.x = c #свойство объекта, координата x
        self.rect.y = d #координата у , свойство объекта

    def move_slayer(self): #
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] == True:
            self.rect.x -= 9.7  # движение объекта
        if keys[pygame.K_d]:
            self.rect.x += 9.7  # движение объекта
        if keys[pygame.K_w]:
            self.rect.y -= 8.4  # движение объекта
        if keys[pygame.K_s]:
            self.rect.y += 8.4  # движение объекта
    def move_food(self):
        self.rect.y += 3.6
        if self.rect.y > 900:
            self.rect.y = -100

    def draw_image(self):  #метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))





q = randint(-1000 , 0)
t = randint(-1000 , 0)
h = randint(-1000 , 0)
g = randint(-1000 , 0)
f = randint(-1000 , 0)
j = randint(-1000 , 0)
k = randint(-1000 , 0)
u = randint(-1000 , 0)

fon = Demon('ad1 (1).jpg', 0, 0 ) #создание объекта класса food
f1 = Demon('demon1 (2).png', 50,  t)#создание объекта класса food
f2 = Demon('demon2.png', 350, q )#создание объекта класса food
f3 = Demon('demon3 (1).png', 660, g )#создание объекта класса food
f4 = Demon('demon2.png', 750, f )#создние объекта класса food
f5 = Demon('demon3 (1).png', 880, u )#создние объекта класса food
f6 = Demon('demon2.png', 1000, k )#создние объекта класса food
f7 = Demon('demon2.png', 1300, j )#создние объекта класса food
f8 = Demon('demon1 (2).png', 1360, h )#создние объекта класса food
slayer = Demon('doom_slayer.png', 380, 600)#создание объекта класса food
demon_list = [f1 , f2 , f3 , f4, f5 ,f6 , f7 , f8 ]




pygame.init() #обязательная функция
window_size=(1840 , 910) #размеры окна
screen=pygame.display.set_mode(window_size) #создаем экран с размерами
pygame.display.set_caption("Doom: The Dark Ages") #название игры
clock = pygame.time.Clock()
bullets = []

while True:# игровой цикл

    fon.draw_image()#применение метода отрисовки картинки
    slayer.move_slayer()#применение метода отрисовки картинки
    slayer.draw_image()#применение метода отрисовки картинки
    clock.tick(67)# фпс
    for i in bullets:
        i.draw_image()
        i.rect.y -= 14
        for j in demon_list:
            if i.rect.colliderect(j.rect):
                demon_list.remove(j)
                bullets.remove(i)
    for i in demon_list:
        i.draw_image()
        i.move_food()

    if demon_list == [ ]:
        pygame.exit()
    for event in pygame.event.get(): # ходим по событиям
        if event.type == pygame.QUIT: # нажали на крестик
            pygame.QUIT() # вышли из игры
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Demon("fire_boll.png", slayer.rect.x,slayer.rect.y)
            bullets.append(bullet)
    pygame.display.update() # обнова экрана





