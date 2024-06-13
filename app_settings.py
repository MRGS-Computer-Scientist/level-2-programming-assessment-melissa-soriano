from email import message
from tkinter import NW
from tkinter import Toplevel, Label, Button


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
      
def place_logo(self):
        pass
        
    
