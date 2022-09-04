import maincommandslist
from tkinter import *

# луп ввода команд

"""
programm_work = True
while programm_work:
    maincommandslist.input_command()
"""

window = Tk()
window.title("AxiDataBase editor")
window.geometry('400x250')


but = Button(window, text = 'rand int', command=lambda: maincommandslist.rand_int(None))
but.grid(column=1, row=0)

window.mainloop()