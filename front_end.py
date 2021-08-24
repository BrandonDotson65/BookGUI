from tkinter import *
from back_end import Database
"""
A program that stores the following information:
Author
ISBN
Title
Year

The user can do the following with records:
View
Update
Add
Delete
Close
"""
db = Database()

mainWindow = Tk()
mainWindow.resizable(0,0)
mainWindow.iconbitmap("../pythonProjects/BookGUI/books.ico")
mainWindow.title("Book DB")

label1 = Label(mainWindow, text="Title")
label1.grid(row=0, column=0)

label2= Label(mainWindow, text="Author")
label2.grid(row=0, column=2)

label3 = Label(mainWindow, text="Year")
label3.grid(row=1, column=0)

label4 = Label(mainWindow, text="ISBN")
label4.grid(row=1, column=2)

title_text = StringVar()
entryL1 = Entry(mainWindow, textvariable=title_text)
entryL1.grid(row=0, column=1)

author_text = StringVar()
entryL2 = Entry(mainWindow, textvariable=author_text)
entryL2.grid(row=0, column=3)

year_text = StringVar()
entryL3 = Entry(mainWindow, textvariable=year_text)
entryL3.grid(row=1, column=1)

isbn_text = StringVar()
entryL4 = Entry(mainWindow, textvariable=isbn_text)
entryL4.grid(row=1, column=3)

listB = Listbox(mainWindow, height=6, width=35)
listB.grid(row=2, column=0, rowspan=6, columnspan=2)
scrollB = Scrollbar(mainWindow)
scrollB.grid(row=2, column=2, rowspan=6)

listB.configure(yscrollcommand=scrollB.set)
scrollB.configure(command=listB.yview)

def get_selected_row(event):
    try:
        global selected_row
        index=listB.curselection()[0]
        selected_row = listB.get(index)
        entryL1.delete(0, END)
        entryL1.insert(0, selected_row[1])
        entryL2.delete(0, END)
        entryL2.insert(0, selected_row[2])
        entryL3.delete(0, END)
        entryL3.insert(0, selected_row[3])
        entryL4.delete(0, END)
        entryL4.insert(0, selected_row[4])
    except IndexError:
        pass

#wrapper functions
def view_rows():
    #delete previous entries so no overlap
    listB.delete(0, END)
    for row in db.view():
        listB.insert(END, row)

def search_data():
    listB.delete(0, END)
    rows = db.search_rows(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    for row in rows:
        listB.insert(END, row)

def add_entry():
    db.insert_row(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listB.delete(0, END)
    listB.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def update_row():
    db.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_rows()

def delete_row():
    db.delete(selected_row[0])
    view_rows()

def clear_listB():
    listB.delete(0, END)

def openInfoWindow():
    newWindow = Toplevel(mainWindow)
    newWindow.title('About')
    newWindow.resizable(0,0)
    newWindow.geometry("190x200")
    Label(newWindow, text="Written in Python 3.9\nutilizing Tkinter by \nBrandon Dotson", font=('helvetica', 11, 'bold')).pack()
    Label(newWindow, text="\nThe program will allow the\nuser to save, update,\n delete, and view book\n records that are saved\n in a .db file.", font=('helvetica', 11,)).pack()
    Label(newWindow, text="Uses SQLite3 for the DB.", font=('helvetica', 11,)).pack()

def clear_all():
    listB.delete(0, END)
    entryL1.delete(0, END)
    entryL2.delete(0, END)
    entryL3.delete(0, END)
    entryL4.delete(0, END)

listB.bind('<<ListboxSelect>>', get_selected_row)

button1=Button(mainWindow, text='View All', width=12, command=view_rows)
button1.grid(row=2, column=3)

button2=Button(mainWindow, text='Search Entry', width=12, command=search_data)
button2.grid(row=3, column=3)

button3=Button(mainWindow, text='Add Entry', width=12, command=add_entry)
button3.grid(row=4, column=3)

button4=Button(mainWindow, text='Update Selection', width=12, command=update_row)
button4.grid(row=5, column=3)

button5=Button(mainWindow, text='Delete Selection', width=12, command=delete_row)
button5.grid(row=6, column=3)

button6=Button(mainWindow, text='Close', width=12, command=mainWindow.destroy)
button6.grid(row=7, column=3)

button6=Button(mainWindow, text='Info', width=12, command=openInfoWindow)
button6.grid(row=7, column=0, columnspan=1)

button7=Button(mainWindow, text='Clear List', width=12, command=clear_listB)
button7.grid(row=7, column=1, columnspan=1)

button8=Button(mainWindow, text='Clear All', command=clear_all)
button8.grid(row=7, column=2, columnspan=1)

mainWindow.mainloop()

