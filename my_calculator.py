from tkinter import *

window = Tk()
window.geometry("320x500+600+100")
# disabling the window resizing so that the calculator looks clean.
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

btn_row5 = Frame(window, bg ="red")
btn_row5.pack(expand=True, fill="both")
"-----------------------------------------------------------------------------"
btn_clear_= Button(
    btn_row1,
    text="C",
    font=("Verdana",20),
    width=2,
    relief= GROOVE,
    border=0,
)
btn_clear_.pack(side=LEFT, expand=True, fill="both")
btn_del_ = Button(
    btn_row1,
    text="8",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn_del_.pack(side=LEFT, expand=True, fill="both")
btn_one_by_ = Button(
    btn_row1,
    text="9",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn_one_by_.pack(side=LEFT, expand=True, fill="both")
btn_div_ = Button(
    btn_row1,
    text="/",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn_div_.pack(side=LEFT, expand=True, fill="both")


"----------------------------------------------------------------"

btn7_ = Button(
    btn_row2,
    text="7",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn7_.pack(side=LEFT, expand=True, fill="both")
btn8_ = Button(
    btn_row2,
    text="8",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn8_.pack(side=LEFT, expand=True, fill="both")
btn9_ = Button(
    btn_row2,
    text="9",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn9_.pack(side=LEFT, expand=True, fill="both")
btn_mul_ = Button(
    btn_row2,
    text="*",
    font=("Verdana",19),
    relief= GROOVE,
    border=0,
)
btn_mul_.pack(side=LEFT, expand=True, fill="both")

"---------------------------------------------------------------------------------------------------"

btn4_ = Button(
    btn_row3,
    text="4",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn4_.pack(side=LEFT, expand=True, fill="both")
btn5_ = Button(
    btn_row3,
    text="5",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn5_.pack(side=LEFT, expand=True, fill="both")
btn6_ = Button(
    btn_row3,
    text="6",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn6_.pack(side=LEFT, expand=True, fill="both")
btn_min_ = Button(
    btn_row3,
    text="-",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn_min_.pack(side=LEFT, expand=True, fill="both")


"--------------------------------------------------------------------------------"

btn1_ = Button(
    btn_row4,
    text="1",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn1_.pack(side=LEFT, expand=True, fill="both")
btn2_ = Button(
    btn_row4,
    text="2",
    font=("Verdana",22),
    relief= GROOVE,
    border=0,
)
btn2_.pack(side=LEFT, expand=True, fill="both")
btn3_ = Button(
    btn_row4,
    text="3",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
)
btn3_.pack(side=LEFT, expand=True, fill="both")
btn_plus = Button(
    btn_row4,
    text="+",
    font=("Verdana",17),
    relief=GROOVE,
    border=0,
)
btn_plus.pack(side=LEFT, expand=True, fill="both")


"------------------------------------------------------------"

btn_percent_ = Button(
    btn_row5,
    text="%",
    font=("Verdana",20),
    width=2,
    relief= GROOVE,
    border=0,
)
btn_percent_.pack(side=LEFT, expand=True, fill="both")
btn0_ = Button(
    btn_row5,
    text="0",
    font=("Verdana",21),
    width=2,
    relief= GROOVE,
    border=0,
)
btn0_.pack(side=LEFT, expand=True, fill="both")
btn_dot_ = Button(
    btn_row5,
    text=".",
    font=("Verdana",22),
    width=2,
    relief= GROOVE,
    border=0,

)
btn_dot_.pack(side=LEFT, expand=True, fill="both")
btn_equal_ = Button(
    btn_row5,
    text="=",
    font=("Verdana",17),
    relief= GROOVE,
    border=0,
)
btn_equal_.pack(side=LEFT, expand=True, fill="both")












window.mainloop()
