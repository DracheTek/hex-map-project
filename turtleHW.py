import turtle

turtletop = turtle.getscreen()  #turtle的主要部件称为“窗口”，绘图指针是黑色三角形，成为“乌龟”（turtle）
t = turtle.getturtle() #这个命令可以“抓住”乌龟（将活动的乌龟获取为对象）
# 乌龟会向特定方向移动.默认方向是正东。可以指定其状态是UP（不绘线）或DOWN（绘线）
t.right(120)
for i in range(1000):
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.right(60)

