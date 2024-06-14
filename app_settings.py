from email import message
from tkinter import CENTER, NW
from tkinter.ttk import Progressbar
from tkinter import Toplevel, Label, Button, Entry


class CustomMessageBox(Toplevel):
            
      def __init__(self, parent, title, message):
            super().__init__(parent)
            self.title(title)
            self.geometry("500x150")
            self.resizable(False, False)

            label = Label(self, text=message, padx=20, pady=10, font=("Great Vibes", 15))
            label.pack(pady=10)
                  
            ok_button = Button(self, text="OK", bg="green", fg="white", command=self.destroy, width=5, height=1)
            ok_button.pack(pady=5)

def hide_main_page_widgets(self):
    self.welcome_label.place_forget()
    self.balance_label.place_forget()
    self.enter_allowance_button.place_forget()
    self.saving_button.place_forget()
    self.expense_button.place_forget()
    self.track_button.place_forget()
    self.logout_button.place_forget()

def hide_enter_allowance_widgets(app):
      app.allowance_label.place_forget()
      app.allowance_entry.place_forget()
      app.enter_button.place_forget()
      app.exit_button.place_forget()
    
def hide_enter_savings_widgets(app):
      app.savings_title.place_forget()
      app.current_saving_message.place_forget()
      app.savings_entry.place_forget()
      app.enter_savings_button.place_forget()
      app.exit_savings_button.place_forget()

def hide_expense_widgets(app):
      app.expense_label.place_forget()
      app.expense_entry.place_forget()
      app.enter_button.place_forget()
      app.exit_button.place_forget()

def hide_track_widgets(app):
      app.transaction_label.place_forget()
      app.transactions_list.place_forget()
      app.exit_button.place_forget()

def sign_up(app):
      username = app.signup_username_entry.get()
      password = app.signup_password_entry.get()
      confirm_password = app.signup_confirm_entry.get()
      
      if len(username) < 3 or len(username) > 25:
            CustomMessageBox(app.window, "Error", "Username must be between 3 and 25 characters.")
            return
      
      if len(password) < 5 or len(password) > 20:
            CustomMessageBox(app.window, "Error", "Password must be between 5 and 20 characters.")
            return
      
      if password != confirm_password:
            CustomMessageBox(app.window, "Error", "Password do not match.")
            return
      
      app.user = {}
      if username in app.users:
            CustomMessageBox(app.window, "Error", "Username already exists.")
      else:
            app.users[username] = password
            CustomMessageBox(app.window, "Success", "Account created successfully!")
            app.login()

def Login(app):
      username = app.username_entry.get()
      password = app.password_entry.get()

      if len(username) < 3 or len(username) > 25:
            CustomMessageBox(app.window, "Error", "Username must be between 3 and 25 characters.")
            return

      if len(password) < 5 or len(password) >20:
            CustomMessageBox(app.window, "Error", "Password must be between 5 and 20 characters.")
            return

      if username in app.users and app.users[username] == password:
            print("Username: ", username)
            print("Password: ", password)

            app.username_label.place_forget()
            app.username_entry.place_forget()
            app.password_entry.place_forget()
            app.login_button.place_forget()

            app.loading_bar = Progressbar(app.window, length=250, mode='indeterminate')
            app.loading_bar.place(relx=0.5, rely=0.5, anchor=CENTER)

            app.loading_bar.start()
            app.window.after(500, app.show_main_page)
      
      else:
            CustomMessageBox(app.window, "Error", "Invalid username or password.")
            
            
def place_logo(self):
        pass
        
    
