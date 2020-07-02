from tkinter import *

window = Tk()
window.geometry("250x400+300+300")
# disabling the window resizing so that the calculator looks good
window.resizable(0, 0)
window.title("Calculator")
# using frame to simplify the huge frame and working in small parts
btn_row1 = Frame(window)
btn_row1.pack(expand=TRUE, fill="both")

btn_row2 = Frame(window)
btn_row2.pack(expand=TRUE, fill="both")

btn_row3 = Frame(window)
btn_row3.pack(expand=TRUE, fill="both")

btn_row4 = Frame(window)
btn_row4.pack(expand=TRUE, fill="both")














window.mainloop()
