__author__ = 'kehao'
"""
一个员工信息管理的GUI程序，要求实现员工信息（姓名，年龄，职位，薪资）的插入，以及查看所有员工信息，要求员工信息数据持久化存储在shelve中。最终代码提交网络学堂。
"""
from tkinter  import *
from tkinter import ttk
import shelve





class GUI:
    line = 0
    def show_one(self, name, age, position, salary):
        ttk.Label(self.listframe, text=name).grid(column=0, row=self.line, sticky=(W), padx=10, pady=5)
        ttk.Label(self.listframe, text=age).grid(column=1, row=self.line, sticky=(W), padx=10, pady=5)
        ttk.Label(self.listframe, text=position).grid(column=2, row=self.line, sticky=(W), padx=10, pady=5)
        ttk.Label(self.listframe, text=salary).grid(column=3, row=self.line, sticky=(W), padx=10, pady=5)
        self.line += 1

    def show_all(self):
        self.show_one('name','age','position','salary')
        for key, val in get_all(self.db):
            obj = val
            print(val)
            self.show_one(obj['name'], obj['age'], obj['position'], obj['salary'])

    def delete(self):
        name = self._name.get()
        for key,val in get_all(self.db):
            if val['name'] == name:
                print('del:', name)
                del self.db[key]
                self.refresh()

    def insert(self):
        key = str(self.line)
        name = self._name.get()
        age = self._age.get()
        position = self._position.get()
        salary = self._salary.get()
        for k,val in get_all(self.db):
            if val['name'] == name:
                return None
        for i in [name, age, position, salary]:
            if i == "":
                return None
        obj = dict(
            name=name,
            age=age,
            position=position,
            salary=salary
        )
        print('key'+str(key),'line'+str(self.line))
        print(obj)
        self.line += 1
        self.db[key] = obj
        self.show_one(name, age, position, salary)
        self.line += 1

    def refresh(self):
        for widget in self.listframe.winfo_children():
            widget.destroy()
        self.listframe.destroy()
        self.listframe = ttk.Frame(self.root, padding='3 3 3 3')
        self.listframe.grid(column=0, row=1, sticky=(N, W, E, S))
        self.listframe.columnconfigure(0, weight=1)
        self.listframe.rowconfigure(0, weight=1)
        self.show_all()

    def __init__(self, db):
        self.db = db
        dbshow(db)
        self.line = 0
        self.root = Tk()
        self.root.title("雇员信息输入")
        self.mainframe = ttk.Frame(self.root, padding="3 3 3 3")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.listframe = ttk.Frame(self.root, padding='3 3 3 3')
        self.listframe.grid(column=0, row=1, sticky=(N, W, E, S))
        self.listframe.columnconfigure(0, weight=1)
        self.listframe.rowconfigure(0, weight=1)

        self._key = StringVar()
        self._name = StringVar()
        self._age = StringVar()
        self._position = StringVar()
        self._salary = StringVar()
        """
        ttk.Label(self.mainframe, text="键值").grid(column=1, row=0, sticky=W)
        feet_entry = ttk.Entry(self.mainframe, width=10, textvariable=self._key)
        feet_entry.grid(column=2, row=0, sticky=(E))
        """
        ttk.Label(self.mainframe, text="姓名").grid(column=1, row=1, sticky=W)
        feet_entry = ttk.Entry(self.mainframe, width=10, textvariable=self._name)
        feet_entry.grid(column=2, row=1, sticky=(E))

        ttk.Label(self.mainframe, text="年龄").grid(column=1, row=2, sticky=W)
        feet_entry = ttk.Entry(self.mainframe, width=10, textvariable=self._age)
        feet_entry.grid(column=2, row=2, sticky=(E))

        ttk.Label(self.mainframe, text="职位").grid(column=1, row=3, sticky=W)
        feet_entry = ttk.Entry(self.mainframe, width=15, textvariable=self._position)
        feet_entry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(self.mainframe, text="薪水").grid(column=1, row=4, sticky=W)
        feet_entry = ttk.Entry(self.mainframe, width=15, textvariable=self._salary)
        feet_entry.grid(column=2, row=4, sticky=(E))

        ttk.Button(self.mainframe, text="插入雇员", command=self.insert).grid(column=1, row=5, columnspan=2, sticky=E)
        ttk.Button(self.mainframe, text="删除", command=self.delete).grid(column=1, row=5, columnspan=1, sticky=E)


        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.listframe.winfo_children():
            child.grid_configure(padx=10, pady=5)
        self.show_all()
        self.root.mainloop()


def get_all(database):
    for key in database:
        yield key, database[key]


def dbshow(db):
    for key, val in get_all(db):
        print('key:', key, "val:", val)


def main():
    DBNAME = 'shelve.db'
    db = shelve.open(DBNAME, writeback=True)
    foo = GUI(db)
    for i, j in get_all(db):
        print(i, j)


if __name__ == '__main__':
    main()
