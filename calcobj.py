from tkinter import *
from tkinter.messagebox import showinfo


class Knopka(Frame):
    def reply(self, sym):
        showinfo(title='popup', message='Button pressed!' + sym)

    def __init__(self, parent=None, sym='#'):
        self.sym = sym
        Frame.__init__(self, parent)
        but = Button(self, text=self.sym, command=lambda: self.reply(self.sym))
        but.pack()


if __name__ == '__main__':
    root = Tk()
    kn = Knopka(root, sym='$')
    kn.sym = '1'
    kn.pack(side=RIGHT)
    root.mainloop()
