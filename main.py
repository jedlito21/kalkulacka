from tkinter import *

okno = Tk()

okno.geometry('300x300')
okno.resizable(0, 0)
okno.title("Kalkulus 3000")

input_text = StringVar()


def on_click(text):
    input_field.insert(END, text)


def clear():
    input_field.delete(0, END)


def equals():
    input_eq = input_field.get()
    input_field.delete(0, END)
    try:
        answer = eval(input_eq)
    except:
        input_field.insert(END, "Error")
    else:
        input_field.insert(END, answer)

    # input_field.insert(END, answer)


input_frame = Frame(okno, width=300, height=70, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1)
input_frame.grid(row=0, column=0, columnspan=4)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=25, bg="#eee", fg="black",
                    bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

text = Entry(okno, width=300)

left_bracket = Button(okno, text="(", width=4, height=2, command=lambda: on_click("("))
left_bracket.grid(row=1, column=0)

right_bracket = Button(okno, text=")", width=4, height=2, command=lambda: on_click(")"))
right_bracket.grid(row=1, column=1)

power = Button(okno, text="x²", width=4, height=2, command=lambda: on_click("**2"))
power.grid(row=1, column=2)

square_root = Button(okno, text="√", width=4, height=2, command=lambda: on_click("**(1/2)"))
square_root.grid(row=1, column=3)

one = Button(okno, text="1", width=4, height=2, command=lambda: on_click("1"))
one.grid(row=2, column=0)

two = Button(okno, text="2", width=4, height=2, command=lambda: on_click("2"))
two.grid(row=2, column=1)

three = Button(okno, text="3", width=4, height=2, command=lambda: on_click("3"))
three.grid(row=2, column=2)

three = Button(okno, text="C", width=4, height=2, command=clear)
three.grid(row=2, column=3)

four = Button(okno, text="4", width=4, height=2, command=lambda: on_click("4"))
four.grid(row=3, column=0)

five = Button(okno, text="5", width=4, height=2, command=lambda: on_click("5"))
five.grid(row=3, column=1)

six = Button(okno, text="6", width=4, height=2, command=lambda: on_click("6"))
six.grid(row=3, column=2)

plus = Button(okno, text="+", width=4, height=2, command=lambda: on_click("+"))
plus.grid(row=3, column=3)

seven = Button(okno, text="7", width=4, height=2, command=lambda: on_click("7"))
seven.grid(row=4, column=0)

two = Button(okno, text="8", width=4, height=2, command=lambda: on_click("8"))
two.grid(row=4, column=1)

nine = Button(okno, text="9", width=4, height=2, command=lambda: on_click("9"))
nine.grid(row=4, column=2)

minus = Button(okno, text="-", width=4, height=2, command=lambda: on_click("-"))
minus.grid(row=4, column=3)

point = Button(okno, text=".", width=4, height=2, command=lambda: on_click("."))
point.grid(row=5, column=0)

times = Button(okno, text="*", width=4, height=2, command=lambda: on_click("*"))
times.grid(row=5, column=1)

devide = Button(okno, text="/", width=4, height=2, command=lambda: on_click("/"))
devide.grid(row=5, column=2)

equals = Button(okno, text="=", width=4, height=2, command=equals)
equals.grid(row=5, column=3)

zero = Button(okno, text="0", width=20, height=2, command=lambda: on_click("0"))
zero.grid(row=6, column=0, columnspan=3)



okno.mainloop()
