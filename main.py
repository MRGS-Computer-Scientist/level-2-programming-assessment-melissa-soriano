from tkinter import*
from app_settings import*

class App():
    
    def __init__(self):
        #Creating the main window
        self.window=Tk()
        self.window.title("Cash Control")

        #size of window
        self.window.geometry("500x500")

        #Logo   
        logo_image = PhotoImage(file="Images/Logo.png")
        self.logo_label = Label(self.window, image=logo_image, bg="white")
        self.logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        #Username
        self.username_label = Label(self.window, text="Username: ")
        self.username_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.username_entry = Entry(self.window)
        self.username_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

        #Password
        self.password_label = Label(self.window, text="Password: ")
        self.password_label.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.password_entry = Entry(self.window, show="*")
        self.password_entry.place(relx=0.5, rely=0.65, anchor=CENTER)

        #Login Button
        self.login_button = Button(self.window,text="ENTER", command=self.login, bg="#CB997E")
        self.login_button.place(relx=0.5, rely=0.75, anchor=CENTER)

        self.window.mainloop()
    #Function to print username and password
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Username: ", username)
        print("Password: ", password)

#instance of my app
app = App()