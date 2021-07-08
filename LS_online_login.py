from tkinter import *
from tkinter import messagebox


def exitapplication():
    msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msgbox == 'yes':
        window.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def user():
    window.destroy()
    import main


def admin():
    window.destroy()
    import Admin_login


window = Tk()
window.title("Sign in")
window.geometry("1000x600")
window.config(background='#80b636')

# Image

canvas = Canvas(window, width=900, height=300)
canvas.place(x=50, y=50)
img = PhotoImage(file="lifechoices-services-8.png")
canvas.create_image(0, 0, anchor=NW, image=img)

cal_btn = Button(window, text='Log in as User', bg='#8dc63f', command=user, borderwidth=5, width=10)
cal_btn.place(x=600, y=400)

cal_btn = Button(window, text='Log in as Admin', bg='#8dc63f', command=admin, borderwidth=5, width=10)
cal_btn.place(x=300, y=400)

exit_btn = Button(window, text='Exit', bg='#8dc63f', command=exitapplication, borderwidth=5, width=10)
exit_btn.place(x=600, y=450)


window.mainloop()
