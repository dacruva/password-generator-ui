from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_', '~', '.']


def password_generator():
    password = ""
    password_list = []
    # for letter in range(1, nr_letters + 1):
    #     password_list.append(random.choice(letters))
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_symbols + password_numbers + password_letters

    shuffle(password_list)
    password = "".join(password_list)

    password_result_entry.insert(0, f"{password}")
    window.clipboard_clear()
    window.clipboard_append(password)


def save2file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_result_entry.get()

    if not website or not password:
        messagebox.showwarning(0, "Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \n"
                                                      f"Email: {email} \nPassword: {password}\n Is it ok to save?")

        if is_ok:
            with open("supersecrets.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            # Clearing entries
            website_entry.delete(0, "end")
            password_result_entry.delete(0, "end")


window = Tk()
window.title("PyPassword Generator!")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "@mail.com")
password_result_entry = Entry(width=21)
password_result_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate", command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save2file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
