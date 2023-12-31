from tkinter import *
import random
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password ="".join(password_list)
    # print(f"your password is {password}")
    password_input.insert(0,password)
    pyperclip.copy(password)  # automatically copy password
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title ="Warning", message ="Please fill all the field")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Email: {email}"
                                       f"\nPassword: {password}\n Is this ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.focus()  # the cursor start at website box
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "yijin1380@gmail.com")  # auto input in the entry box
password_input = Entry(width=20)
password_input.grid(column=1, row=3)




# Bottons
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1,row=4, columnspan=2)






window.mainloop()