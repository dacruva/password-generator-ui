import random
from tkinter import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_', '~', '.']


def passwordgen():
    password = ""
    password_list = []
    nr_letters = random.randrange(4, 6, 1)
    nr_symbols = random.randrange(4, 6, 1)
    nr_numbers = random.randrange(4, 6, 1)

    password_result_label.config(text="0")

    for letter in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for symbol in range(1, nr_symbols + 1):
        password_list.append(random.choice(symbols))

    for number in range(1, nr_numbers + 1):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    for char in password_list:
        password += char
    password_result_label.config(text=f"{password}")
    window.clipboard_clear()
    window.clipboard_append(password)


window = Tk()
window.title("Welcome to the PyPassword Generator!")
window.config(padx=60, pady=40)

password_result_label = Label(text="0")
password_result_label.grid(column=1, row=2)

generate_button = Button(text="Generate password and copy to clipboard", command=passwordgen)
generate_button.grid(column=1, row=1)

window.mainloop()
