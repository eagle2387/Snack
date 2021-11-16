import random
from typing import Tuple
import pygame
import copy

#蛇的模型
snack_list = [[10, 10]]


#背景大小 500*500

#食物模型(隨機生成)
x = random.randint(10, 490)
y = random.randint(10, 490)
food_point = [x, y]

#初始蛇方向
move_up = False
move_down = False
move_left = False
move_right = False

#初始化遊戲
pygame.init()
#畫布
screen = pygame.display.set_mode((500, 500))
#名稱
title = pygame.display.set_caption("貪吃蛇")

clock = pygame.time.Clock()

while True:
    #遊戲循環
    #遊戲禎數
    clock.tick(30)
    #背景為白色
    screen.fill([255, 255, 255])
    #繪製圓點
    food_rect = pygame.draw.circle(screen, [255, 0, 0], food_point, 15)
    '''蛇蛇移動 鍵盤事件'''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_up = False
                move_down = True
                move_left = False
                move_right = False
            if event.key == pygame.K_UP:
                move_up = True
                move_down = False
                move_left = False
                move_right = False
            if event.key == pygame.K_LEFT:
                move_up = False
                move_down = False
                move_left = True
                move_right = False
            if event.key == pygame.K_RIGHT:
                move_up = False
                move_down = False
                move_left = False
                move_right = True

    #身體移動
    snack_len = len(snack_list) - 1
    while snack_len > 0:
        snack_list[snack_len] = copy.deepcopy(snack_list[snack_len - 1])
        snack_len -= 1
    #更改蛇頭位置 
    if move_up:
        snack_list[snack_len][1] -= 10
        if snack_list[snack_len][1] < 0:
            snack_list[snack_len][1] = 500
    if move_down:
        snack_list[snack_len][1] += 10
        if snack_list[snack_len][1] > 500:
            snack_list[snack_len][1] = 0
    if move_left:
        snack_list[snack_len][0] -= 10
        if snack_list[snack_len][0] < 0:
            snack_list[snack_len][0] = 500
    if move_right:
        snack_list[snack_len][0] += 10
        if snack_list[snack_len][0] > 500:
            snack_list[snack_len][0] = 0 
    #繪製蛇
    snack_rect = []
    for snack_pos in snack_list:
        snack_rect.append(pygame.draw.circle(screen, [255, 0, 0], snack_pos, 5))
        #蛇吃食物 碰撞檢測方法
        if food_rect.collidepoint(snack_pos):
            snack_list.append(food_point)
            #重新生成食物
            food_point = [random.randint(10, 490), random.randint(10, 490)]
            break
    
    #定義Game over
    snack_head_rect = snack_rect[0]
    count = len(snack_rect)
    while count > 1:
        #與身體碰撞
        if snack_head_rect.colliderect(snack_rect[count - 1]):
            print("Game Over")
            pygame.quit()
        count -= 1
    
    
    pygame.display.update()
