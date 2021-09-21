import pygame
import time
import random


#Инициализируем приложение pygame
pygame.init()

#Размеры окна
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

#Цвета экрана, змейки, сообщения
green = (0, 255, 0)
black = (0, 0, 0)
red = (213, 50, 80)

#Начальный размер змейки
segment_size = 20
#Скорость движения змейки
snake_speed = 8

#Расположение змейки по середине
head_x = width // 2 // segment_size * segment_size
head_y = height // 2 // segment_size * segment_size

#создаем метод генерирующий рандомную точку кратную segment_size 
def get_random_point():
    x = random.randint(0, width - segment_size) // segment_size * segment_size
    y = random.randint(0, height - segment_size) // segment_size * segment_size
    return x, y

#вызываем метод с координатами рандомной точки
food_x, food_y = get_random_point()

#Переменные скорость
vx = 0
vy = 0


clock = pygame.time.Clock()

while True:
    
    #если змейка выходит за пределы экрана
    if head_x < 0 or head_x > width - segment_size or head_y < 0 or head_y > height - segment_size:
        #использовать шрифт и размер для
        font = pygame.font.SysFont("None", 35)
        #сообщения о проиграше
        message = font.render("Вы проиграли!", True, red) #msg, True, color
        #вывести сообщение в конкретном месте
        display.blit(message, [width / 6, height / 3])
        #наше обновление появилось у пользователя
        pygame.display.flip()
        
        #задержка сообщения, чтоб не исчезала мгновенно
        time.sleep(2)
        #закрыть экран
        pygame.quit()
        quit()
        
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vy = segment_size
                vx = 0
            elif event.key == pygame.K_UP:
                vy = -segment_size
                vx = 0
            elif event.key == pygame.K_LEFT:
                vy = 0
                vx = -segment_size
            elif event.key == pygame.K_RIGHT:
                vy = 0
                vx = segment_size 
    
    head_x += vx
    head_y += vy
    
    #залить экран зеленым цветом
    display.fill(green)
    
    #отобразить food квадратом на экране с красным цветом
    pygame.draw.rect(display, red, [food_x, food_y, segment_size, segment_size])
    
    #отобразить змейку квадратом на экране в черном цвете
    pygame.draw.rect(display, black, [head_x, head_y, segment_size, segment_size])
    
    #проверка съела ли змейка еду, совпадение координат
    #если съела, то выдаем новую еду с новыми рандомными координатами
    if head_x == food_x and head_y == food_y:
        food_x, food_y = get_random_point()
        
    
    #Выполнить команды, вывести на дисплее 
    pygame.display.flip()
    clock.tick(snake_speed)