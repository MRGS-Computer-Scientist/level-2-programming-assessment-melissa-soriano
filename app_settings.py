from tkinter import NW


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
    

def place_logo(self):
        pass
        
    
