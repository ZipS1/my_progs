import tkinter as tk
from random import randint

WIDTH = 300
HEIGHT = 200
TICK_RATE = 50 

class Ball:
    def __init__(self, x, y, R, color):
        global ball_id
        self.x = x
        self.y = y
        self.R = R
        self.color = color
        ball_id = canvas.create_oval(x - R, y - R, x + R, y + R, fill = self.color)
    def move(self, dx, dy):
        canvas.move(ball_id, dx, dy)

def canvas_click_handler(event):
    print('x =', event.x, 'y =', event.y)

def tick():
    global x, y
    """ Обработчик времени
    """
    ball_1.move(5, 0)
    root.after(TICK_RATE, tick)

def main():
    global root, canvas
    global x, y, z, ball_1, R
    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack()
    canvas.bind('<Button-1>', canvas_click_handler)

    R = randint(20, 50)
    x = randint(R, WIDTH - R)
    y = randint(R, HEIGHT - R)
    ball_1 = Ball(x, y, R, '#ff3333')

    tick()
    root.mainloop()

if __name__ == '__main__':
    main()