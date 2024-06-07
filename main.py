from tkinter import*
from app_settings import hide_main_page_widgets, hide_enter_allowance_widgets, CustomMessageBox
from tkinter.ttk import Progressbar
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
        self.photo = ImageTk.PhotoImage(image.resize((1000, 1000)))

        # Create a label for the background image
        bg_label = Label(self.window, image=self.photo)
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

        #To check if the username meets the length requirements
        if len(username)< 3 or len(username)> 25:
            CustomMessageBox(self.window, "Error", "Username must be between 3 and 25 characters.")
            return
        
        #To check if password meets the length requirements
        if len(password) < 5 or len(password) > 20:
            CustomMessageBox(self.window, "Error", "Password must be between 5 and 20 characters.")
            return
            
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
        
    def place_logo(self):
        #Resize and move the logo to left corner
        logo_image = Image.open("Images/Logo.png").resize((209, 121))
        logo_photo = ImageTk.PhotoImage(logo_image)
        self.logo_label.config(image=logo_photo)
        self.logo_label.image = logo_photo #keep a reference to avoid garbage collection
        self.logo_label.place(relx=0.0, rely=0.0, anchor=NW)

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
         #Hide the main page widgets
        hide_main_page_widgets(self)
        
        self.show_loading()
        def show_widgets():
            self.hide_loading()
            #place logo
            self.place_logo()

            #Enter Allowance text
            self.allowance_label = Label(self.window, text="Enter Allowance", font=("Arial", 50), bg="#caf0f8")
            self.allowance_label.place(relx=0.5, rely=0.3, anchor=CENTER)

            #Entry for typing allowance
            self.allowance_entry = Entry(self.window, font=("Arial", 30), width=10)
            self.allowance_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

            #Enter button
            self.enter_button = Button(self.window, text="Enter", command=self.add_allowance, bg="#70e000", font=("Arial", 20))
            self.enter_button.place(relx=0.5, rely=0.6, anchor=CENTER)

            #Exit button
            self.exit_button = Button(self.window, text="Exit", command=lambda: [self.show_main_page(), hide_enter_allowance_widgets(self)], bg="red", font=("Arial", 20))
            self.exit_button.place(relx=0.5, rely=0.7, anchor=CENTER)   
            
        #Schedule the display of the widgets after 1 second
        self.window.after(1000, show_widgets)


    def add_allowance(self):
        #Get the entered allowance
        allowance_str = self.allowance_entry.get()
        if not allowance_str:
            #If the entry field is empty, show an error message
            CustomMessageBox(self.window, "Error", "Please enter valid allowance")
            return
        
        try:
            allowance = float(allowance_str)
            
        except ValueError:
            # If the input cannot be converted to a float, show an error message
            CustomMessageBox(self.window, "Error", "Please enter a valid number for allowance.")
            return
    
        #Add the allowanceto the current balance
        self.balance += allowance

        #Update the balance message
        balance_message = "Your balance is $" + str(self.balance)
        self.balance_label.config(text=balance_message)
        #show a message bow to confirm the allowance was added
        CustomMessageBox("Allowance Added", "Allowance successfully added!")

    def saving(self):
        #Hide the main page widgets
        hide_main_page_widgets(self)

        self.show_loading()
        def show_saving_widgets():
            self.hide_loading()
            #Code to place logo
            self.place_logo()

            #Savings title
            savings_title = Label(self.window, text="Savings", font=("Arial", 50), bg="#caf0f8")
            savings_title.place(relx=0.5, rely=0.3, anchor=CENTER)

            #Current savings message
            current_saving_message = "Your current savings is $" + str(self.balance)
            current_saving_message = Label(self.window, text=current_saving_message, font=("Arial", 25), bg="#caf0f8")
            current_saving_message.place(relx=0.5, rely=0.4, anchor=CENTER)

            #Entry for typing savings
            self.savings_entry = Entry(self.window, font=("Arial", 30), width=10)
            self.savings_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

            #Enter Button
            self.enter_savings_button = Button(self.window, text="Enter", command=self.add_savings, bg="#70e000", font=("Arial", 20))
            self.enter_savings_button.place(relx=0.5, rely=0.6, anchor=CENTER)
            
        #Schedule the display of the window after 1 second
        self.window.after(1000, show_saving_widgets)
    def add_savings(self):
        #Get the entered savings
        savings_str = self.savings_entry.get()
        if not savings_str:
            #If the entry field is empty, show an error message
            CustomMessageBox("Error", "Please enter valid savings")
            return
        
        try:
            savings = float(savings_str)
        
        except ValueError:
            #If input cannot be  converted to a float, show an error message
            CustomMessageBox("Error", "Please enter a valid number for savings.")
            return
        
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
       top = Toplevel(self.window)
       top.title("Logout")
       top.geometry("300x100")
       top.resizable(False, False)

       label = Label(top, text="Are you sure you want to logout?", padx=20, pady=10)
       label.pack()

       button_frame = Frame(top)
       button_frame.pack(pady=10)

       ok_button = Button(button_frame, text="Logout", bg="green", fg="white", padx=10, pady=5, command=lambda: self.confirm_logout(top))
       ok_button.pack(side=LEFT, padx=10)

       cancel_button = Button(button_frame, text="Cancel", bg="red", fg="white", padx=10, pady=5, command=top.destroy)
       cancel_button.pack(side=RIGHT, padx=10)

    def confirm_logout(self, top):
        top.destroy()
        self.window.destroy()
    
#instance of my app
app = App()