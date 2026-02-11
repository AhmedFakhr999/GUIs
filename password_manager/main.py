from tkinter import * 
from tkinter import messagebox
import random
import pyperclip
import json


LOGO='logo.png'

def find_password():
    try:
        website_name=website_field.get()
        with open('data.json','r') as data_file:
            data=json.load(data_file) 
    except FileNotFoundError :
        
        messagebox.showinfo(title='Error',message=f"password doesn\'t exist or wrong email typed")
    else:
        if website_name in data:
            email=data[website_name]["email"] 
            passwrd=data[website_name]["password"]
            messagebox.showinfo(title='website info',message=f"the email is :{email} \n the password is : {password}")
        else:
            messagebox.showerror(title='Error',message="An Error has Occured,please try again , make sure that website name is correct")
        
        

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    # this here will make the list get random order
    random.shuffle(password_list)
    # and here will take every single element after shuffling it and place in string variable
    password_generated = "".join(password_list)
    try:
        
        pyperclip.copy(password_generated)
        print('copied success')
    except:
        print('failed to copy')
    
    password_field.delete(0, END)
    password_field.insert(0, password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_val=website_field.get()
    email_val=email_field.get()
    password_val=password_field.get()
    
    new_data = {
        website_val: {
            "email": email_val,
            "password": password_val
        }
    }
    if len(website_val)==0 or len(email_val)==0 or len(password_val)==0:
        messagebox.showinfo(title='NOTIFY',message='you should fill the fields with a value')
    else:
        try : 
            with open('data.json', 'r') as data_file:
                data=json.load(data_file)
                
        except FileNotFoundError:
            
            with open('data.json', 'w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_field.delete(0,END) 
            email_field.delete(0,END) 
            password_field.delete(0,END)
        
   

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

logo_png = PhotoImage(file=LOGO)

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website')
website_label.grid(row=1, column=0, pady=5)

email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0, pady=5)

password_label = Label(text='Password')
password_label.grid(row=3, column=0, pady=5)

# Entries
website = StringVar()
website_field = Entry(textvariable=website, width=21)
website_field.grid(row=1, column=1, sticky="EW", pady=5)

email = StringVar()
email_field = Entry(textvariable=email, width=35)
email_field.grid(row=2, column=1, columnspan=2, sticky="EW", pady=5)

password = StringVar()
password_field = Entry(textvariable=password, width=21)
password_field.grid(row=3, column=1, sticky="EW", pady=5)

# Buttons
search_button = Button(text='Search', width=13, background='blue', fg='black',command=find_password)
search_button.grid(row=1, column=2, sticky="EW", pady=5)

generate_button = Button(text='Generate Password', command=password_generator)
generate_button.grid(row=3, column=2, sticky="EW", pady=5)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", pady=5)

window.mainloop()