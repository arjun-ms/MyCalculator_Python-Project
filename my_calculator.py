from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry("320x500+600+100")

##################################### Binding Functions ##########################################
def entered_clear(event):
    btn_clear_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_clear(event):
    btn_clear_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_del(event):
        btn_del_.config(
            bg="#323232",
            fg="#ff7b00"
        )

def left_del(event):
        btn_del_.config(
            bg="#3b3b3b",
            fg="orange",
        )

def entered_oneby(event):
    btn_one_by_.config(
    bg="#323232",
    fg="#ff7b00"
    )
def left_oneby(event):
    btn_one_by_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_div(event):
    btn_div_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_div(event):
    btn_div_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_7(event):
    btn7_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_7(event):
    btn7_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_8(event):
    btn8_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_8(event):
    btn8_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_9(event):
    btn9_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_9(event):
    btn9_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_mul(event):
    btn_mul_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_mul(event):
    btn_mul_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_4(event):
    btn4_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_4(event):
    btn4_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_5(event):
    btn5_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_5(event):
    btn5_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_6(event):
    btn6_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_6(event):
    btn6_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_min(event):
    btn_min_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_min(event):
    btn_min_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_1(event):
    btn1_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_1(event):
    btn1_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_2(event):
    btn2_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_2(event):
    btn2_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_3(event):
    btn3_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_3(event):
    btn3_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_plus(event):
    btn_plus_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_plus(event):
    btn_plus_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_percent(event):
    btn_percent_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_percent(event):
    btn_percent_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_0(event):
    btn0_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_0(event):
    btn0_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_dot(event):
    btn_dot_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_dot(event):
    btn_dot_.config(
        bg="#3b3b3b",
        fg="orange",
    )

def entered_equal(event):
    btn_equal_.config(
        bg="#323232",
        fg="#ff7b00"
    )
def left_euqal(event):
    btn_equal_.config(
        bg="#3b3b3b",
        fg="orange",
    )


# disabling the window resizing so that the calculator looks clean.
window.resizable(0, 0)
window.title("Calculator")
window.iconbitmap("C:\\Users\\Arjun\\Desktop\\My Calculator\\essentials\\icon.ico")

label_ = Label(
    window,
    text="Label",
    anchor=SE,
    font=("Verdana", 20)
)
label_.pack(expand=True, fill="both")

# using frame to simplify the huge frame and working in small parts
btn_row1 = Frame(window)
btn_row1.pack(expand=True, fill="both")

btn_row2 = Frame(window)
btn_row2.pack(expand=True, fill="both")

btn_row3 = Frame(window)
btn_row3.pack(expand=True, fill="both")

btn_row4 = Frame(window)
btn_row4.pack(expand=True, fill="both")

btn_row5 = Frame(window)
btn_row5.pack(expand=True, fill="both")
"-----------------------------------------------------------------------------"
btn_clear_ = Button(
    btn_row1,
    text="C",
    font=("Verdana", 20),
    width=2,
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_clear_.pack(side=LEFT, expand=True, fill="both")
btn_clear_.bind("<Enter>",entered_clear)
btn_clear_.bind("<Leave>",left_clear)

btn_del_ = Button(
    btn_row1,
    text="⌫",
    font=("Verdana", 20),
    relief=GROOVE,
    border=0,
    width=2,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_del_.pack(side=LEFT, expand=True, fill="both")
btn_del_.bind("<Enter>",entered_del)
btn_del_.bind("<Leave>",left_del)

btn_one_by_ = Button(
    btn_row1,
    text="1/x",
    font=("Verdana", 20),
    relief=GROOVE,
    border=0,
    width=2,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_one_by_.pack(side=LEFT, expand=True, fill="both")
btn_one_by_.bind("<Enter>",entered_oneby)
btn_one_by_.bind("<Leave>",left_oneby)

btn_div_ = Button(
    btn_row1,
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_div_.pack(side=LEFT, expand=True, fill="both")
btn_div_.bind("<Enter>",entered_div)
btn_div_.bind("<Leave>",left_div)
"----------------------------------------------------------------"

btn7_ = Button(
    btn_row2,
    text="7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn7_.pack(side=LEFT, expand=True, fill="both")
btn7_.bind("<Enter>",entered_7)
btn7_.bind("<Leave>",left_7)

btn8_ = Button(
    btn_row2,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn8_.pack(side=LEFT, expand=True, fill="both")
btn8_.bind("<Enter>",entered_8)
btn8_.bind("<Leave>",left_8)

btn9_ = Button(
    btn_row2,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn9_.pack(side=LEFT, expand=True, fill="both")
btn9_.bind("<Enter>",entered_9)
btn9_.bind("<Leave>",left_9)

btn_mul_ = Button(
    btn_row2,
    text="*",
    font=("Verdana", 19),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_mul_.pack(side=LEFT, expand=True, fill="both")
btn_mul_.bind("<Enter>",entered_mul)
btn_mul_.bind("<Leave>",left_mul)
"---------------------------------------------------------------------------------------------------"

btn4_ = Button(
    btn_row3,
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn4_.pack(side=LEFT, expand=True, fill="both")
btn4_.bind("<Enter>",entered_4)
btn4_.bind("<Leave>",left_4)

btn5_ = Button(
    btn_row3,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn5_.pack(side=LEFT, expand=True, fill="both")
btn5_.bind("<Enter>",entered_5)
btn5_.bind("<Leave>",left_5)

btn6_ = Button(
    btn_row3,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn6_.pack(side=LEFT, expand=True, fill="both")
btn6_.bind("<Enter>",entered_6)
btn6_.bind("<Leave>",left_6)

btn_min_ = Button(
    btn_row3,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_min_.pack(side=LEFT, expand=True, fill="both")
btn_min_.bind("<Enter>",entered_min)
btn_min_.bind("<Leave>",left_min)
"--------------------------------------------------------------------------------"

btn1_ = Button(
    btn_row4,
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn1_.pack(side=LEFT, expand=True, fill="both")
btn1_.bind("<Enter>",entered_1)
btn1_.bind("<Leave>",left_1)
btn2_ = Button(
    btn_row4,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn2_.pack(side=LEFT, expand=True, fill="both")
btn2_.bind("<Enter>",entered_2)
btn2_.bind("<Leave>",left_2)

btn3_ = Button(
    btn_row4,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn3_.pack(side=LEFT, expand=True, fill="both")
btn3_.bind("<Enter>",entered_3)
btn3_.bind("<Leave>",left_3)

btn_plus_ = Button(
    btn_row4,
    text="+",
    font=("Verdana", 17),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_plus_.pack(side=LEFT, expand=True, fill="both")
btn_plus_.bind("<Enter>",entered_plus)
btn_plus_.bind("<Leave>",left_plus)
"------------------------------------------------------------"

btn_percent_ = Button(
    btn_row5,
    text="%",
    font=("Verdana", 20),
    width=2,
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_percent_.bind("<Enter>",entered_percent)
btn_percent_.bind("<Leave>",left_percent)
btn_percent_.pack(side=LEFT, expand=True, fill="both")
btn0_ = Button(
    btn_row5,
    text="0",
    font=("Verdana", 21),
    width=2,
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn0_.pack(side=LEFT, expand=True, fill="both")
btn0_.bind("<Enter>",entered_0)
btn0_.bind("<Leave>",left_0)

btn_dot_ = Button(
    btn_row5,
    text=".",
    font=("Verdana", 22),
    width=2,
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
)
btn_dot_.pack(side=LEFT, expand=True, fill="both")
btn_dot_.bind("<Enter>",entered_dot)
btn_dot_.bind("<Leave>",left_dot)

btn_equal_ = Button(
    btn_row5,
    text="=",
    font=("Verdana", 17),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",

)
btn_equal_.pack(side=LEFT, expand=True, fill="both")
btn_equal_.bind("<Enter>",entered_equal)
btn_equal_.bind("<Leave>",left_euqal)












window.mainloop()
