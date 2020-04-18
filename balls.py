import tkinter as tk
from random import randint

WIDTH = 300
HEIGHT = 200
TICK_RATE = 50

dx, dy = 1, 1
class Ball:
    def __init__(self, x, y, R, color, speeed):
        global ball_id, dx,dy
        self.x = x
        self.y = y
        self.R = R
        self.color = color
        self.speed = speeed
        ball_id =\
            canvas.create_oval(x - R, y - R, x + R, y + R, fill=self.color)
        dx, dy = speeed, speeed

    def move(self, dx, dy):
        canvas.move(ball_id, dx, dy)

    def collision_handler(self):
        global x, y, R, dx, dy
        x += dx
        y += dy
        if x + R > WIDTH or x - R < 0:
            dx = -dx
        if y + R > HEIGHT or y - R < 0:
            dy = -dy

def tick():
    global dx, dy
    """ Обработчик времени
    """
    ball_1.collision_handler()
    ball_1.move(dx, dy)
    root.after(TICK_RATE, tick)


def main():
    global root, canvas
    global ball_1, x, y, R
    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack()

    R = randint(20, 50)
    x = randint(R, WIDTH - R)
    y = randint(R, HEIGHT - R)
    ball_1 = Ball(x, y, R, '#ff3333', 5)

    tick()
    root.mainloop()

if __name__ == '__main__':
    main()
