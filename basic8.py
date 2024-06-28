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

# from tkinter import *

# window = Tk()

# channel = ["youtube", "facebook", "google"]
# channelImg = PhotoImage(file="./youtube.png")

# channelImage = [
#     channelImg.subsample(8, 8),
#     channelImg.subsample(8, 8),
#     channelImg.subsample(8, 8),
# ]


# def order():
#     if x.get() == 0:
#         print("you are watching Youtube")
#     elif x.get() == 1:
#         print("you are watching Facebook")
#     elif x.get() == 2:
#         print("you are watching Google")
#     else:
#         print("what?")


# x = IntVar()

# for i in range(len(channel)):
#     radioBtn = Radiobutton(
#         window,
#         text=channel[i],
#         variable=x,
#         value=i,
#         image=channelImage[i],
#         compound="left",
#         indicatoron=0,
#         width=400,
#         command=order,
#     )
#     radioBtn.pack(anchor=W, padx=25, pady=10)

# window.mainloop()


# scale

# from tkinter import *


# def submit():
#     print(f"現在溫度：{str(scale.get())}度")


# window = Tk()

# photo = PhotoImage(file="./youtube.png")
# # photo = photo.subsample(2, 2)
# label = Label(image=photo)
# label.pack()

# scale = Scale(
#     window,
#     from_=100,
#     to=0,
#     length=600,
#     orient=VERTICAL,
#     font=("Arial", 20),
#     tickinterval=10,
#     showvalue=0,
#     resolution=5,
#     troughcolor="steelblue",
#     fg="red",
#     bg="black",
# )

# scale.set((scale["from"] - scale["to"]) / 2 + scale["to"])

# scale.pack()


# dice = PhotoImage(file="./dices.png")
# label = Label(image=dice)
# label.pack()


# button = Button(
#     window,
#     text="送出",
#     command=submit,
# )
# button.pack()

# window.mainloop()
