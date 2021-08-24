import sqlite3

class Database:

    #constructor
    def __init__(self):
        self.connection = sqlite3.connect("../pythonProjects/BookGUI/book.db")
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connection.commit()

    def insert_row(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
        self.connection.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search_rows(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.connection.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
#print(view())
#insert_row(title="cc", author="cc", year=3, isbn=3)
#print(search_rows(title="aa"))
#delete(1)
#update(1, "bb", "bb", 2, 2)
#print(view())