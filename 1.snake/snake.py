import pygame
import time
import random

pygame.init()

# 游戏窗口的宽度和高度
window_width = 800
window_height = 600

# 设置颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# 创建游戏窗口
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇')

# 设置游戏时钟
clock = pygame.time.Clock()

# 定义蛇的大小
snake_block_size = 10

# 设置字体
font_path = pygame.font.match_font('arial')
font_style = pygame.font.Font(font_path, 50)


def our_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block_size, snake_block_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [window_width / 6, window_height / 3])


def game_loop():
    game_over = False
    game_close = False

    # 初始化蛇的位置
    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    # 初始化蛇的长度
    snake_List = []
    Length_of_snake = 1

    # 初始化食物的位置
    foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        while game_close == True:
            game_display.fill(black)
            message("你输了，按 Q 退出或按 C 重新开始", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()


        # 移动蛇头
        x1 += x1_change
        y1 += y1_change

        # 检查是否吃到了食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
            Length_of_snake += 1

        # 更新蛇的位置
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.insert(0, snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[-1]

        # 检查是否撞墙
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # 检查是否撞到自己
        for x in snake_List[1:]:
            if x == snake_Head:
                game_close = True

        # 更新游戏窗口
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block_size, snake_block_size])
        our_snake(snake_block_size, snake_List)
        pygame.display.update()

        # 控制蛇移动速度
        clock.tick(5)

    pygame.quit()
    quit()

game_loop()
           
