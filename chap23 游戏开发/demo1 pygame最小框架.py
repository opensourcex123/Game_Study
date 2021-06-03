# 作者：宁方笑
# 开发时间：2021/6/3 21:20
import pygame,sys

pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('Pygame游戏之旅')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()