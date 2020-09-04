"""
    A program that stores book information:
    Title, Author
    Year, ISBN

    User can:

    View all records
    Search an entry
    Add entry
    Update entry
    Delete
    Close
    """
from tkinter import *
import backend_Bookshop


def get_selected_row(event):
    try:
        global selected_tuple
        index = d1.curselection()[0]
        selected_tuple = d1.get(index)

        # Fill the Text Area when selected

        t1.delete(0, END)
        t1.insert(END, selected_tuple[1])
        t2.delete(0, END)
        t2.insert(END, selected_tuple[2])
        t3.delete(0, END)
        t3.insert(END, selected_tuple[3])
        t4.delete(0, END)
        t4.insert(END, selected_tuple[4])
    except:
        pass


def view_command():
    d1.delete(0, END)
    for row in backend_Bookshop.view():
        d1.insert(END, row)


def search_command():
    d1.delete(0, END)
    for row in backend_Bookshop.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        d1.insert(END, row)


def add_command():
    backend_Bookshop.insert(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    d1.delete(0, END)
    d1.insert(END, (title_text.get(), author_text.get(),
                    year_text.get(), isbn_text.get()))


def delete_command():
    backend_Bookshop.delete(selected_tuple[0])
    d1.delete(0, END)
    d1.insert(END, ("Deleted Successfully"))


def update_command():
    backend_Bookshop.update(
        selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    d1.delete(0, END)
    d1.insert(END, ("Updated Successfully"))


window = Tk()

window.wm_title("BookStore")

# Text Label

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)


l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Text Area

title_text = StringVar()
t1 = Entry(window, textvariable=title_text)
t1.grid(row=0, column=1)

author_text = StringVar()
t2 = Entry(window, textvariable=author_text)
t2.grid(row=0, column=4)

year_text = StringVar()
t3 = Entry(window, textvariable=year_text)
t3.grid(row=1, column=1)

isbn_text = StringVar()
t4 = Entry(window, textvariable=isbn_text)
t4.grid(row=1, column=4)

# Display Box

d1 = Listbox(window, height=20, width=60)
d1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Scroll Bar

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=8)

d1.config(yscrollcommand=sb1.set)
sb1.configure(command=d1.yview)

d1.bind('<<ListboxSelect>>', get_selected_row)

# Button

b1 = Button(text="View all", width=12, command=view_command)
b1.grid(row=2, column=4)
b2 = Button(text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=4)
b3 = Button(text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=4)
b4 = Button(text="Update", width=12, command=update_command)
b4.grid(row=5, column=4)
b5 = Button(text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=4)
b6 = Button(text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=4)

window.mainloop()
