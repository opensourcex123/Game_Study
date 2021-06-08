# 作者：宁方笑
# 开发时间：2021/6/8 9:31
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygames事件产生')
fps = 1
fclock = pygame.time.Clock()
num = 1

while True:
    uevent = pygame.event.Event(pygame.KEYDOWN, {'unicode': 123, 'key': pygame.K_SPACE, 'mod': pygame.KMOD_ALT})
    pygame.event.post(uevent)
    num = num + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == '':
                print('[KEYDOWN,{}]:'.format(num), '#', event.key, event.mod)
            else:
                print('[KEYDOWN,{}]:'.format(num), event.unicode, event.key, event.mod)
        pygame.display.update()
        fclock.tick(fps)
