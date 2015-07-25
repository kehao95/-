__author__ = "kehao"
import shelve
from tkinter import *
from tkinter import ttk


class DataBase:
    db = 0

    def __init__(self, dbname):
        self.db = shelve.open(dbname, writeback=True)

    def __del__(self):
        self.db.close()

    def set(self, key, dic=None):
        if dic is None:
            del self.db[key]
        else:
            self.db[key] = dic

    def get(self, key):
        try:
            return self.db[key]
        except Exception as ex:
            print('no key:', key)
            return None

    def getAll(self):
        for key in self.db:
            yield key, self.db[key]


class Person:
    person = dict(name=0,
                  age=0,
                  position=0,
                  salary=0)

    def getPerson(self):
        name = input("name:")
        age = input("age:")
        position = input("position:")
        salary = input("salary:")
        self.set(name, age, position, salary)

    def print(self):
        print(self.person)

    def set(self, name, age, position, salary):
        p = self.person
        p['name'] = name
        p['age'] = age
        p['position'] = position
        p['salary'] = salary

    def Dict(self):
        return self.person


"""
def testDB():
    db = DataBase('database')
    p = Person()
    p.set('wang', 30, 'CEO', 100000)
    db.set('wang', p.Dict())
    print(db.get('wang'))
"""


def main():
    db = DataBase('database')

    def insert():
        global db
        global text
        print('insert')
        r = {'key': text.key.get(), 'name': text.name.get(), 'age': int(text.age.get()),
             'position': text.position.get(),
             'salary': int(text.salary.get())}
        db.set(r['key'], r)

    def find():
        global db
        global text
        = db.get(text.key)

    print('find')


# the root tk
root = Tk()
root.title("雇员信息输入")
# insert mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# don't know what's for
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)

# set the GUI
text = dict(
    key=StringVar(),
    name=StringVar(),
    age=StringVar(),
    position=StringVar(),
    salary=StringVar()
)
ttk.Label(mainframe, text="键值").grid(column=1, row=0, sticky=W)
feet_entry = ttk.Entry(mainframe, width=10, textvariable=text.key)
feet_entry.grid(column=2, row=0, sticky=(E))
ttk.Label(mainframe, text="姓名").grid(column=1, row=1, sticky=W)
feet_entry = ttk.Entry(mainframe, width=10, textvariable=text.name)
feet_entry.grid(column=2, row=1, sticky=(E))
ttk.Label(mainframe, text="年龄").grid(column=1, row=2, sticky=W)
feet_entry = ttk.Entry(mainframe, width=10, textvariable=text.age)
feet_entry.grid(column=2, row=2, sticky=(E))
ttk.Label(mainframe, text="职位").grid(column=1, row=3, sticky=W)
feet_entry = ttk.Entry(mainframe, width=15, textvariable=text.position)
feet_entry.grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="薪水").grid(column=1, row=4, sticky=W)
feet_entry = ttk.Entry(mainframe, width=15, textvariable=text.salary)
feet_entry.grid(column=2, row=4, sticky=(E))
ttk.Button(mainframe, text="插入雇员", command=insert).grid(column=1, row=5, columnspan=2, sticky=E)
root.bind('<Return>', insert)
ttk.Button(mainframe, text="查找", command=find).grid(column=1, row=5, columnspan=1, sticky=E)
for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=5)
root.mainloop()

if __name__ == '__main__':
    main()
