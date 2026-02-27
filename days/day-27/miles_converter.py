import tkinter as tk

FONT = ("Verdana", 12)

root = tk.Tk()

root.config(padx=20, pady=20)
root.title("Miles Converter")

root.geometry("300x120")

input= tk.Entry(root, width=10, font=FONT)

input.grid(row=0, column=2)

label_miles = tk.Label(root, text="Miles", font=FONT)

label_miles.grid(row=0, column=3)

label_equals = tk.Label(root, text="is equal to", font=FONT)
label_equals.grid(row=1, column=1)

label_ml = tk.Label(root, text="", font=("Courier", 12, "bold"))
label_ml.grid(row=1, column=3)
label_ml.grid(row=1, column=3)
label_ml.grid(row=1, column=2)


label_km = tk.Label(root, text="Km", font=FONT)
label_km.grid(row=1, column=3)


def on_click():
    miles = float(input.get())
    miles = miles * 1.60934
    label_ml.config(text=miles)

button = tk.Button(root, text="Convert", command=on_click, font=("Courier", 15))
button.grid(row=2, column=2) # Spans across two columns



root.mainloop()