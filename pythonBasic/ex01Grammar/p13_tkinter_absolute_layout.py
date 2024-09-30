import tkinter
import tkinter.ttk as ttk
import tkinter.font
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("MyWindow Absolute")
window.geometry('250x120')
# window.config(bg="light gray")
window.resizable(1, True)
font = tkinter.font.Font(family="맑은 고딕", size=12)

def check_login():
  if str(entryId.get()) == "":
    messagebox.showinfo("알림", "ID를 확인하여 주세요")
    entryId.focus()
    return

  if str(entryPass.get()) == "":
    messagebox.showinfo("알림", "Password를 확인하여 주세요")
    entryPass.focus()
    return

#place() 절대 위치에 컴포넌트를 배치 할 수 있다.
lbId = tkinter.Label(window, text="ID", font=font)
lbPass = tkinter.Label(window, text="Pass", font=font)
entryId = tkinter.Entry(window, relief="solid", borderwidth=1, font=font)
entryPass = tkinter.Entry(window, relief="solid", borderwidth=1, font=font, show="*")

lbId.place(x=10, y=8)
entryId.place(x=50, y=10)
lbPass.place(x=10, y=38)
entryPass.place(x=50, y=40)

btnLogin = Button(window, text="Login", width="10",
              overrelief="groove", anchor="n", command=check_login)
btnLogin.place(x=30, y=80)

btnJoin = Button(window, text="Join", width="10",
              overrelief="groove", anchor="n")
btnJoin.place(x=130, y=80)

entryId.focus()
window.mainloop()



