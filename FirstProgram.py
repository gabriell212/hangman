from tkinter import *
root = Tk()
root.title("Simple calculator")

#Text box
entry_text = Entry(root, width=30, borderwidth=5)
entry_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Buttons commands
def WriteNumber(number):
    current = entry_text.get()
    entry_text.delete(0, END)
    entry_text.insert(0, str(current) + str(number))

def Clear():
    entry_text.delete(0, END)

def AddNumbers():
    global first_number
    first_number = entry_text.get()
    first_number = int(first_number)
    entry_text.delete(0, END)

def Equal():
    second_number = entry_text.get()
    second_number = int(second_number)
    entry_text.delete(0, END)
    entry_text.insert(0, first_number + second_number)

#Buttons
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: WriteNumber(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: WriteNumber(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: WriteNumber(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: WriteNumber(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: WriteNumber(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: WriteNumber(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: WriteNumber(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: WriteNumber(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: WriteNumber(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: WriteNumber(0))
button_clear = Button(root, text="Clear", padx=57, pady=20, command=Clear)
button_add = Button(root, text="+", padx=29, pady=20, command=AddNumbers)
button_equal = Button(root, text="=", padx=66, pady=20, command=Equal)

#Button positioning
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()