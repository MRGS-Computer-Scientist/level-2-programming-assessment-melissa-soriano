from tkinter import*

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

#set the background gradient


#Logo
logo_image = PhotoImage(file="Images/Logo.png")
logo_label = Label(window, image=logo_image)
logo_label.pack()

#Username
username_label = Label(window, text="Username: ")
username_label.pack()
username_entry = Entry(window)
username_entry.pack()

#Password
password_label = Label(window, text="Password: ")
password_label.pack()
password_entry = Entry(window)
password_entry.pack()

#Login Button
login_button = Button(window,text="Login", command=login)
login_button.pack()

window.mainloop()