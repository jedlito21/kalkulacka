from tkinter import *

okno = Tk()

okno.geometry('330x480')
okno.title("Kalkulus 3000")

num_rows = 7
num_columns = 4

for i in range(num_rows):
    okno.rowconfigure(i, weight=1)
for k in range(num_columns):
    okno.columnconfigure(k, weight=1)

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

def plus_minus():
    on_click("*-1")
    input_eq = input_field.get()
    input_field.delete(0, END)
    try:
        answer = eval(input_eq)
    except:
        input_field.insert(END, "Error")
    else:
        input_field.insert(END, answer)



input_frame = Frame(okno, width=300, bd=0, bg="#DADADA",
                    highlightthickness=1)
input_frame.grid(row=0, column=0, columnspan=4, sticky="nswe")

input_field = Entry(input_frame, font=('Orator Std', 25), border=0.5, relief="solid", textvariable=input_text, width=25, bg="#DADADA", fg="black",
                    bd=0, justify=RIGHT)
input_field.grid(row=0, column=0, sticky="nswe")
input_field.pack(ipady=10)

text = Entry(okno, width=300)

left_bracket = Button(okno, text="(", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("("))
left_bracket.grid(row=2, column=0, sticky="nswe")

right_bracket = Button(okno, text=")", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click(")"))
right_bracket.grid(row=2, column=1, sticky="nswe")

power = Button(okno, text="x²", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("**2"))
power.grid(row=1, column=1, sticky="nswe")

square_root = Button(okno, text="√", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("**(1/2)"))
square_root.grid(row=1, column=2, sticky="nswe")

one = Button(okno, text="1", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("1"))
one.grid(row=3, column=0, sticky="nswe")

two = Button(okno, text="2", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("2"))
two.grid(row=3, column=1, sticky="nswe")

three = Button(okno, text="3", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("3"))
three.grid(row=3, column=2, sticky="nswe")

c = Button(okno, text="C", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=clear)
c.grid(row=1, column=3, sticky="nswe")

four = Button(okno, text="4", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("4"))
four.grid(row=4, column=0, sticky="nswe")

five = Button(okno, text="5", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("5"))
five.grid(row=4, column=1, sticky="nswe")

six = Button(okno, text="6", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("6"))
six.grid(row=4, column=2, sticky="nswe")

plus = Button(okno, text="+", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("+"))
plus.grid(row=2, column=3, sticky="nswe")

seven = Button(okno, text="7", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("7"))
seven.grid(row=5, column=0, sticky="nswe")

two = Button(okno, text="8", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("8"))
two.grid(row=5, column=1, sticky="nswe")

nine = Button(okno, text="9", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("9"))
nine.grid(row=5, column=2, sticky="nswe")

minus = Button(okno, text="-", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("-"))
minus.grid(row=3, column=3, sticky="nswe")

point = Button(okno, text=".", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("."))
point.grid(row=6, column=2, sticky="nswe")

times = Button(okno, text="*", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("*"))
times.grid(row=4, column=3, sticky="nswe")

devide = Button(okno, text="/", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("/"))
devide.grid(row=5, column=3, sticky="nswe")

equals = Button(okno, text="=", font=('Orator Std', 14), bg="orange", border=0.5, relief="solid", width=4, height=2, command=equals)
equals.grid(row=6, column=3, sticky="nswe")

zero = Button(okno, text="0", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=8, height=2, command=lambda: on_click("0"))
zero.grid(row=6, column=0, columnspan=2, sticky="nswe")

one_over = Button(okno, text="1/x", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=lambda: on_click("1/"))
one_over.grid(row=1, column=0, sticky="nswe")

plu_min = Button(okno, text="±", font=('Orator Std', 14), bg="white", border=0.5, relief="solid", width=4, height=2, command=plus_minus)
plu_min.grid(row=2, column=2, sticky="nswe")

okno.mainloop()
