# Day 27 Tkinter GUI basic learning
# pack, place, grid.  pack and grid are incompatible
# pack: self.pack(side = )
# place: self.place(x= , y= )
# grid:  self.grid(column=, row =)

import tkinter

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("Clicked")

window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)  # add pad in the window, to make space

# label
my_label = tkinter.Label(text = "I am a label", font=("Arial",24, "bold"))
# change the config
my_label["text"] = "New Text"
# method 2
my_label.config(text="New Text")
# my_label.pack(side ="left")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Create button

button = tkinter.Button(text = "Button", command= button_clicked)
## button.pack()  # make sure the button packed on the screen
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button, command= button clicked")
new_button.grid(column=2, row=0)


# generate entry component
input = tkinter.Entry(width=20)
input.get()  # take input
input.grid(column=3, row=2)






window.mainloop() # keep window on.