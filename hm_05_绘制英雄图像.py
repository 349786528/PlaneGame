import pygame

pygame.init()

#创建游戏的窗口480*700
screen = pygame.display.set_mode((480,700))
#绘制背景图像
#1>加载图像数据
bg = pygame.image.load("./images/background.png")
#2>blit绘制图像
screen.blit(bg,(0,0))
#3>update更新屏幕显示
pygame.display.update()


#绘制英雄的飞机
#1>加载图像数据
hero = pygame.image.load("./images/me1.png")
#2>blit绘制图像
#向左移动修改第一个值150，向上移动修改第二个值300
screen.blit(hero,(150,300))
#3>update更新屏幕显示
pygame.display.update()


#无线循环
while True:
    pass

pygame.quit()
