"""

# -*- coding: utf-8 -*-
Created on          01 Feb 2019 at 6.39 PM
@author:            Arvind Sachidev Chilkoor
Created using:      PyCharm
Name of Project:    Bookstore Database Project - FRONTEND GUI

"""

"""
This program is for the frontend code of the Bookstore App, which is basically the GUI.
"""



from tkinter import *
import AppbookstoredbBACKEND                       #This imports the back-end script here.


def get_selected_row(event):
    """
    This function recieves the row, which the user has selected via list1.bind and passes it as "event" as arguements
    to get_selected_row, and return back the selected tuple for deletion.
    :param event:
    :return:
    """
    try:
        global selected_tuple               # declared global var, since used by delete_command and list1.bind
        index=list1.curselection()[0]       # This gets the index of selected tuple from the listbox, curselection()[0], gets the data at index 0 of the tuple.
        selected_tuple=list1.get(index)
        e1.delete(0,END)                    # empty the box for title
        e1.insert(END,selected_tuple[1])    # insert the entry of index[1] which is the title
        e2.delete(0,END)                    # empty the box for author
        e2.insert(END,selected_tuple[2])    # insert the entry of index[1] which is the author
        e3.delete(0,END)                    # empty the box for year
        e3.insert(END,selected_tuple[3])    # insert the entry of index[1] which is the year
        e4.delete(0,END)                    # empty the box for isbn
        e4.insert(END,selected_tuple[4])    # insert the entry of index[1] which is the isbn
    except IndexError:
        pass                                # pass if there is an index error



def view_command():
    """
    This command triggers when the View All button is pressed, list1.delete erases the previous contents of the listbox
    The for loop traverses through the view_data() in the Backend script
    The list1.insert, inserts the data from the database into the list box as per ID.
    :return:
    """
    list1.delete(0,END)
    for row in AppbookstoredbBACKEND.view_data():
        list1.insert(END,row)

def search_command():
    """
    Search command receives the parameter from user, i.e. the search parameter for title, author, year or isbn
    and every row realting to search data inserts into the listbox
    :return:
    """
    list1.delete(0,END)
    for row in AppbookstoredbBACKEND.search_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def insert_command():
    """
    Recieves the parameter to insert via get() for title or author or year or isbn.
    passes the value to backend for insert into table
    :return:
    """
    AppbookstoredbBACKEND.insert_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def update_command():
    """
    Recieves the update from the user through get() for either title, author, year, isbn as per user entry,
    passes the value to backend for update of table
    :return:
    """
    AppbookstoredbBACKEND.update_data(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def delete_command():
    """
    Recieves the selected_tuple after the user selects on the GUI and passes the value to backend for deletion.
    :return:
    """
    AppbookstoredbBACKEND.del_data(selected_tuple[0])


window = Tk()

window.title("Arvind's Bookstore App")


l1 = Label(window, text="Title")        # button label for title
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")       # button label for author
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")         # button label for year
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")         # button label for ISBN
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text) # For user input of the title variable, and grid location of box
e1.grid(row=0, column=1)


author_text = StringVar()
e2 = Entry(window, textvariable=author_text) # For user input of the author variable, and grid location of box
e2.grid(row=0, column=3)


year_text = StringVar()
e3 = Entry(window, textvariable=year_text)  # For user input of the year variable, and grid location of box
e3.grid(row=1, column=1)


isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)  # For user input of the isbn variable, and grid location of box
e4.grid(row=1, column=3)

list1 = Listbox(window, height=10, width=65)    # Listbox decleration and grid location
list1.grid(row=2, column=0, rowspan=6, columnspan=2)


sb1 = Scrollbar(window)                 #Scroll bar decleration
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set) #Scroll bar assignment
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",get_selected_row)    #Decleration of Listbox bind with selected tuple by user

b1 = Button(window, text='View All', width=12, command=view_command) # Button Decleration
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()   # Tkinter method to keep the GUI active loop, until user closes the window