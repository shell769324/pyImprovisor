# Render Page

from Tkinter import *

def draw(canvas, width, height):
    canvas.create_rectangle(0,0,150,150, fill="yellow")

def runRenderPage(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

