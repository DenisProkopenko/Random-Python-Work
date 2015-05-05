# This is just a fun game, try clicking the button and see what happens :)

from tkinter import *
from random import *

def do_event(event):
    print("{},{}".format(event.x,event.y))

def jump(event):
    app.button.place(relx=random(),rely=random())

class App:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("400x400")
        master.title("Press ME!")
        master.bind("<Button-1>",do_event)
        master.bind("<Button-1>",do_event)
        frame.pack()

        self.button = Button(master,text="Quit",command=sys.exit)
        self.button.configure(bg="green")
        self.button.bind("<Enter>",jump)
        self.button.pack()

root = Tk()
app = App(root)
root.mainloop()
