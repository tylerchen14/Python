# zip

# username = ["tyler", "steven", "noah"]
# password = ["123", "456", "789"]
# date = ("1/1", "2/2", "3/3")

# # group = dict(zip(username, password))
# group = list(zip(username, password, date))

# # for key, value in group.items():
# #     print(key + " " + value)

# for i in group:
#   print(i)

# __name__

# print(__name__)
# 可用來判斷是否為主要程式，或是被引入的程式

# time function
# import time

# print(time.ctime(0))
# print(time.time())
# print(time.ctime(time.time()))
# clock = time.localtime()
# print(clock)

# formatTime = time.strftime("%Y %B %d %H:%M:%S", clock)
# print(formatTime)

# time_str = "14 October 1994"
# tObject = time.strptime(time_str, "%d %B %Y")
# print(tObject)

# time_tuple = (1994, 10, 14, 0, 0, 0, 4, 287, -1)
# time_t = time.asctime(time_tuple)
# print(time_t)

# multi threading
# import threading
# import time


# def eat():
#     time.sleep(3)
#     print("you are eating")


# def sleep():
#     time.sleep(4)
#     print("you are sleeping")


# def run():
#     time.sleep(5)
#     print("you are running")


# x = threading.Thread(target=eat)
# y = threading.Thread(target=sleep)
# z = threading.Thread(target=run)

# x.start()
# y.start()
# z.start()

# print(time.perf_counter())


# daemon thread

# import threading
# import time


# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("you have logged in for", count, " seconds")


# x = threading.Thread(target=timer, daemon=True)
# x.start()

# answer = input("do you wish to stop?")


# GUI windows
# GUI = Graphical User Interface (GUI)

# from tkinter import *

# window = Tk()
# window.geometry("500x500")
# window.title("專案內容")
# icon = PhotoImage(file="youtube.png")
# window.iconphoto(True, icon)
# window.config(background="Grey")
# window.mainloop()

# label in GUI
# from tkinter import *

# window = Tk()
# window.geometry("500x500")

# photo = PhotoImage(file="youtube.png")
# photo = photo.subsample(5, 5)

# label = Label(
#     window,
#     text="你好啊",
#     font=("Arial", 40, "bold"),
#     fg="orange",
#     bg="black",
#     relief=RAISED,
#     bd=6,
#     padx=20,
#     pady=20,
#     image=photo,
#     compound="top",
# )
# # label.place(x=0, y=0)
# label.pack()

# window.mainloop()
