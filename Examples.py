from tkinter import*
w_width=500
w_height=700

window=Tk()
window.geometry(str(w_width)+ "x" + str(w_height))
window.title("My App")

main_frame = Frame(background="red", width=w_width, height=w_height)
main_frame.pack()

hello_label = Label(text="Hello, World!")
hello_label.place(x=300, y=300)

#window.grid()
#hello_label = Label(text="Hello, World!")
#hello_label.grid(column=0, row=0)#for multiple buttons


#hello_label = Label(text="Hello, World")
#hello_label.pack(side="top")



#image before stretch
#Background gradient image
        #bg_image = PhotoImage(file="Images/background.png")
        #bg_label = Label(self.window, image=bg_image)
        #bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#Initialize balance to 0
        #self.balance = 0

#Resize and move the logo to left corner
        #logo_image = Image.open("Images/Logo.png").resize((209, 121))
        #logo_photo = ImageTk.PhotoImage(logo_image)
        #self.logo_label.config(image=logo_photo)
        #self.logo_label.image = logo_photo #keep a reference to avoid garbage collection
        #self.logo_label.place(relx=0.0, rely=0.0, anchor=NW)
        
# size of window
        #self.window.geometry("500x500")

#when exiting
#def exit(self):
        #if messagebox.askquestion("askquestion", "Are you sure?"):
            #self.window.destroy()
window.mainloop()
