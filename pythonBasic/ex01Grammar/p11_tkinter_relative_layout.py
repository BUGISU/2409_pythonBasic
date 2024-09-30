import tkinter
from tkinter import *
from typing import override

window = Tk()
window.title("MyWindow")
window.geometry('400x400+300+300')
window.config(bg="skyblue")
window.resizable(1, True)

btnConfirm = Button(window, text="Confirm",
              overrelief="groove", anchor="n")
btnConfirm.pack(padx=10, pady=20, side="top")
# pack 상대 위치, top, bottom, left, right, side 없으면 center

btnCancel = Button(window, text="Cancel",
              overrelief="groove", anchor="n")
btnCancel.pack(padx=10, pady=20)
# pack 상대 위치, top, bottom, left, right, side 없으면 center

window.mainloop()
