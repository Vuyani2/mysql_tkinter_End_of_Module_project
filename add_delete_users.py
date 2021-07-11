from tkinter import *
from tkinter import messagebox
import mysql.connector


def exitapplication():
    msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msgbox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


login_info = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                     database="LS_login", auth_plugin="mysql_native_password")

mycursor = login_info.cursor(buffered=True)


def delete_user():
    mycursor.execute('DELETE FROM login_info WHERE name="' + userentry.get()+'"')
    login_info.commit()
    messagebox.showinfo("successful", "you have successfully deleted a user")


def make_admin():
    mycursor.execute("SELECT name, username, password from login_info WHERE name='" + userentry.get() + "'")
    val = mycursor.fetchall()
    tpt = ""
    for i in val:
        tpt = i
    print("INSERT INTO Admin_login(name, username, password) VALUES("+tpt[0] + ", " + tpt[1]+", " + tpt[2]+")")
    mycursor.execute("INSERT INTO Admin_login(name, username, password) VALUES('" + tpt[0] + "', '" + tpt[1]+"', '"
                     + tpt[2]
                     + "')")
    login_info.commit()
    messagebox.showinfo("successful", "you have successfully a user")


def log_count():
    mycursor.execute("SELECT * FROM login_info WHERE login_time is not NULL")
    count_login = len(mycursor.fetchall())
    mycursor.execute("SELECT * FROM login_info WHERE logout_time is not NULL")
    count_logout = len(mycursor.fetchall())
    messagebox.showinfo("Login's", " The number of people logged in is: " + str(count_login) +
                        " and The number of people logged out is: " + str(count_logout))



root = Tk()
root.title("ADD and Delete users")
root.geometry("500x400")
root.config(bg='#80b636')

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)


lbluser = Label(frame, text="Enter your Username")
lbluser.grid(row=1, column=1)

userentry = Entry(frame, )
userentry.grid(row=1, column=2, pady=5)

exit_btn = Button(frame, text='Exit', bg='#8dc63f', command=exitapplication, borderwidth=5, width=10)
exit_btn.grid(row=5, column=2, pady=5)

cal_btn = Button(frame, text='Make Admin', bg='#8dc63f', command=make_admin, borderwidth=5, width=10)
cal_btn.grid(row=5, column=1, pady=5)

reg_btn = Button(frame, text='Delete User', bg='#8dc63f', command=delete_user, borderwidth=5, width=10)
reg_btn.grid(row=6, column=1, pady=5)

count_btn = Button(frame, text="Log Count", bg='#8dc63f', command=log_count, borderwidth=5, width=10)
count_btn.grid(row=6, column=2, pady=5)


root.mainloop()
