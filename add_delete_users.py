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
    pass


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


root.mainloop()
