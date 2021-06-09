# 作者：宁方笑
# 开发时间：2021/6/9 21:12
import pygame,sys
import pygame.freetype

pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('Pygame文字绘制')
GOLD=255,251,0

f1=pygame.freetype.Font('C://Windows//Fonts//msyh.ttc',36)  #获得一个font类
f1rect=f1.render_to(screen,(200,160),'WDNMD',fgcolor=GOLD,size=50)  #获得一个返回值

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()