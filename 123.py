from tkinter import *

def change_color(color1, color2, color3, delay, next_function):
    h.itemconfig(r, fill=color1)
    h.itemconfig(y, fill=color2)
    h.itemconfig(g, fill=color3)
    root.after(delay, next_function)

def svet1():
    change_color('red', '#1c1c08', '#081c0a', 5000, svet6)

def svet6():
    change_color('red', 'yellow', '#081c0a', 3000, svet7)

def svet7():
    change_color('#1c0808', '#1c1c08', 'green', 5000, svet8)

def svet8():
    change_color('#1c0808', '#1c1c08', '#081c0a', 500, svets)

def svets():
    change_color('#1c0808', '#1c1c08', 'green', 500, svetf)

def svetf():
    change_color('#1c0808', '#1c1c08', '#081c0a', 500, svetg)

def svetg():
    change_color('#1c0808', '#1c1c08', 'green', 500, sveth)

def sveth():
    change_color('#1c0808', '#1c1c08', '#081c0a', 500, svetk)

def svetk():
    change_color('#1c0808', '#1c1c08', 'green', 500, svetj)

def svetj():
    change_color('#1c0808', 'yellow', '#081c0a', 3000, svet1)

root = Tk()

h = Canvas(width=500, height=350)
h.pack()

h.create_rectangle(190, 0, 310, 320, fill='black', outline='blue', width=3, dash=(5, 5))

r = h.create_oval(215, 35, 285, 105, fill='red', outline='blue', width=3, dash=(5, 5))
y = h.create_oval(215, 135, 285, 205, fill="yellow", outline='blue', width=3, dash=(5, 5))
g = h.create_oval(215, 235, 285, 305, fill='green', outline='blue', width=2, dash=(5, 5))

root.after(0, svet1)

root.mainloop()
