from tkinter import NW


def hide_main_page_widgets(self):
    self.welcome_label.place_forget()
    self.balance_label.place_forget()
    self.enter_allowance.plaace_forget()
    self.saving_button.place_forget()
    self.expense_button.place_forget()
    self.track_button.place.forget()
    self.logout.place_forget()

def place_logo(self):
    self.logo_label.config(image=self.logo_photo)
    self.logo_label.image = self.logo_photo
    self.logo_label.place(relx=0.0, rely=0.0, anchor=NW)
    
    