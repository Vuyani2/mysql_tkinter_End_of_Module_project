from tkinter import *
from tkinter import messagebox
import mysql.connector

login_info = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database="LS_login",
                               auth_plugin="mysql_native_password")

mycursor = login_info.cursor()
xy = mycursor.execute("Select * from login_info")

def register():
    global login_info
    sql = "INSERT INTO login_info VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nameentry.get(), entrysurname.get(), IDentry.get(), entryPno.get(), NOKNameentry.get(), entryNOKPno.get(), userentry.get(), entryuserpass.get())
    mycursor.execute(sql, val)
    login_info.commit()
    print(mycursor.rowcount, "record installed")
    import pdb;pdb.set_trace()
    mycursor.execute("Select * from login_info")
    for i in mycursor:
        print(i)
    import main

def clear_entry():
    pass

root = Tk()
root.title("Registration")
root.geometry("500x400")
root.config(bg='black')

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)



lblname = Label(frame, text="Enter your Name")
lblname.grid(row=1, column=1)

nameentry = Entry(frame, )
nameentry.grid(row=1, column=2, pady=5)

lblsurname = Label(frame, text="Enter your surname")
lblsurname.grid(row=2, column=1)

entrysurname = Entry(frame, )
entrysurname.grid(row=2, column=2, pady=5)

lblID = Label(frame, text="Enter your ID number")
lblID.grid(row=3, column=1)

IDentry = Entry(frame, )
IDentry.grid(row=3, column=2, pady=5)

lblPno = Label(frame, text="Enter your phone number")
lblPno.grid(row=4, column=1)

entryPno = Entry(frame, )
entryPno.grid(row=4, column=2, pady=5)


lblNOKName = Label(frame, text="Next of kin's name")
lblNOKName.grid(row=5, column=1)

NOKNameentry = Entry(frame, )
NOKNameentry.grid(row=5, column=2, pady=5)

lblNOKno = Label(frame, text="next of kin's phone number")
lblNOKno.grid(row=6, column=1)

entryNOKPno = Entry(frame, )
entryNOKPno.grid(row=6, column=2, pady=5)


userlbl = Label(frame, text="Create Your Username")
userlbl.grid(row=7, column=1)

userentry = Entry(frame, )
userentry.grid(row=7, column=2, pady=5)

lbluserpass = Label(frame, text="Create user password")
lbluserpass.grid(row=8, column=1)

entryuserpass = Entry(frame, )
entryuserpass.grid(row=8, column=2, pady=5)

reset_btn = Button(frame, text='clear', bg='#8dc63f', command=clear_entry)
reset_btn.grid(row=9, column=2, pady=8)

exit_btn = Button(frame, text='Exit', bg='#8dc63f', command=lambda: root.destroy())
exit_btn.grid(row=10, column=2, pady=5)

reg_btn = Button(frame, text='Register', bg='#8dc63f', command=register)
reg_btn.grid(row=9, column=1, pady=5)

root.mainloop()
