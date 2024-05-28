from tkinter import *
from tkinter import messagebox

def clear_all():
    principle_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)

def calculate_ci():
    try:
        principle = int(principle_field.get())
        rate = float(rate_field.get())
        time = int(time_field.get())
        CI = principle * (pow((1 + rate / 100), time)) - principle
        compound_field.insert(10, CI)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values")

if __name__ == "__main__":
    root = Tk()
    root.configure(background='grey')
    root.geometry("400x250")  # Corrected typo in the geometry dimensions
    root.title('Compound Interest Calculator')

    label1 = Label(root, text="Principle Amount(Rs.):", fg="white", bg="grey")
    label2 = Label(root, text="Rate(%):", fg="white", bg="grey")
    label3 = Label(root, text="Time(yrs):", fg="white", bg="grey")
    label4 = Label(root, text="Compound Interest:", fg="white", bg="grey")

    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=5, column=0, padx=10, pady=10)

    principle_field = Entry(root)
    rate_field = Entry(root)
    time_field = Entry(root)
    compound_field = Entry(root)

    principle_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)  # Corrected row number
    compound_field.grid(row=5, column=1, padx=10, pady=10)

    btn1 = Button(root, text="Submit", bg="grey", fg="white", command=calculate_ci)
    btn2 = Button(root, text="Clear", bg="grey", fg="white", command=clear_all)

    btn1.grid(row=4, column=1, pady=10)
    btn2.grid(row=6, column=1, pady=10)

    root.mainloop()
