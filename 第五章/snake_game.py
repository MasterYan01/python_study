import pygame
import time
import random

# 初始化 Pygame
pygame.init()

# 設置遊戲視窗大小
window_x = 720
window_y = 480

# 定義遊戲顏色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# 設置遊戲視窗
pygame.display.set_caption('貪吃蛇遊戲')
game_window = pygame.display.set_mode((window_x, window_y))

# 設置幀率控制
fps = pygame.time.Clock()

# 定義蛇的初始位置
snake_position = [100, 50]

# 定義蛇的初始身體
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# 定義食物位置
food_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
food_spawn = True

# 設置蛇的方向
direction = 'RIGHT'
change_to = direction

# 設置初始分數
score = 0

# 定義顯示分數的函數
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# 定義遊戲結束函數
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# 主循環
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'DOWN':
                    change_to = 'UP'
            if event.key == pygame.K_DOWN:
                if direction != 'UP':
                    change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                if direction != 'RIGHT':
                    change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                if direction != 'LEFT':
                    change_to = 'RIGHT'

    if change_to == 'UP':
        direction = 'UP'
    if change_to == 'DOWN':
        direction = 'DOWN'
    if change_to == 'LEFT':
        direction = 'LEFT'
    if change_to == 'RIGHT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (window_x//10)) * 10,
                         random.randrange(1, (window_y//10)) * 10]
    food_spawn = True

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(25)

