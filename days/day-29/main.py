password_store = []

password_store_record = {"ws":"sodiaj", "user-email":"sakudhsaiudh", "password":"soijdasio"}
password_store.append(password_store_record)

with open("password_store.txt", "a") as f:
    f.write(password_store)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def handle_generate_password():
    pass

def handle_add_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

import tkinter as tk

main_window = tk.Tk()
main_window.title("Password manager")

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

# --- Email/User label and input --- #
label_user=tk.Label(main_window, text="Email/Username")
label_user.grid(row=2, column=0, sticky="w")
input_user= tk.Entry(main_window, width=40)
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