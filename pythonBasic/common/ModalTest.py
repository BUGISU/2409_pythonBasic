import tkinter as tk
from tkinter.simpledialog import Dialog


class MyDialog(Dialog):
  def __init__(self, parent, **kwargs):
    Dialog.__init__(self, parent, **kwargs)

  def body(self, parent):
    label = tk.Label(self, text='Can hold tkinter widgets such as label, listbox, etc...', wraplength=300,
                     justify='left', anchor='w')
    label.pack()

  def validate(self):
    return False

  def apply(self):
    pass


class Window:
  def __init__(self, parent):
    self.parent = parent
    btn = tk.Button(parent, text='Click Me', command=self.opendialog)
    btn.pack()

  def opendialog(self):
    MyDialog(self.parent)


root = tk.Tk()
Window(root)
root.mainloop()