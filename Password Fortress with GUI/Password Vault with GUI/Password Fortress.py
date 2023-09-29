import sqlite3, hashlib
import tkinter
from tkinter import *
from tkinter import simpledialog
from functools import partial

# Database Code
with sqlite3.connect("password_vault.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY, 
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY, 
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")


# Create Popup
def popUp(text):

    answer = simpledialog.askstring("input string", text)


    return answer


# Initial Window
root = Tk()

root.title("Thee Password Fortress")

root.configure(bg='black')


def hashPassword(input):
    hash = hashlib.md5(input)
    hash = hash.hexdigest()

    return hash


def firstScreen():
    root.geometry("300x250")

    lbl = Label(root, text="Create Master Password", bg="black", fg="cyan")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(root, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(root, text="Re-Enter Password", bg="black", fg="cyan")
    lbl1.pack()

    txt1 = Entry(root, width=20, show="*")
    txt1.pack()
    txt1.focus()

    lbl2 = Label(root)
    lbl2.pack()

    def savePassword():
        if txt.get() == txt1.get():
            hashedPassword = hashPassword(txt.get().encode('utf-8'))

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [(hashedPassword)])
            db.commit()

            passwordVault()
        else:
            lbl2.config(text="Passwords do not match",  bg="black", fg="cyan")

    btn = Button(root, text="Save",  bg="cyan", fg="black", command=savePassword)
    btn.pack(pady=10)


def loginScreen():
    root.geometry("300x200")

    lbl = Label(root, text="Enter your Master Password",  bg="black", fg="cyan")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(root, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(root)
    lbl1.pack()

    def getMasterPassword():
        checkHashedPassword = hashPassword(txt.get().encode('utf-8'))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(checkHashedPassword)])

        return cursor.fetchall()

    def checkPassword():
        match = getMasterPassword()

        if match:
            passwordVault()
        else:
            txt.delete(0, 'end')

            lbl1.config(text="Wrong Password", bg="black", fg="cyan")

    btn = Button(root, text="Submit", bg="cyan", activebackground="magenta", command=checkPassword, borderwidth=1)
    btn.pack(pady=10)


def passwordVault():
    for widget in root.winfo_children():
        widget.destroy()


    def addEntry():
        text1 = "Enter Website/App"
        text2 = "Enter Username"
        text3 = "Enter Password"

        website = popUp(text1)
        username = popUp(text2)
        password = popUp(text3)

        insert_fields = """INSERT INTO vault(website,username,password)
        VALUES(?, ?, ?)"""

        cursor.execute(insert_fields, (website, username, password))
        db.commit()

        passwordVault()

    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()

        passwordVault()

    root.geometry("800x350")

    lbl = Label(root, text="Password Fortress", bg="black", fg="cyan")
    lbl.grid(column=1)

    btn = Button(root, text="New Fortress Entry", command=addEntry, bg="cyan", fg="black", activebackground="magenta")
    btn.grid(column=1, pady=10)

    lbl = Label(root, text="The Website/App", bg="black", fg="cyan")
    lbl.grid(row=2, column=0, padx=80)
    lbl = Label(root, text="Your Username", bg="black", fg="cyan")
    lbl.grid(row=2, column=1, padx=80)
    lbl = Label(root, text="Your Password", bg="black", fg="cyan")
    lbl.grid(row=2, column=2, padx=80)

    cursor.execute("SELECT * FROM vault")
    if(cursor.fetchall()!= None):
        i = 0
        while True:
            cursor.execute("SELECT * FROM vault")
            array = cursor.fetchall()

            lbl1 = Label(root, text=(array[i][1]), font=("TimesNewRoman", 12), bg="black", fg="cyan")
            lbl1.grid(column=0, row=i+3)
            lbl1 = Label(root, text=(array[i][2]), font=("TimesNewRoman", 12,), bg="black", fg="cyan")
            lbl1.grid(column=1, row=i+3)
            lbl1 = Label(root, text=(array[i][3]), font=("TimesNewRoman", 12), bg="black", fg="cyan")
            lbl1.grid(column=2, row=i+3)

            btn = Button(root, text="Delete", command= partial(removeEntry, array[i][0]),bg="cyan", fg="black", activebackground="magenta")
            btn.grid(column=3, row=i+3, pady=10)

            i = i+1

            cursor.execute("SELECT * FROM vault")
            if (len(cursor.fetchall()) <= i):
                break

cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    loginScreen()
else:
    firstScreen()
root.mainloop()