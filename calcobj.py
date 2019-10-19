from tkinter import *


class Knopka(Frame):

    def rec(self, sym):
        global rez
        rez += sym
        scr.insert(END, sym)
        if sym == '=':
            scr.insert(END, eval(rez[:-1]))
            rez = ''
        if sym == 'C':
            scr.delete(0, END)
            rez = ''

    def __init__(self, parent=None, sym='#'):
        self.sym = sym
        Frame.__init__(self, parent)
        but = Button(self, text=self.sym, width=8,
                     command=lambda: self.rec(self.sym))
        but.grid()


if __name__ == '__main__':
    global rez
    rez = ''
    root = Tk()
    root.title("Calculator")
    root.geometry("264x130")
    root.resizable(width=False, height=False)
    scr = Entry(root, width=24, font="arial 11")
    scr.grid(row=0, column=0, columnspan=3)
    Knopka(root, sym='C').grid(row=0, column=3)
    Knopka(root, sym='1').grid(row=1, column=0)
    Knopka(root, sym='2').grid(row=1, column=1)
    Knopka(root, sym='3').grid(row=1, column=2)
    Knopka(root, sym='+').grid(row=1, column=3)
    Knopka(root, sym='4').grid(row=2, column=0)
    Knopka(root, sym='5').grid(row=2, column=1)
    Knopka(root, sym='6').grid(row=2, column=2)
    Knopka(root, sym='-').grid(row=2, column=3)
    Knopka(root, sym='7').grid(row=3, column=0)
    Knopka(root, sym='8').grid(row=3, column=1)
    Knopka(root, sym='9').grid(row=3, column=2)
    Knopka(root, sym='*').grid(row=3, column=3)
    Knopka(root, sym='.').grid(row=4, column=0)
    Knopka(root, sym='0').grid(row=4, column=1)
    Knopka(root, sym='=').grid(row=4, column=2)
    Knopka(root, sym='/').grid(row=4, column=3)
    root.mainloop()
