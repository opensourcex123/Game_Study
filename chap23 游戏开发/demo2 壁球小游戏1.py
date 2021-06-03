# 作者：宁方笑
# 开发时间：2021/6/3 21:33
import pygame,sys

pygame.init()
size=width,height=2000,2000
speed=[1,1]
BLACK=0,0,0
screen=pygame.display.set_mode(size)
pygame.display.set_caption('老必登球')
ball=pygame.image.load('国际巨星.png')
ballrect=ball.get_rect()

while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
   ballrect=ballrect.move(speed[0],speed[1])
   if ballrect.left<0 or ballrect.right>width:
       speed[0]=-speed[0]
   if ballrect.top<0 or ballrect.bottom>height:
       speed[1]=-speed[1]
   screen.fill(BLACK)
   screen.blit(ball,ballrect)
   pygame.display.update()