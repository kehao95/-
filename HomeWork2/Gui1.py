__author__ = 'kehao'
"""
一个员工信息管理的GUI程序，要求实现员工信息（姓名，年龄，职位，薪资）的插入，以及查看所有员工信息，要求员工信息数据持久化存储在shelve中。最终代码提交网络学堂。
"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("雇员信息输入")

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
listframe = ttk.Frame(root, padding='3 3 3 3')
listframe.grid(column=0, row=1, sticky=(N, W, E, S))
listframe.columnconfigure(0, weight=1)
listframe.rowconfigure(0, weight=1)


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


@static_vars(line=0)
def show_one(name, age, position, salary):
    print("show new line")
    ttk.Label(listframe, text=name).grid(column=0, row=show_one.line, sticky=(W), padx=10, pady=5)
    ttk.Label(listframe, text=age).grid(column=1, row=show_one.line, sticky=(W), padx=10, pady=5)
    ttk.Label(listframe, text=position).grid(column=2, row=show_one.line, sticky=(W), padx=10, pady=5)
    ttk.Label(listframe, text=salary).grid(column=3, row=show_one.line, sticky=(W), padx=10, pady=5)
    show_one.line += 1


show_one(1, 1, 1, 1)
show_one(1, 1, 1, 1)
show_one(1, 1, 1, 1)


def insert():
    print('press')
    show_one(1, 1, 1, 1)


key = StringVar()
name = StringVar()
age = StringVar()
position = StringVar()
salary = StringVar()

ttk.Label(mainframe, text="键值").grid(column=1, row=1, sticky=W)
feet_entry = ttk.Entry(mainframe, width=10, textvariable=key)
feet_entry.grid(column=2, row=1, sticky=(E))

ttk.Label(mainframe, text="姓名").grid(column=1, row=1, sticky=W)
feet_entry = ttk.Entry(mainframe, width=10, textvariable=name)
feet_entry.grid(column=2, row=1, sticky=(E))

ttk.Label(mainframe, text="年龄").grid(column=1, row=2, sticky=W)
feet_entry = ttk.Entry(mainframe, width=10, textvariable=age)
feet_entry.grid(column=2, row=2, sticky=(E))

ttk.Label(mainframe, text="职位").grid(column=1, row=3, sticky=W)
feet_entry = ttk.Entry(mainframe, width=15, textvariable=position)
feet_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="薪水").grid(column=1, row=4, sticky=W)
feet_entry = ttk.Entry(mainframe, width=15, textvariable=salary)
feet_entry.grid(column=2, row=4, sticky=(E))

ttk.Button(mainframe, text="插入雇员", command=insert).grid(column=1, row=5, columnspan=2, sticky=E)

ttk.Button(mainframe, text="刷新", command=insert).grid(column=1, row=5, columnspan=1, sticky=E)
root.bind('<Return>', show_one(1, 1, 1, 1))


class ScrollTxtArea:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.textPad(frame)
        return

    def textPad(self, frame):
        # add a frame and put a text area into it
        textPad = Frame(frame)
        self.text = Text(textPad, height=50, width=90)

        # add a vertical scroll bar to the text area
        scroll = Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)

        # pack everythingF
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        textPad.pack(side=TOP)
        return


for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=5)
for child in listframe.winfo_children():
    child.grid_configure(padx=10, pady=5)

root.mainloop()
