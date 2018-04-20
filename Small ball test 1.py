from tkinter import *
import random
import time
#
#创建一个类，这个类含有两个参数，一个是画布，一个是球的颜色
#
class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        #来回反弹
        self.x = 0
        self.y = -1
        #winfo_height()函数来获取画布当前的高度，赋值给对象变量
        self.canvas_height = self.canvas.winfo_height()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        #获取某个对象在画布的坐标，返回一个数组（两个坐标，左上角的坐标和右下角的两个坐标）
        pos = self.canvas.coords(self.id)
        #打印获取的坐标
        print(pos)
        #如果最上面的纵轴坐标在顶上，则往下移动一个像素
        if pos[1] <= 0:
            self.y = 1
        #如果最下面的纵轴坐标在底上，则向上移动
        if pos[3] > self.canvas_height:
            self.y = -1


#创建画布
tk = Tk()
tk.title("Game_ball")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
#bd=0,highlightthickness=0 画布之外没有边框
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

#创建对象
ball = Ball(canvas,'red')

#一直保持循环
while 1:
    ball.draw()
    #快速刷新屏幕
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)