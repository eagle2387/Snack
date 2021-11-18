'''貪吃蛇'''

from os import curdir
import random
import sys
import time
import pygame
from pygame.locals import *
from collections import deque

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
SIZE = 20 

def print_text(screen, font, x, y, text, fcolor = (255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("貪吃蛇")

    light = (100, 100, 100) #蛇的顏色
    dark = (200, 200, 200) #食物顏色
    
    font1 = pygame.font.SysFont("SimHei", 24) #得分的字體
    font2 = pygame.font.Font(None, 72)        #game ove 的字體
    red = (200, 30, 30)                       #game over 字體顏色 
    fwidth, fheight = font2.size("Game Over")
    line_width = 1                            #網格線寬度
    black = (0, 0, 0)                         #網格線顏色
    bgcolor = (40, 40, 40)                    #背景色
    
    #方向起始向右
    pos_x = 1
    pos_y = 0
    # 如果蛇向右移動 那麼快速點擊向下向左 由於程式刷新沒有那麼快 向下事件會被覆蓋掉 導致蛇後退 直接Game Over
    # b向量就是防止這種情況發生
    b = True
    # 範圍
    scope_x = (0, SCREEN_WIDTH // SIZE - 1)
    scope_y = (2, SCREEN_HEIGHT // SIZE - 1)
    # 蛇
    snake = deque()
    #食物
    food_x = 0
    food_y = 0

    # 初始化蛇
    def _init_snake():
        nonlocal snake
        snake.clear()
        snake.append((2, scope_y[0]))
        snake.append((1, scope_y[0]))
        snake.append((0, scope_y[0]))

    # 食物
    def _create_food():
        nonlocal food_x, food_y
        food_x = random.randint(scope_x[0], scope_x[1])
        food_y = random.randint(scope_y[0], scope_y[1])
        while (food_x, food_y) in snake:
            #防止食物出現蛇身上
            food_x = random.randint(scope_x[0], scope_x[1])
            food_y = random.randint(scope_y[0], scope_y[1])

    _init_snake()
    _create_food()

    game_over = True
    start = False     # 是否開始 當start = True, game_over = True時,完顯示 GAME OVER
    score = 0         # 得分
    orispeed = 0.1    # 原始速度
    speed = orispeed
    last_move_time = None
    pause = False     # 暫停

    #設定鍵盤事件
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if game_over:
                        start = True
                        game_over = False
                        b = True
                        _init_snake()
                        _create_food()
                        pos_x = 1
                        pos_y = 0
                        # 得分
                        score = 0
                        last_move_time = time.time()
                elif event.key == K_SPACE:
                    if not game_over:
                        pause = not pause
                elif event.key in (K_w, K_UP):
                    # 防止蛇向上移動時按了向下鍵 導致Game Over
                    if b and not pos_y:
                        pos_x = 0
                        pos_y = -1
                        b = False
                elif event.key in (K_s, K_DOWN):
                    if b and not pos_y:
                        pos_x = 0
                        pos_y = 1
                        b = False
                elif event.key in (K_s, K_LEFT):
                    if b and not pos_x:
                        pos_x = -1
                        pos_y = 0
                        b = False
                elif event.key in (K_s, K_RIGHT):
                    if b and not pos_x:
                        pos_x = 1
                        pos_y = 0
                        b = False
        
        #填充背景
        screen.fill(bgcolor)
        #畫網格 豎線
        for x in range(SIZE, SCREEN_WIDTH, SIZE):
            pygame.draw.line(screen, black, (x, scope_y[0] * SIZE), (x, SCREEN_HEIGHT), line_width)
        #畫網格 橫線
        for y in range(scope_y[0] * SIZE, SCREEN_HEIGHT, SIZE):
            pygame.draw.line(screen, black, (0, y), (SCREEN_WIDTH, y), line_width)

        if game_over:
            if start:
                print_text(screen, font2, (SCREEN_WIDTH - fwidth) // 2, (SCREEN_HEIGHT - fheight) // 2, "GAME OVER", red)
        else:
            curTime = time.time()
            if curTime - last_move_time > speed:
                if not pause:
                    b = True
                    last_move_time = curTime
                    next_s = (snake[0][0] + pos_x, snake[0][1] + pos_y)
                    if next_s[0] == food_x and next_s[1] == food_y:
                        #吃到了食物
                        _create_food()
                        snake.appendleft(next_s)
                        score += 10
                        speed = orispeed - 0.03 * (score // 100)
                    else:
                        if scope_x[0] <= next_s[0] <= scope_x[1] and scope_y[0] <= next_s[1] <= scope_y[1] and next_s not in snake:
                            snake.appendleft(next_s)
                            snake.pop()
                        else:
                            game_over = True
        #畫食物
        if not game_over:
            #避免 GG 的時候把 Game Over 給遮住
            pygame.draw.rect(screen, light, (food_x * SIZE, food_y * SIZE, SIZE, SIZE), 0)
        #畫蛇
        for s in snake:
            pygame.draw.rect(screen, dark, (s[0]* SIZE + line_width, s[1]* SIZE + line_width,
                                            SIZE - line_width * 2, SIZE - line_width * 2), 0)

        print_text(screen, font1, 30, 7, f"速度: {score //100}")
        print_text(screen, font1 , 450, 7, f"得分: {score}")
        
        pygame.display.update()

if __name__ == "__main__":
    main()
        

                        
                    
                    

                
