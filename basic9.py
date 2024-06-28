# listbox

from tkinter import *


def submit():

    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    # print(f"你預定了{listbox.get(listbox.curselection())}")

    for index in food:
        print(f"你預定了：{index}")


def add():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())
    entry.delete(0, END)


def delete():
    # listbox.delete(listbox.curselection())

    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window, width=12, font=("Arial", 24), selectmode=MULTIPLE)
listbox.pack()

listbox.insert(0, "pizza")
listbox.insert(1, "pasta")
listbox.insert(2, "garlic")
listbox.insert(3, "bread")
listbox.insert(4, "fries")

listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()


addBtn = Button(window, text="新增", command=add)
addBtn.pack()

submitBtn = Button(window, text="預定", command=submit)
submitBtn.pack()

delBtn = Button(window, text="刪除", command=delete)
delBtn.pack()

window.mainloop()
