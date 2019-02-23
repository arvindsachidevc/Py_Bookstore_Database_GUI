"""

# -*- coding: utf-8 -*-
Created on          01 Feb 2019 at 7.21 PM
@author:            Arvind Sachidev Chilkoor
Created using:      PyCharm
Name of Project:    Bookstore Database Project - BACKEND Database

"""


"""
This program is for the Backend code of the Bookstore App, which is basically the DATABASE using the SQLite3.

"""


import sqlite3


def connect():
    """
    Connect function creates the database using SQLite3 library, and creates the table in the database with,
    ID, TITLE, AUTHOR, YEAR, ISBN columns
    :return:
    """
    conn = sqlite3.connect("BookApp.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert_data(title, author, year, isbn):
    '''
    Insert data inserts the user input into the table respectively
    :param title:
    :param author:
    :param year:
    :param isbn:
    :return:
    '''
    conn = sqlite3.connect("BookApp.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Book VALUES(NULL, ?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()
    view_data()


def view_data():
    '''
    View data displays all the contents in the listbox
    :return:
    '''
    conn = sqlite3.connect("BookApp.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_data(title="",author="",year="",isbn=""):
    '''
    Search data finds the row, containing the search parameter as entered by the user in the frontend GUI
    :param title:
    :param author:
    :param year:
    :param isbn:
    :return:
    '''
    conn = sqlite3.connect("BookApp.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def del_data(id):
    '''
    Del data, deletes the data based on the selection of the user keyed in the frontend GUI
    :param id:
    :return:
    '''
    conn = sqlite3.connect("BookApp.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Book WHERE id=?", (id,))
    conn.commit()
    conn.close()
    view_data()

def update_data(id,title,author,year,isbn):
    """
    Update data will update the respective column, either title, author, year or isbn as the case maybe, and user input.
    :param id:
    :param title:
    :param author:
    :param year:
    :param isbn:
    :return:
    """
    conn = sqlite3.connect("BookApp.db")
    cur = conn.cursor()
    cur.execute("UPDATE Book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()
    view_data()



connect()                       # establishes the connection with database.
