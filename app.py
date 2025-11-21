import random
import math
from tkinter import Canvas
from shapes_SzD import ShapeSzD, draw_shape_SzD

def run(root):
    canvas = Canvas(root, width=800, height=500, bg="white")
    canvas.pack()

    # Induláskor kiírjuk a szöveget a vászon közepére
    canvas.create_text(400, 30, text="Nyomkodd a bal egérgombot!", font=("Segoe UI", 16), fill="black")

    def on_click(event):
        size = random.randint(25, 100)
        shape = ShapeSzD(event.x, event.y, size)
        draw_shape_SzD(canvas, shape)

    canvas.bind("<Button-1>", on_click)