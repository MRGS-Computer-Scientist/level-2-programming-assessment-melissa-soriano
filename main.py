from tkinter import*
from app_settings import*
from tkinter.ttk import Progressbar
from tkinter import messagebox
from PIL import ImageTk, Image # type: ignore #Import ImageTk and Image from PIL

class App():
    
    def __init__(self):
        #Creating the main window
        self.window=Tk()
        self.window.title("Cash Control")

        #size of window
        self.window.geometry("1000x1000")

        # Load and stretch the background image
        image = Image.open("Images/background.png")
        photo = ImageTk.PhotoImage(image.resize((1000, 1000)))

        # Create a label for the background image
        bg_label = Label(self.window, image=photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
         
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
        self.login_button = Button(self.window,text="ENTER", command=self.login, bg="#70e000")
        self.login_button.place(relx=0.5, rely=0.75, anchor=CENTER)

        #Initialize balance to 0
        self.balance = 0
        
        self.window.mainloop()
    #Function to print username and password
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Username: ", username)
        print("Password: ", password)

        #Hide login widgets
        self.username_label.place_forget()
        self.username_entry.place_forget()
        self.password_label.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()

        #Create a loading bar
        self.loading_bar = Progressbar(self.window, length=250, mode='indeterminate')
        self.loading_bar.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Show loading bar
        self.loading_bar.start()

        #Simulate delay 
        self.window.after(500, self.show_main_page)

    def show_main_page(self):
        #hide loading bar
        self.loading_bar.stop()
        self.loading_bar.place_forget()

        ####### MAIN PAGE #######

        #Resize and move the logo to left corner
        logo_image = Image.open("Images/Logo.png").resize((209, 121))
        logo_photo = ImageTk.PhotoImage(logo_image)
        self.logo_label.config(image=logo_photo)
        self.logo_label.image = logo_photo #keep a reference to avoid garbage collection
        self.logo_label.place(relx=0.0, rely=0.0, anchor=NW)

        #Welcome message with rounded rectangle
        welcome_message = "Welcome, " + self.username_entry.get()
        self.welcome_label = Label(self.window, text=welcome_message, font=("Arial", 50), bg="#caf0f8" )
        self.welcome_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.create_rounded_rectangle(self.welcome_label)
        

        #Balance message
        balance_message = "Your balance is $" + str(self.balance)
        self.balance_label = Label(self.window, text=balance_message, font=("Arial", 25), bg="#caf0f8")
        self.balance_label.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.create_rounded_rectangle(self.balance_label)

        #Buttons
        self.enter_allowance_button = Button(self.window, text="Enter Allowance", command=self.enter_allowance, bg="#ffb5a7")
        self.enter_allowance_button.place(relx=0.5, rely=0.52, anchor=CENTER)

        self.saving_button = Button(self.window, text="Saving", command=self.saving, bg="#ffb4a2")
        self.saving_button.place(relx=0.5, rely=0.58, anchor=CENTER)

        self.expense_button = Button(self.window, text="Expense", command=self.expense, bg="#ffb4a2")
        self.expense_button.place(relx=0.5, rely=0.64, anchor=CENTER)

        self.track_button = Button(self.window, text="Track", command=self.track, bg="#ffb4a2")
        self.track_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        #Logout Button
        self.logout_button = Button(self.window, text="Logout", command=self.logout, bg="#ffb4a2")
        self.logout_button.place(relx=0.9, rely=0.9, anchor=SE)

    def create_rounded_rectangle(self, widget):
        widget.config(bg="#caf0f8", relief="solid", bd=10, padx=10, pady=5, borderwidth=1, font=("Arial", 40))
        
    def show_loading(self):
        self.loading_bar = Progressbar(self.window, length=250, mode='indeterminate')
        self.loading_bar.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.loading_bar.start()

    def hide_loading(self):
        self.loading_bar.stop()
        self.loading_bar.place_forget()

    def enter_allowance(self):
        self.show_loading()
        self.window.after(1000, self.hide_loading)
        #code to go to the next page for entering allowance
        pass
    
    def saving(self):
        self.show_loading()
        self.window.after(1000, self.hide_loading)
        #code to go to the next page for entering saving
        pass

    def expense(self):
        self.show_loading()
        self.window.after(1000, self.hide_loading)
        #code to go to the next page for entering Expense page
        pass

    def track(self):
        self.show_loading()
        self.window.after(1000, self.hide_loading)
        #code to go to the next page
        pass

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            #reset UI or go back to login page
            self.reset_ui()

    def reset_ui(self):
        #Resetting the UI (returning to the login page) 
        print("Logging out....")       
    
#instance of my app
app = App()