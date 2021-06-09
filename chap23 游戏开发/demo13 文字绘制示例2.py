# 作者：宁方笑
# 开发时间：2021/6/9 21:16
import pygame,sys
import pygame.freetype

pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('Pygame文字绘制')
GOLD=255,251,0

f1=pygame.freetype.Font('C://Windows//Fonts//msyh.ttc',36)  #获得一个font类
f1surf,f1rect=f1.render('WDNMD',fgcolor=GOLD,size=60)   #获得两个返回值

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.blit(f1surf,(300,200))
        pygame.display.update()