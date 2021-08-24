import sqlite3

def connInit():
    connection = sqlite3.connect("../pythonProjects/BookGUI/book.db")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()

def insert_row(title, author, year, isbn):
    connection = sqlite3.connect("../pythonProjects/BookGUI/book.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("../pythonProjects/BookGUI/book.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    connection.close()
    return rows

def search_rows(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("../pythonProjects/BookGUI/book.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    rows = cur.fetchall()
    connection.close()
    return rows

def delete(id):
    connection = sqlite3.connect("../pythonProjects/BookGUI/book.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    connection.commit()
    connection.close()

def update(id, title, author, year, isbn):
    connection = sqlite3.connect("../pythonProjects/BookGUI/book.db")
    cur = connection.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    connection.commit()
    connection.close()

#print(view())
#insert_row(title="cc", author="cc", year=3, isbn=3)
#print(search_rows(title="aa"))
#delete(1)
#update(1, "bb", "bb", 2, 2)
#print(view())