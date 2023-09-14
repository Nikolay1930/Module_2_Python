from tkinter import *
from time import sleep
from random import choice


class Ball:
    def __init__(self, canvas, color, platform):
        self.canvas = canvas
        self.platform = platform
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.x = choice([-3, -2, -1, 1, 2, 3])
        self.y = -1
        self.touch_bottom = False

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        coords = self.canvas.coords(self.oval)
        if coords[0] <= 0:
            self.x = abs(self.x)
        if coords[1] <= 0:
            self.y = abs(self.y)
        if coords[2] >= 500:
            self.x = -self.x
        if coords[3] >= 400:
            self.touch_bottom = True
        if self.touch_platform(coords):
            self.y = -3


    def touch_platform(self, ball_coords):
        platform_coords = self.canvas.coords(self.platform.rect)
        if ball_coords[2] >= platform_coords[0] and ball_coords[0] <= platform_coords[2]:
            if platform_coords[1] <= ball_coords[3] <= platform_coords[3]:
                return True
        return False


class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        coords = self.canvas.coords(self.rect)
        if coords[0] <= 0:
            self.x = 0
        if coords[2] >= 500:
            self.x = 0


window = Tk()
window.title('Ping-Pong')
window.resizable(0, 0)
window.wm_attributes('-topmost', 1)
canvas = Canvas(window, width=500, height=400)
canvas.pack()


platform = Platform(canvas, 'green')
ball = Ball(canvas, 'red', platform)
while True:
    if not ball.touch_bottom:
        ball.draw()
        platform.draw()
    else:
        break
    window.update()
    sleep(0.01)
