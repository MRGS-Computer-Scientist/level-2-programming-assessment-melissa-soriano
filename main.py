from tkinter import*
from app_settings import*

#Function to print username and password
def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username: ", username)
    print("Password: ", password)

#Creating the main window
window=Tk()
window.title("Cash Control")

#size of window
window.geometry("500x500")

#Logo
logo_image = PhotoImage(file="Images/Logo.png")
logo_label = Label(window, image=logo_image, bg="white")
logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)

#Username
username_label = Label(window, text="Username: ")
username_label.place(relx=0.5, rely=0.5, anchor=CENTER)
username_entry = Entry(window)
username_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

#Password
password_label = Label(window, text="Password: ")
password_label.place(relx=0.5, rely=0.6, anchor=CENTER)
password_entry = Entry(window, show="*")
password_entry.place(relx=0.5, rely=0.65, anchor=CENTER)

#Login Button
login_button = Button(window,text="ENTER", command=login, bg="#CB997E")
login_button.place(relx=0.5, rely=0.75, anchor=CENTER)

window.mainloop()