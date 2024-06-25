# button

# from tkinter import *

# window = Tk()

# count = 0


# def click():
#     global count
#     count += 1
#     print("你點擊了按鈕" + str(count))


# photo = PhotoImage(file="./youtube.png")

# button = Button(
#     window,
#     text="點擊按鈕",
#     command=click,
#     font=("Ariel", 30),
#     fg="orange",
#     bg="black",
#     activeforeground="orange",
#     activebackground="black",
#     state="active",
#     image=photo,
#     compound="bottom",
# )
# button.pack()

# window.mainloop()


# entry box

# from tkinter import *

# window = Tk()


# def sent():
#     input = entry.get()
#     print(input)
#     entry.delete(0, END)
#     entry.config(state="disabled")


# def delete():
#     entry.delete(0, END)


# def backspace():
#     entry.delete(len(entry.get()) - 1, END)


# entry = Entry(window, font=("Arial, 50"), fg="#00FF00", bg="black", show="*")

# entry.insert(0, "你好啊")
# entry.pack(side="left")

# backspace_button = Button(window, text="倒回", command=backspace)
# backspace_button.pack(side="right")

# delete_button = Button(window, text="清空", command=delete)
# delete_button.pack(side="right")

# submit_button = Button(window, text="送出", command=sent)
# submit_button.pack(side="right")


# window.mainloop()


# checkbox

# from tkinter import *


# def display():
#     if x.get():
#         print("你選擇選項一")
#     else:
#         print("你沒有選擇選項一")


# window = Tk()


# x = BooleanVar()
# # IntVar()
# # StringVar()

# photo = PhotoImage(file="./youtube.png")
# photo = photo.subsample(8, 8)

# checkBtn = Checkbutton(
#     window,
#     text="選項一",
#     variable=x,
#     onvalue=True,
#     offvalue=False,
#     command=display,
#     font=("Arial", 20),
#     fg="orange",
#     bg="black",
#     activeforeground="orange",
#     activebackground="black",
#     state="active",
#     padx=25,
#     pady=10,
#     image=photo,
#     compound=LEFT,
# )
# checkBtn.pack(side="left")

# window.mainloop()


# radio button

from tkinter import *

window = Tk()

food = ["youtube", "facebook", "google"]

x = IntVar()

for i in range(len(food)):
    radioBtn = Radiobutton(window, text=food[i], variable=x, value=i)
    radioBtn.pack()

window.mainloop()
