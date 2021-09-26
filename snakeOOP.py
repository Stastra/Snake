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

#шрифт и размер 
font = pygame.font.SysFont("None", 35)

#Цвета экрана, змейки, сообщения
green = (0, 255, 0)
black = (0, 0, 0)
red = (213, 50, 80)

#Начальный размер змейки
segment_size = 20
#Скорость движения змейки
snake_speed = 5

#Расположение змейки по середине
head_x = width // 2 // segment_size * segment_size
head_y = height // 2 // segment_size * segment_size

#создаем метод генерирующий рандомную точку кратную segment_size 
def get_random_point():
    x = random.randint(0, width - segment_size) // segment_size * segment_size
    y = random.randint(0, height - segment_size) // segment_size * segment_size
    return x, y

#отображаем список змейки, т.е. змейку с новой длинной
def show_snake(snake):
    for x in snake:
        pygame.draw.rect(display, black, [x[0], x[1], segment_size, segment_size])
        
#создали счетчик съеденых фруктов
def show_score(score):
    value = font.render("Очки: " + str(score), True, black)
    display.blit(value, [0, 0])

#вызываем метод с координатами рандомной точки
food_x, food_y = get_random_point()


#создаем пустой список
snake = []
#реальная длина змейки
snake_length = 1


#Переменные скорость
vx = 0
vy = 0


clock = pygame.time.Clock()

while True:
    
    #если змейка выходит за пределы экрана
    if head_x < 0 or head_x > width - segment_size or head_y < 0 or head_y > height - segment_size:
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
    
    #задали движение змейке
    head_x += vx
    head_y += vy
    
    #залить экран зеленым цветом
    display.fill(green)
    
    #отобразить food квадратом на экране с красным цветом
    pygame.draw.rect(display, red, [food_x, food_y, segment_size, segment_size])
    
    #отобразить змейку, если фрукт не съеден, то удаляем хвост, оставляем прежний размер
    snake.append((head_x, head_y))
    if len(snake) > snake_length:
        del snake[0]
        
    #отобразить змейку и очки
    show_snake(snake)
    show_score(snake_length - 1)
    
    #отобразить голову змейки квадратом на экране в черном цвете
    #pygame.draw.rect(display, black, [head_x, head_y, segment_size, segment_size])
    
    #проверка съела ли змейка еду, совпадение координат
    #если съела, то выдаем новую еду с новыми рандомными координатами
    #и увеличиваем длину змейки на единицу, обновляем и выдаем новую длину змейки
    if head_x == food_x and head_y == food_y:
        food_x, food_y = get_random_point()
        snake_length += 1
        
    
    #Выполнить команды, вывести на дисплее 
    pygame.display.flip()
    clock.tick(snake_speed)