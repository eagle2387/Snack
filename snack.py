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
    
    