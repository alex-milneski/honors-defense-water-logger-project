from tkinter import *
import random
from tkinter import Entry
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():

    password_e.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    params_let = parameters_let.get()
    params_num = parameters_num.get()
    params_sym = parameters_sym.get()

    password_letters = [random.choice(letters) for _ in range(int(params_let))]
    password_numbers = [random.choice(numbers) for _ in range(int(params_num))]
    password_symbols = [random.choice(symbols) for _ in range(int(params_sym))]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    password_e.insert(0, generated_password)

    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_text():


    website = website_e.get().lower()
    email = email_e.get()
    password = password_e.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0:
        messagebox.showinfo(title="OOPS!", message=f"Please enter a valid website")
    elif len(password) == 0:
        messagebox.showinfo(title="OOPS!", message=f"Please enter a valid password")
    else:

        try:
            with open('password_manager.json', 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open('password_manager.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('password_manager.json', 'w') as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo(title="Confirmation", message=f'Password {password} was saved to Password Manager '
                                                                  f'file for {website}')
        finally:
            # I want to sort the keys (website) alphabetically but cannot get a .sort() function to
            # work on the JSON dictionary
            password_e.delete(0,END)
            website_e.delete(0,END)



#----------------------------- FIND PASSWORD FEATURE ------------------ #


def find_password():

# use 'all small letters' function so there is no capitalization mistake
    website = website_e.get().lower()



    with open('password_manager.json', 'r') as file:
        search_data = json.load(file)

    if website in search_data:
        password = search_data[website]['password']
        messagebox.showinfo(title=f'{website}', message=f'PASSWORD: {password}')
        pyperclip.copy(password)
    else:
        messagebox.showinfo(title=f'{website}', message=f'entry for {website} does not exist in Password Manager')

# ---------------------------- DELETE AN ENTRY ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.config(padx=20, pady=20)
root.title("Password Generator")


canvas = Canvas(height=200, width=200)
myimg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=myimg)
canvas.grid(row=0, column=1)

# LABELS

website_l = Label(text="website:", anchor="e")
website_l.grid(row=1,column=0)
email_l = Label(text="email/username:", anchor="e")
email_l.grid(row=2,column=0)
password_l = Label(text="password:", anchor="e")
password_l.grid(row=3,column=0)
parameters_let_l = Label(text="# of letters", anchor="e")
parameters_let_l.grid(row=4, column=0)
parameters_num_l = Label(text="# of numbers:", anchor="e")
parameters_num_l.grid(row=5, column=0)
parameters_sym_l = Label(text="# of symbols:", anchor="e")
parameters_sym_l.grid(row=6, column=0)

# ENTRY BOXES

website_e = Entry(width=35)
website_e.grid(row=1,column=1, columnspan=2)
website_e.focus()
email_e = Entry(width=35)
email_e.insert(0, "yourmostusedemail@aol.com")
email_e.grid(row=2,column=1, columnspan=2)
password_e = Entry(width=27)
password_e.grid(row=3,column=1)
parameters_let = Entry(width=7)
parameters_let.grid(row=4,column=1)
parameters_num = Entry(width=7)
parameters_num.grid(row=5,column=1)
parameters_sym = Entry(width=7)
parameters_sym.grid(row=6,column=1)
parameters_let.insert(0, "4")
parameters_num.insert(0, "4")
parameters_sym.insert(0, "3")

# BUTTONS

search_b = Button(text='Search', command=find_password)
search_b.grid(row=1,column=2)
g_pass = Button(text="generate", command=generate_pass)
g_pass.grid(row=3,column=2)
add_pass = Button(text="save to file", command=save_text)
add_pass.grid(row=4,column=2)

root.mainloop()

