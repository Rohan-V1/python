from tkinter import *

expression = " "


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = " "
    except:
        equation.set("error")
        expression = " "


def clear():
    global expression
    expression = " "
    equation.set(" ")


def create_button(label, row, column):
    if label == "=":
        button = Button(gui, text='=', fg='black', bg='white', command=equalpress, height=1, width=7)
        button.grid(row=row, column=column)
    elif label == "C":
        button = Button(gui, text='clear', fg='black', bg='white', command=clear, height=1, width=7)
        button.grid(row=row, column=column)
    else:
        button = Button(gui, text=label, fg='black', bg='white', command=lambda: press(label), height=1, width=7)
        button.grid(row=row, column=column)


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="grey")
    gui.title("Simple Calculator")
    gui.geometry("270x150")  # Corrected typo in geometry setting
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    button_labels = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '0', '.', 'C', '/','=']
    row = 2
    column = 0
    for label in button_labels:
        create_button(label, row, column)
        column += 1
        if column > 3:
            column = 0
            row += 1
    gui.mainloop()
