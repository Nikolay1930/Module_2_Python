from tkinter import *
from random import randint


class Knight:
    def __init__(self):
        self.x = 70
        self.y = h / 2
        self.v = 0
        self.img = PhotoImage(file='knight.png')

    def up(self, event):
        self.v = -3

    def down(self, event):
        self.v = 3

    def stop(self, event):
        self.v = 0


class Dragon:
    def __init__(self):
        self.x = w - 50
        self.y = randint(100, 500)
        self.v = randint(1, 3)
        self.img = PhotoImage(file='dragon.png')


def game():
    canvas.delete('all')
    canvas.create_image(w/2, h/2, image=bg_img)
    knight.y += knight.v
    canvas.create_image(knight.x, knight.y, image=knight.img)
    dragon_to_kill = -1
    current_dragon = 0

    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.img)

        if (dragon.x - knight.x)**2 + (dragon.y - knight.y)**2 <= 96**2:
            dragon_to_kill = current_dragon
        current_dragon += 1

        if dragon.x <=0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text='Ты проиграл!', font='Verdana 42', fill='red')

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w // 2, h // 2, text='Ты победил!', font='Verdana 42', fill='red')
    else:
        window.after(50, game)


window = Tk()

h = 600
w = 600
window.geometry(f'{w}x{h}')

canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)

bg_img = PhotoImage(file='bg_2.png')

knight = Knight()
dragons = []
for i in range(3):
    dragons.append(Dragon())

game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)


window.mainloop()