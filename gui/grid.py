import tkinter as tk

root = tk.Tk()

root.title("Geometry Managers Example")

root.geometry("400x300") # Width x Height


label1 = tk.Label(root, text="Label 1")

label1.grid(row=0, column=0) # Row 0, Column 0

label2 = tk.Label(root, text="Label 2")

label2.grid(row=0, column=1) # Row 0, Column 1

button = tk.Button(root, text="Click Me")

button.grid(row=1, columnspan=2) # Spans across two columns

root.mainloop()
