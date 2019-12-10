import pygame

#游戏初始化
pygame.init()

#创建游戏的窗口480*700
screen = pygame.display.set_mode((480,700))
#绘制背景图像
#1>加载图像数据
bg = pygame.image.load("./images/background.png")
#2>blit绘制图像
screen.blit(bg,(0,0))
#3>update更新屏幕显示
#pygame.display.update()


#绘制英雄的飞机
#1>加载图像数据
hero = pygame.image.load("./images/me1.png")
#2>blit绘制图像
#向左移动修改第一个值150，向上移动修改第二个值300
screen.blit(hero,(150,300))

#3>可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()

#无限循环
#无限循环也叫游戏循环，-->意味着游戏的开始！
i = 0
while True:
    #时钟对象调用tick方法，可以指定循环体内部的代码执行的频率
    clock.tick(60)
    #打印输出i
    print(i)
    #i自增加1
    i += 1
    pass

pygame.quit()
