from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500 , height=300)

my_label = Label(text = "I am a Label" , font=("Arial" , 24 , "bold"))
my_label.pack(side =  "top")

def button_clicked():

    new_text = input.get()
    my_label.config(text=new_text)



button = Button(text="Click me", command= button_clicked)
button.pack()



input = Entry(width = 15)
input.pack()
input.get()



window.mainloop()
