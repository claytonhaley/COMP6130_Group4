try:
    import tkinter as t
    from tkinter import *
except ImportError:
    import Tkinter as t
    from Tkinter import *

class Window:
    def __init__(self, master):

        canvas = Canvas(master, height=450, width=450, bg="white")
        canvas.pack()

        frame1 = Frame(master)
        frame1.pack()
        MainWindow = canvas.create_window(450,450,window=frame1)

        e1 = Entry(frame1)
        e1.pack()


root = Tk()
root.resizable(0,0)
root.geometry("450x450")
root.title("Test")
root.configure(background="#212F3C")
window = Window(root)
root.mainloop()