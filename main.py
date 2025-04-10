import pygame # импортируем библеотеку ыыыыы
class Food(): # создание класса
    def __init__(self, a, c, d): # создание конструктора в нем создаются свойства , вызывается при создании объекта
        self.image = pygame.image.load(a)# загружаем картинку, это свойство
        self.rect = self.image.get_rect()# получение прямоугольника от картинки , тоже свойство
        self.rect.x = c #свойство объекта, координата x
        self.rect.y = d #координата у , свойство объекта

    def move_plate(self): #
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
             self.rect.x -= 5 # движение объекта
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5  # движение объекта

    def move_food(self):
        self.rect.y += 5
        if self.rect.y == 700:
            self.rect.y = 0

    def draw_image(self):  #метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))


fon = Food('kitchen.jpg', 0, 0 ) #создание объекта класса food
f1 = Food('pelmen.png', 50, 0 )#создание объекта класса food
f2 = Food('cheesburger.png', 300, 0 )#создание объекта класса food
f3 = Food('pelmen.png', 500, 0 )#создание объекта класса food
f4 = Food('gummy bear.png', 700, 0 )#создание объекта класса food
f5 = Food('pelmen.png', 900, 0 )#создание объекта класса food
plate = Food('plate.png', 380, 600)#создание объекта класса food

pygame.init() #обязательная программа
window_size=(1000 , 700) #размеры окна
screen=pygame.display.set_mode(window_size) #создаем экран с размерами
pygame.display.set_caption("Doom eternal") #название игры
clock = pygame.time.Clock()

while True:# игровой цикл

    fon.draw_image()#применение метода отрисовки картинки
    plate.move_plate()#применение метода отрисовки картинки
    f1.draw_image()#применение метода отрисовки картинки
    f2.draw_image()#применение метода отрисовки картинки
    f3.draw_image()#применение метода отрисовки картинки
    f4.draw_image()#применение метода отрисовки картинки
    f5.draw_image()#применение метода отрисовки картинки
    plate.draw_image()#применение метода отрисовки картинки
    clock.tick(65)# фпс
    for event in pygame.event.get(): # ходим по событиям
        if event.type == pygame.QUIT: # нажали на крестик
            pygame.QUIT() # вышли из игры
    f1.move_food()#применение метода отрисовки картинки
    f2.move_food()#применение метода отрисовки картинки
    f3.move_food()#применение метода отрисовки картинки
    f4.move_food()#применение метода отрисовки картинки
    f5.move_food()#применение метода отрисовки картинки
    pygame.display.update() # обнова экрана

