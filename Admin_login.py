from tkinter import *
from tkinter import messagebox
import mysql.connector


Login = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database="LS_login",
                                auth_plugin="mysql_native_password")

mycursor = Login.cursor()
xy = mycursor.execute("Select * from Admin_login")

obj = {}
for i in mycursor:
    rcv = {i[1]: i[2]}
    keys = rcv.keys()
    entries = rcv.values()

    for key in keys:
        for entry in entries:
            obj[key] = entry

print(obj)


user_pass = obj


def clear_entry():
    userentry.delete(0, 'end')
    entrypass.delete(0, 'end')


def exitapplication():
    msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msgbox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def user_pass_search(username, _password, _dict):
    if username in _dict:
        if _password == _dict[username]:
            return 1
        else:
            return 0
    else:
        return -1


def verify():
    user = userentry.get()
    password = entrypass.get()

    x = int(user_pass_search(user, password, user_pass))
    print(" ")
    if x == 1:
        root.destroy()
        import add_delete_users

    elif x == 0:
        messagebox.showinfo("Alert", "Incorrect password ")
        userentry.delete(0, 'end')
        entrypass.delete(0, 'end')
    elif x == -1:
        messagebox.showinfo("Alert", "Username Doesn't Exist")
        userentry.delete(0, 'end')
        entrypass.delete(0, 'end')


root = Tk()
root.title("Admin user Verification")
root.geometry("500x400")
root.config(bg='#80b636')

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)


lbluser = Label(frame, text="Enter your Username")
lbluser.grid(row=1, column=1)

userentry = Entry(frame, )
userentry.grid(row=1, column=2, pady=5)

lblpass = Label(frame, text="Enter your Password")
lblpass.grid(row=2, column=1)

entrypass = Entry(frame, )
entrypass.grid(row=2, column=2, pady=5)

reset_btn = Button(frame, text='clear', bg='#8dc63f', command=clear_entry, borderwidth=5, width=10)
reset_btn.grid(row=6, column=2, pady=8)

exit_btn = Button(frame, text='Exit', bg='#8dc63f', command=exitapplication, borderwidth=5, width=10)
exit_btn.grid(row=5, column=2, pady=5)

cal_btn = Button(frame, text='Log in', bg='#8dc63f', command=verify, borderwidth=5, width=10)
cal_btn.grid(row=5, column=1, pady=5)


root.mainloop()
