""" This program implements an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white. """

import tkinter as tk

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CELL_SIZE = 50
ERASER_SIZE = 30

class EraserCanvas:
    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        
        self.cells = []
        for row in range(CANVAS_HEIGHT // CELL_SIZE):
            for col in range(CANVAS_WIDTH // CELL_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue')
                self.cells.append(cell)
        
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')
        self.canvas.bind('<Motion>', self.move_eraser)
        self.canvas.bind('<B1-Motion>', self.erase)

    def move_eraser(self, event):
        self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)

    def erase(self, event):
        x1, y1, x2, y2 = event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE
        overlapping = self.canvas.find_overlapping(x1, y1, x2, y2)
        for obj in overlapping:
            if obj != self.eraser:
                self.canvas.itemconfig(obj, fill='white')

def main():
    root = tk.Tk()
    app = EraserCanvas(root)
    root.mainloop()

if __name__ == '__main__':
    main()