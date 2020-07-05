from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

value_ = ""
old_value_ = 0
operator_ = ""


################################################ Number Buttons Clicked ##################################

def btn1_isclicked():
    global value_
    value_ = value_ + "1"
    data.set(value_)


def btn2_isclicked():
    global value_
    value_ = value_ + "2"
    data.set(value_)


def btn3_isclicked():
    global value_
    value_ = value_ + "3"
    data.set(value_)


def btn4_isclicked():
    global value_
    value_ = value_ + "4"
    data.set(value_)


def btn5_isclicked():
    global value_
    value_ = value_ + "5"
    data.set(value_)


def btn6_isclicked():
    global value_
    value_ = value_ + "6"
    data.set(value_)


def btn7_isclicked():
    global value_
    value_ = value_ + "7"
    data.set(value_)


def btn8_isclicked():
    global value_
    value_ = value_ + "8"
    data.set(value_)


def btn9_isclicked():
    global value_
    value_ = value_ + "9"
    data.set(value_)


def btn0_isclicked():
    global value_
    value_ = value_ + "0"
    data.set(value_)


def btn_dot_isclicked():
    global value_
    value_ = value_ + "."
    data.set(value_)

############################################# Operator Buttons Clicked #############################

def btn_plus_isclicked():
    global old_value_
    global operator_
    global value_
    old_value_ = float(value_)
    operator_ = "+"
    value_ = value_ + "+"
    data.set(value_)

def btn_div_isclicked():
    global old_value_
    global operator_
    global value_
    old_value_ = float(value_)
    operator_ = "÷"
    value_ = value_ + "÷"
    data.set(value_)

def btn_mul_isclicked():
    global old_value_
    global operator_
    global value_
    old_value_ = float(value_)
    operator_ = "x"
    value_ = value_ + "x"
    data.set(value_)

def btn_min_isclicked():
    global old_value_
    global operator_
    global value_
    old_value_ = float(value_)
    operator_ = "-"
    value_ = value_ + "-"
    data.set(value_)
def btn_percent_isclicked():
    global old_value_
    global value_
    value_ = float(value_)/100
    old_value_ = float(value_)
    data.set(value_)
def btn_oneby_isclicked():
    global old_value_
    global value_
    value_ = 1/float(value_)
    old_value_ = float(value_)
    data.set(value_)

################################ Other Buttons Clicked ########################################

def btn_clear_clicked():
    global old_value_
    global value_
    global operator_
    value_ = ""
    old_value_ = 0
    operator_ = ""
    data.set(value_)

def backspace():
    global value_
    value_ = (value_[:-1])
    data.set(value_)


def result():
    global old_value_
    global value_
    global operator_
    full_value_ = value_
    if operator_ == "+":
        second_value_ = float((full_value_.split("+")[1]))
        result_= float(old_value_ + second_value_)
        data.set(result_)
        value_ = str(result_)
    elif operator_ == "-":
        second_value_ = float((full_value_.split("-")[1]))
        result_ = float(old_value_ - second_value_)
        data.set(result_)
        value_ = str(result_)
    elif operator_ == "x":
        second_value_ = float((full_value_.split("x")[1]))
        result_ = float(old_value_ * second_value_)
        data.set(result_)
        value_ = str(result_)
    elif operator_ == "÷":
        second_value_ = float((full_value_.split("÷")[1]))
        if second_value_ == 0:
            messagebox.showerror("Error","Can't divide by zero")
            old_value_ = ""
            value_ = ""
            data.set(value_)
        else:
            result_ = float(old_value_ / second_value_)
            data.set(result_)
            value_ = str(result_)













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
        bg="#ff7b00",
        fg="white"
    )


def left_euqal(event):
    btn_equal_.config(
        bg="#3b3b3b",
        fg="orange",
    )


# disabling the window resizing so that the calculator looks clean.
window = Tk()
window.geometry("320x500+600+100")
window.resizable(0, 0)
window.title("Calculator")
window.iconbitmap("C:\\Users\\Arjun\\Desktop\\My Calculator\\essentials\\icon.ico")

data = StringVar()

label_ = Label(
    window,
    text="Label",
    anchor=SE,
    font=("Verdana", 20),
    textvariable=data,
    bg="#141414",
    fg="white"
)
label_.pack(expand=True, fill="both")

############################################## using frame to simplify the huge frame and working in small parts
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
    command=btn_clear_clicked
)
btn_clear_.pack(side=LEFT, expand=True, fill="both")
btn_clear_.bind("<Enter>", entered_clear)
btn_clear_.bind("<Leave>", left_clear)

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
    command=backspace
)
btn_del_.pack(side=LEFT, expand=True, fill="both")
btn_del_.bind("<Enter>", entered_del)
btn_del_.bind("<Leave>", left_del)

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
    command = btn_oneby_isclicked
)
btn_one_by_.pack(side=LEFT, expand=True, fill="both")
btn_one_by_.bind("<Enter>", entered_oneby)
btn_one_by_.bind("<Leave>", left_oneby)

btn_div_ = Button(
    btn_row1,
    text="÷",
    font=("Verdana", 17),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command = btn_div_isclicked
)
btn_div_.pack(side=LEFT, expand=True, fill="both")
btn_div_.bind("<Enter>", entered_div)
btn_div_.bind("<Leave>", left_div)
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
    command=btn7_isclicked,
)
btn7_.pack(side=LEFT, expand=True, fill="both")
btn7_.bind("<Enter>", entered_7)
btn7_.bind("<Leave>", left_7)

btn8_ = Button(
    btn_row2,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command=btn8_isclicked,
)
btn8_.pack(side=LEFT, expand=True, fill="both")
btn8_.bind("<Enter>", entered_8)
btn8_.bind("<Leave>", left_8)

btn9_ = Button(
    btn_row2,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command=btn9_isclicked,
)
btn9_.pack(side=LEFT, expand=True, fill="both")
btn9_.bind("<Enter>", entered_9)
btn9_.bind("<Leave>", left_9)

btn_mul_ = Button(
    btn_row2,
    text="x",
    font=("Verdana", 19),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command = btn_mul_isclicked

)
btn_mul_.pack(side=LEFT, expand=True, fill="both")
btn_mul_.bind("<Enter>", entered_mul)
btn_mul_.bind("<Leave>", left_mul)
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
    command=btn4_isclicked,
)
btn4_.pack(side=LEFT, expand=True, fill="both")
btn4_.bind("<Enter>", entered_4)
btn4_.bind("<Leave>", left_4)

btn5_ = Button(
    btn_row3,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command=btn5_isclicked,
)
btn5_.pack(side=LEFT, expand=True, fill="both")
btn5_.bind("<Enter>", entered_5)
btn5_.bind("<Leave>", left_5)

btn6_ = Button(
    btn_row3,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command=btn6_isclicked,
)
btn6_.pack(side=LEFT, expand=True, fill="both")
btn6_.bind("<Enter>", entered_6)
btn6_.bind("<Leave>", left_6)

btn_min_ = Button(
    btn_row3,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command = btn_min_isclicked
)
btn_min_.pack(side=LEFT, expand=True, fill="both")
btn_min_.bind("<Enter>", entered_min)
btn_min_.bind("<Leave>", left_min)
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
    command=btn1_isclicked,
)
btn1_.pack(side=LEFT, expand=True, fill="both")
btn1_.bind("<Enter>", entered_1)
btn1_.bind("<Leave>", left_1)
btn2_ = Button(
    btn_row4,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command=btn2_isclicked,
)
btn2_.pack(side=LEFT, expand=True, fill="both")
btn2_.bind("<Enter>", entered_2)
btn2_.bind("<Leave>", left_2)

btn3_ = Button(
    btn_row4,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command=btn3_isclicked,
)
btn3_.pack(side=LEFT, expand=True, fill="both")
btn3_.bind("<Enter>", entered_3)
btn3_.bind("<Leave>", left_3)

btn_plus_ = Button(
    btn_row4,
    text="+",
    font=("Verdana", 17),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command = btn_plus_isclicked
)
btn_plus_.pack(side=LEFT, expand=True, fill="both")
btn_plus_.bind("<Enter>", entered_plus)
btn_plus_.bind("<Leave>", left_plus)
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
    command = btn_percent_isclicked
)
btn_percent_.bind("<Enter>", entered_percent)
btn_percent_.bind("<Leave>", left_percent)
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
    command=btn0_isclicked,
)
btn0_.pack(side=LEFT, expand=True, fill="both")
btn0_.bind("<Enter>", entered_0)
btn0_.bind("<Leave>", left_0)

btn_dot_ = Button(
    btn_row5,
    text=".",
    font=("Verdana", 22),
    width=2,
    anchor=CENTER,
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command = btn_dot_isclicked,
)
btn_dot_.pack(side=LEFT, expand=True, fill="both")
btn_dot_.bind("<Enter>", entered_dot)
btn_dot_.bind("<Leave>", left_dot)

btn_equal_ = Button(
    btn_row5,
    text="=",
    font=("Verdana", 17),
    relief=GROOVE,
    border=0,
    bg="#3b3b3b",
    fg="orange",
    activebackground="gray",
    command=result,

)
btn_equal_.pack(side=LEFT, expand=True, fill="both")
btn_equal_.bind("<Enter>", entered_equal)
btn_equal_.bind("<Leave>", left_euqal)

window.mainloop()
