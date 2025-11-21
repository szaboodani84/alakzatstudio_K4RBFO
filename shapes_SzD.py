import math
import random

class ShapeSzD:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

def draw_shape_SzD(canvas, shape):
    t = random.choice(["rect", "oval", "poly"])
    if t == "rect":
        canvas.create_rectangle(
            shape.x, shape.y,
            shape.x + shape.size, shape.y + shape.size,
            fill="#66b3ff", outline=""
        )
    elif t == "oval":
        canvas.create_oval(
            shape.x - shape.size / 2, shape.y - shape.size / 2,
            shape.x + shape.size / 2, shape.y + shape.size / 2,
            fill="#7fd38a", outline=""
        )
    else:
        r = shape.size / 2
        n = 5
        pts = []
        for i in range(n * 2):
            ang = i * math.pi / n
            rad = r if i % 2 == 0 else r * 0.5
            px = shape.x + rad * math.cos(ang)
            py = shape.y + rad * math.sin(ang)
            pts.extend([px, py])
        canvas.create_polygon(pts, fill="#ffcc66", outline="")