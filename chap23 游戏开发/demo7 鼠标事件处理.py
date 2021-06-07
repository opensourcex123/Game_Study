# 作者：宁方笑
# 开发时间：2021/6/7 21:33
import pygame,sys

pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('Pygame事件处理')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            print('[MOUSEMOTION]:',event.pos,event.rel,event.buttons)   #绝对位置，相对位置，按下哪个键
        elif event.type == pygame.MOUSEBUTTONUP:
            print('[MOUSEUP]:',event.pos,event.button)  #绝对位置，按下哪个键
        elif event.type == pygame.MOUSEBUTTONUP:
            print('[MOUSEDOWN]:', event.pos, event.button)
        pygame.display.update()