from tkinter import*
from app_settings import hide_main_page_widgets, hide_enter_allowance_widgets, CustomMessageBox, hide_enter_savings_widgets, hide_expense_widgets, hide_track_widgets
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image # type: ignore #Import ImageTk and Image from PIL
import json
import os
from tkinter import messagebox

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
        
        def show_hide():
            if self.show_hide_button['text'] == 'Show':
                self.password_entry.config(show='')
                self.show_hide_button.config(text="Hide")
            else:
                self.password_entry.config(show='*')
                self.show_hide_button.config(text="Show")

        self.show_hide_button = Button(self.window, text="Show", command=show_hide, bg="#81c3d7")
        self.show_hide_button.place(relx=0.63, rely=0.65, anchor=CENTER)

        #Confirm Password
        self.confirm_label = Label(self.window, text="Confirm Password: ")
        self.confirm_label.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.confirm_entry = Entry(self.window, show="*")
        self.confirm_entry.place(relx=0.5, rely=0.75, anchor=CENTER)
        
        def confirm_show_hide():
            if self.confirm_show_hide_button['text'] == 'Show':
                self.confirm_entry.config(show='')
                self.confirm_show_hide_button.config(text='Hide')
            else:
                self.confirm_entry.config(show='*')
                self.confirm_show_hide_button.config(text="Show")

        self.confirm_show_hide_button = Button(self.window, text="Show", command=confirm_show_hide, bg="#81c3d7")
        self.confirm_show_hide_button.place(relx=0.63, rely=0.75, anchor=CENTER)
        
        #Login Button
        self.login_button = Button(self.window,text="ENTER", command=self.login, bg="#70e000")
        self.login_button.place(relx=0.5, rely=0.85, anchor=CENTER)

        #Initialize balance to 0
        self.balance = 0
        self.savings= 0 

        #List to store transactions
        self.transactions = []

        self.window.mainloop()

#Function to print username and password
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        #To check if the username meets the length requirements
        if len(username)< 3 or len(username)> 25:
            CustomMessageBox(self.window, "Error", "Username must be between 3 to 25 characters.")
            return
        
        #To check if password meets the length requirements
        if len(password) < 5 or len(password) > 20:
            CustomMessageBox(self.window, "Error", "Password must be between 5 to 20 characters.")
            return
        
        #To check if confirm password match the password 
        if password != confirm:
            CustomMessageBox(self.window, "Error", "Passwords do not match.")
            return
        
        self.username = username
        self.password = password
        self.load_user_data()
    
    def load_user_data(self):
        filename = "accounts.txt"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    accounts = json.load(f)
                except json.JSONDecodeError:
                    accounts = {}
            
            user_data = accounts.get(self.username)
            if user_data:
                saved_password = user_data.get('password')
                if saved_password != self.password:
                    CustomMessageBox(self.window, "Error", "Incorrect password.")
                    return

                #Mask the password
                user_data['password'] = saved_password
                self.balance = user_data.get('balance', 0)
                self.savings = user_data.get('savings', 0)
                self.transactions = user_data.get('transactions', [])
            else:
                CustomMessageBox(self.window, "Info", "No existing account found. A new account will be created.")
        else:
            CustomMessageBox(self.window, "Info", "No existing account found. A new account will be created.")
            accounts = {}

        #Save new user data
        accounts[self.username] = user_data
        with open(filename, 'w') as f:
            json.dump(accounts, f)

        #Hide login widgets
        self.username_label.place_forget()
        self.username_entry.place_forget()
        self.password_label.place_forget()
        self.password_entry.place_forget()
        self.confirm_label.place_forget()
        self.confirm_entry.place_forget()
        self.login_button.place_forget()
        self.confirm_show_hide_button.place_forget()
        self.show_hide_button.place_forget()
        
        #Create a loading bar
        self.loading_bar = Progressbar(self.window, length=250, mode='indeterminate')
        self.loading_bar.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Show loading bar
        self.loading_bar.start()

        #Simulate delay 
        self.window.after(500, self.show_main_page)
  
    def save_user_data(self):
        filename = "accounts.txt"

        #New user data
        new_user_data = {
            self.username:{
                'password': self.password,
                'balance': self.balance,
                'savings': self.savings,
                'transactions': self.transactions
            }
        }

        #Read existing data from the file
        existing_data = []
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip():#To check if line is empty in accounts.txt
                        existing_data.append(json.loads(line.strip()))
        except FileNotFoundError:
            pass
        
        # Check if the user already exists and update their data
        user_exists = False
        for user_data in existing_data:
            if self.username in user_data:
                user_data[self.username] = new_user_data[self.username]
                user_exists = True
                break
            
        # If the user does not exist, add their data to the list
        if not user_exists:
            existing_data.append(new_user_data)

        # Write all data back to the file, each user on a new line
        with open(filename, 'w') as f:
            for user_data in existing_data:
                f.write(json.dumps(user_data) + '\n')

        print("User data saved successfully.")

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

        #Code to update the balance and transaction list
        #Add the allowanceto the current balance
        self.balance += allowance
        self.transactions.append(f"Allowance: +${allowance}")


        #Update the balance message
        balance_message = "Your balance is $" + str(self.balance)
        self.balance_label.config(text=balance_message)

        #Clear the entry field
        self.allowance_entry.delete(0, END)

        #show a message bow to confirm the allowance was added
        CustomMessageBox(self.window, "Allowance Added", "Allowance successfully added!")

    def saving(self):
        #Hide the main page widgets
        hide_main_page_widgets(self)

        self.show_loading()
        
        def show_saving_widgets():
            self.hide_loading()
            #Code to place logo
            self.place_logo()

            #Savings title
            self.savings_title = Label(self.window, text="Savings", font=("Arial", 50), bg="#caf0f8")
            self.savings_title.place(relx=0.5, rely=0.3, anchor=CENTER)

            #Current savings message
            current_saving_message = "Your current savings is $" + str(self.savings)
            self.current_saving_message = Label(self.window, text=current_saving_message, font=("Arial", 25), bg="#caf0f8")
            self.current_saving_message.place(relx=0.5, rely=0.4, anchor=CENTER)

            #Entry for typing savings
            self.savings_entry = Entry(self.window, font=("Arial", 30), width=10)
            self.savings_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

            #Enter Button
            self.enter_savings_button = Button(self.window, text="Enter", command=self.add_savings, bg="#70e000", font=("Arial", 20))
            self.enter_savings_button.place(relx=0.5, rely=0.6, anchor=CENTER)

            #Exit Button
            self.exit_savings_button = Button(self.window, text="Exit", command=lambda: [self.show_main_page(), hide_enter_savings_widgets(self)], bg="red", font=("Arial", 20))
            self.exit_savings_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        #Schedule the display of the window after 1 second
        self.window.after(1000, show_saving_widgets)

    def add_savings(self):
        #Get the entered savings
        savings_str = self.savings_entry.get()
        if not savings_str:
            #If the entry field is empty, show an error message
            CustomMessageBox(self.window, "Error", "Please enter valid savings")
            return
        
        try:
            savings = float(savings_str)
        
        except ValueError:
            #If input cannot be  converted to a float, show an error message
            CustomMessageBox(self.window, "Error", "Please enter a valid number for savings.")
            return
        
        #Codes to update the savings and transactions list
        #Add the savings to the currect savings
        self.savings += savings
        self.transactions.append(f"Savings: +{savings}")

        #Update the savings message
        current_saving_message = "Your current savings is $" + str(self.savings)
        self.current_saving_message.config(text=current_saving_message)

        #Clear the entry field
        self.savings_entry.delete(0, END)

        #To show a message to tell that the savings was added
        CustomMessageBox(self.window, "Savings Added", "Savings is successfully added!")

    def expense(self):
        #To Hide the main page widgets
        hide_main_page_widgets(self)

        self.show_loading()
        
        def expense_widgets():
            self.hide_loading()
            #place logo
            self.place_logo()

            #Expense title
            self.expense_label = Label(self.window, text="Expense", font=("Arial", 50), bg="#caf0f8")
            self.expense_label.place(relx=0.5, rely=0.3, anchor=CENTER)

            #Entry for typing expense
            self.expense_entry = Entry(self.window, font=("Arial", 30), width=10)
            self.expense_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

            #Enter button
            self.enter_button = Button(self.window, text="Enter",command=self.add_expense, bg="#70e000", font=("Arial", 20))
            self.enter_button.place(relx=0.5, rely=0.6, anchor=CENTER)

            #Exit button
            self.exit_button = Button(self.window, text="Exit", command=lambda: [self.show_main_page(), hide_expense_widgets(self)], bg="red", font=("Arial", 20))
            self.exit_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        #Schedule the display of the widgets after 1 Second
        self.window.after(1000, expense_widgets)

    def add_expense(self):
        #Get the entered expense
        expense_str = self.expense_entry.get()
        if not expense_str:
            #if the entry field is empty, show an error message
            CustomMessageBox(self.window, "Error", "Please enter valid expense")
            return
        
        try:
            expense = float(expense_str)

        except ValueError:
            #if the input cannot be converted to a float, it will show an error
            CustomMessageBox(self.window, "Error", "Please enter a valid number for expense.")
            return
        
        #Codes to update balance and transaction list
        #Subtract the expense from the current balance
        self.balance -= expense
        self.transactions.append(f"Expense: -${expense}")

        #Update the balance message in the main page
        self.balance_label.config(text="Your balance is $" + str(self.balance))

        #Clear the entry field
        self.expense_entry.delete(0, END)

        #Show succes message
        CustomMessageBox(self.window, "Success", "Expense subtracted successfully!")

    def track(self):
        #Hide the main page widgets
        hide_main_page_widgets(self)

        self.show_loading()
        
        def show_track_widgets():
            self.hide_loading()

            #To place logo
            self.place_logo()

            #set the label text based on the number of transaction
            if len(self.transactions) == 1:
                transactions_text = "Transaction"
            else:
                transactions_text = "Transactions"

            #Transaction text
            self.transaction_label = Label(self.window, text=transactions_text, font=("Arial", 50), bg="#caf0f8")
            self.transaction_label.place(relx=0.5, rely=0.2, anchor=CENTER)

            #Placeholder for transactions       
            self.transactions_list = Listbox(self.window, font=("Arial", 20))
            self.transactions_list.place(relx=0.5, rely=0.6, anchor=CENTER)

            #Exit button
            self.exit_button = Button(self.window, text="Exit",  command=lambda: [self.show_main_page(), hide_track_widgets(self)], bg="red", font=("Arial", 20))
            self.exit_button.place(relx=0.5, rely=0.9, anchor=CENTER)

            #Add transaction to the listbox
            for transaction in self.transactions:
                self.transactions_list.insert(END, transaction)

        #Schedule the display of the widgets  after 1 second
        self.window.after(1000, show_track_widgets)

#Code for logout
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
    
    #Code to confirm logout
    def confirm_logout(self, top):
        self.save_user_data()
        top.destroy()
        self.window.destroy()
    
#instance of my app
app = App()