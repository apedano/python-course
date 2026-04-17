import tkinter as tk

root = tk.Tk()

root.title("Geometry Managers Example")

root.geometry("400x300") # Width x Height

frame = tk.Frame(root)

frame.pack()

label1 = tk.Label(frame, text="Label 1")

label1.grid(row=0, column=0)

label2 = tk.Label(frame, text="Label 2")

label2.grid(row=0, column=1)

button = tk.Button(frame, text="Click Me")

button.grid(row=1, columnspan=2)

root.mainloop()