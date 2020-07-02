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


btn1_ = Button(
    btn_row1,
    text="1",
    font=("Verdana",22),
)
btn1_.pack(side=LEFT, expand=TRUE, fill="both")
btn2_ = Button(
    btn_row1,
    text="2",
    font=("Verdana",22),
)
btn2_.pack(side=LEFT, expand=TRUE, fill="both")
btn3_ = Button(
    btn_row1,
    text="3",
    font=("Verdana",22),
)
btn3_.pack(side=LEFT, expand=TRUE, fill="both")
btn4_ = Button(
    btn_row1,
    text="4",
    font=("Verdana",22),
)
btn4_.pack(side=LEFT, expand=TRUE, fill="both")












window.mainloop()
