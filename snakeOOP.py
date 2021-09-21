import pygame
import time
import random


#�������������� ���������� pygame
pygame.init()

#������� ����
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

#����� ������, ������, ���������
green = (0, 255, 0)
black = (0, 0, 0)
red = (213, 50, 80)

#��������� ������ ������
segment_size = 20
#�������� �������� ������
snake_speed = 8

#������������ ������ �� ��������
head_x = width // 2 // segment_size * segment_size
head_y = height // 2 // segment_size * segment_size

#������� ����� ������������ ��������� ����� ������� segment_size 
def get_random_point():
    x = random.randint(0, width - segment_size) // segment_size * segment_size
    y = random.randint(0, height - segment_size) // segment_size * segment_size
    return x, y

#�������� ����� � ������������ ��������� �����
food_x, food_y = get_random_point()

#���������� ��������
vx = 0
vy = 0


clock = pygame.time.Clock()

while True:
    
    #���� ������ ������� �� ������� ������
    if head_x < 0 or head_x > width - segment_size or head_y < 0 or head_y > height - segment_size:
        #������������ ����� � ������ ���
        font = pygame.font.SysFont("None", 35)
        #��������� � ���������
        message = font.render("�� ���������!", True, red) #msg, True, color
        #������� ��������� � ���������� �����
        display.blit(message, [width / 6, height / 3])
        #���� ���������� ��������� � ������������
        pygame.display.flip()
        
        #�������� ���������, ���� �� �������� ���������
        time.sleep(2)
        #������� �����
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
    
    #������ ����� ������� ������
    display.fill(green)
    
    #���������� food ��������� �� ������ � ������� ������
    pygame.draw.rect(display, red, [food_x, food_y, segment_size, segment_size])
    
    #���������� ������ ��������� �� ������ � ������ �����
    pygame.draw.rect(display, black, [head_x, head_y, segment_size, segment_size])
    
    #�������� ����� �� ������ ���, ���������� ���������
    #���� �����, �� ������ ����� ��� � ������ ���������� ������������
    if head_x == food_x and head_y == food_y:
        food_x, food_y = get_random_point()
        
    
    #��������� �������, ������� �� ������� 
    pygame.display.flip()
    clock.tick(snake_speed)