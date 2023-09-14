from tkinter import *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()

# canvas.create_rectangle(100, 100,
#                         120, 120,
#                         fill='yellow',
#                         outline='')
# canvas.create_rectangle(130, 130,
#                         170, 170,
#                         fill='gold',
#                         outline='')
# canvas.create_rectangle(180, 180,
#                         240, 240,
#                         fill='blue',
#                         outline='')

# canvas.create_polygon(50, 200,
#                       100, 100,
#                       150, 200,
#                       fill='gold')

# canvas.create_polygon(300, 100, 200, 200, 400, 200, fill='gold')
# canvas.create_rectangle(250, 200, 350, 350, fill='red', outline='')
#
# canvas.create_polygon(100, 100, 50, 200, 150, 200, fill='pink')
# canvas.create_rectangle(60, 200, 140, 280, fill='brown')


class House:
    def __init__(self, roof_color, wall_color):
        self.roof_color = roof_color
        self.wall_color = wall_color
        self.height = 200
        self.width = 100
        self.roof = None
        self.wall = None

    def build_house(self, x, y):
        h = self.height
        w = self.width

        self.roof = canvas.create_polygon(x, y,
                                          x - w/2, y + 70,
                                          x + w/2, y + 70,
                                          fill=self.roof_color)

        self.wall = canvas.create_rectangle(x - w/2 + 10, y + 70,
                                            x + w/2 - 10, y + h,
                                            fill=self.wall_color)


house_1 = House('pink', 'grey')
house_1.build_house(150, 10)

house_2 = House('gold', 'green')
house_2.build_house(350, 10)



window.mainloop()
