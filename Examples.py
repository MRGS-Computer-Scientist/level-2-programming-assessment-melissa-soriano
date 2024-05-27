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



# size of window
        #self.window.geometry("500x500")

#when exiting
#def exit(self):
        #if messagebox.askquestion("askquestion", "Are you sure?"):
            #self.window.destroy()
window.mainloop()
