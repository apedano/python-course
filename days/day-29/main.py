import random
import string
from tkinter import END
import tkinter as tk
import tkinter.messagebox as messagebox


JOINER = " | "
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
NUMBERS = "0123456789"
CAPITAL_LETTERS = string.ascii_uppercase
PASSWORD_LENGTH = 20
PASSWORD_ELEMENTS = [SPECIAL_CHARACTERS, NUMBERS, CAPITAL_LETTERS]

password_store = []

password_store_record = {"ws":"sodiaj", "user-email":"sakudhsaiudh", "password":"soijdasio"}
password_store.append(password_store_record)

main_window = tk.Tk()
main_window.title("Password manager")

with open("password_store.txt", "a") as f:
    pass

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    generates_password = ""
    for i in range(PASSWORD_LENGTH):
        ELEMENT = random.choice(PASSWORD_ELEMENTS)
        generates_password += random.choice(ELEMENT)
    return generates_password

def copy_to_clipboard(text: str):
    main_window.clipboard_clear()
    main_window.clipboard_append(text)

def handle_generate_password():
    psw = generate_password()
    copy_to_clipboard(str(psw))
    input_psw.insert(0, psw)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def reset_controls():
    input_ws.delete(0, END)
    input_user.delete(0, END)
    input_psw.delete(0, END)

def validate_input(values: list[str]):
    for input in values:
        if len(input) == 0:
            messagebox.showerror("Error", "Please make sure all values are entered")
            return False
    return True

def handle_add_password():
    inserted_values = [input_ws.get(), input_user.get(), input_psw.get()]
    if validate_input(inserted_values):
        answer = messagebox.askokcancel("Confirm", "Do you want to save the password?")
        if answer:
            with open("password_store.txt", "a") as f:
                f.write(JOINER.join(inserted_values))
                f.write("\n")
            reset_controls()

    # ---------------------------- UI SETUP ------------------------------- #




main_window.config(padx=20, pady=20)

canvas_width=200
canvas_height=189
center_x = int(canvas_width / 2)
center_y = int((canvas_height / 2))

# --- LOGO ---- #
canvas = tk.Canvas(width=canvas_width, height=canvas_height, highlightthickness=0)
logo=tk.PhotoImage(file="logo.png")
canvas.create_image(center_x, center_y, image=logo)
canvas.grid(row=0, column=2) #of 5 colums

# --- WEBSITE label and input --- #
label_ws=tk.Label(main_window, text="Website")
label_ws.grid(row=1, column=0, sticky="w")
input_ws= tk.Entry(main_window, width=40)
input_ws.grid(row=1, column=1, columnspan=3, sticky="w")
input_ws.focus()

# --- Email/User label and input --- #
label_user=tk.Label(main_window, text="Email/Username")
label_user.grid(row=2, column=0, sticky="w")
input_user= tk.Entry(main_window, width=40)
input_user.insert(0, "my_email@domain.com")
input_user.grid(row=2, column=1, columnspan=3, sticky="w")

# --- Password label and input --- #
label_psw=tk.Label(main_window, text="Paasword")
label_psw.grid(row=3, column=0, sticky="w")
input_psw= tk.Entry(main_window, width=30)
input_psw.grid(row=3, column=1, columnspan=2, sticky="w")
button_gen_pws = tk.Button(main_window, text="Generate", command=handle_generate_password)
button_gen_pws.grid(row=3, column=3, sticky="w")

# --- Add button --- #
button_gen_pws = tk.Button(main_window, text="Add", width=50, command=handle_add_password)
button_gen_pws.grid(row=4, column=0, columnspan=4)





main_window.mainloop()