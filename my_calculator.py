from tkinter import *

window = Tk()
window.geometry("250x400+300+300")
# disabling the window resizing so that the calculator looks good
window.resizable(0, 0)
window.title("Calculator")


label_ = Label(
    window,
    text="Label",
    anchor=SE,
    font =("Verdana", 20)
)
label_.pack(expand= True, fill="both")


# using frame to simplify the huge frame and working in small parts
btn_row1 = Frame(window)
btn_row1.pack(expand=True, fill="both")

btn_row2 = Frame(window)
btn_row2.pack(expand=True, fill="both")

btn_row3 = Frame(window)
btn_row3.pack(expand=True, fill="both")

btn_row4 = Frame(window)
btn_row4.pack(expand=True, fill="both")

"----------------------------------------------------------------"

btn7_ = Button(
    btn_row1,
    text="7",
    font=("Verdana",22),
)
btn7_.pack(side=LEFT, expand=True, fill="both")
btn8_ = Button(
    btn_row1,
    text="8",
    font=("Verdana",22),
)
btn8_.pack(side=LEFT, expand=True, fill="both")
btn9_ = Button(
    btn_row1,
    text="9",
    font=("Verdana",22),
)
btn9_.pack(side=LEFT, expand=True, fill="both")
btn_div_ = Button(
    btn_row1,
    text="/",
    font=("Verdana",22),
)
btn_div_.pack(side=LEFT, expand=True, fill="both")

"---------------------------------------------------------------------------------------------------"

btn4_ = Button(
    btn_row2,
    text="4",
    font=("Verdana",22),
)
btn4_.pack(side=LEFT, expand=True, fill="both")
btn5_ = Button(
    btn_row2,
    text="5",
    font=("Verdana",22),
)
btn5_.pack(side=LEFT, expand=True, fill="both")
btn6_ = Button(
    btn_row2,
    text="6",
    font=("Verdana",22),
)
btn6_.pack(side=LEFT, expand=True, fill="both")
btn_mul_ = Button(
    btn_row2,
    text="*",
    font=("Verdana",19),
)
btn_mul_.pack(side=LEFT, expand=True, fill="both")

"--------------------------------------------------------------------------------"

btn1_ = Button(
    btn_row3,
    text="1",
    font=("Verdana",22),
)
btn1_.pack(side=LEFT, expand=True, fill="both")
btn2_ = Button(
    btn_row3,
    text="2",
    font=("Verdana",22),
)
btn2_.pack(side=LEFT, expand=True, fill="both")
btn3_ = Button(
    btn_row3,
    text="3",
    font=("Verdana",22),
)
btn3_.pack(side=LEFT, expand=True, fill="both")
btn_min_ = Button(
    btn_row3,
    text="-",
    font=("Verdana",22),
)
btn_min_.pack(side=LEFT, expand=True, fill="both")

"------------------------------------------------------------"

btn_clear_ = Button(
    btn_row4,
    text="C",
    font=("Verdana",23),
    width=2
)
btn_clear_.pack(side=LEFT, expand=True, fill="both")
btn0_ = Button(
    btn_row4,
    text="0",
    font=("Verdana",23),
)
btn0_.pack(side=LEFT, expand=True, fill="both")
btn_equal_ = Button(
    btn_row4,
    text="=",
    font=("Verdana",20),
)
btn_equal_.pack(side=LEFT, expand=True, fill="both")
btn_plus = Button(
    btn_row4,
    text="+",
    font=("Verdana",18),

)
btn_plus.pack(side=LEFT, expand=True, fill="both")













window.mainloop()
