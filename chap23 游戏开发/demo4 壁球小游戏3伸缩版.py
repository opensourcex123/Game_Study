# 作者：宁方笑
# 开发时间：2021/6/6 21:13
import pygame,sys

pygame.init()
size=width,height=600,400
speed=[1,1]
BLACK=0,0,0
screen=pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption('老必登球')
ball=pygame.image.load('PYG02-ball.gif')
ballrect=ball.get_rect()
fps=300 #设置小球的运动速度，实际设置循环的频率
fclock=pygame.time.Clock()

while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0]=speed[0] if speed[0]==0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0]=speed[0]+1 if speed[0]>=0 else speed[0]-1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] >= 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1]=speed[1] if speed[1]==0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))
        elif event.type==pygame.VIDEORESIZE:    #响应事件，并更改大小
            size=width,height=event.size[0],event.size[1]
            pygame.display.set_mode(size,pygame.RESIZABLE)
   ballrect=ballrect.move(speed[0],speed[1])
   if ballrect.left<0 or ballrect.right>width:
       speed[0]=-speed[0]
   if ballrect.top<0 or ballrect.bottom>height:
       speed[1]=-speed[1]
   screen.fill(BLACK)
   screen.blit(ball,ballrect)
   pygame.display.update()
   fclock.tick(fps) #控制帧的刷新速度