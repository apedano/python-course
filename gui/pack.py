import tkinter as tk

root = tk.Tk()

root.title("Geometry Managers Example")

root.geometry("400x300") # Width x Height


label1 = tk.Label(root, text="Label 1")

label1.pack() # This will be placed at the top by default

label2 = tk.Label(root, text="Label 2")

label2.pack(pady=10) # This will be placed below Label 1

button = tk.Button(root, text="Click Me")

button.pack(pady=10) # This will be placed below Label 2

root.mainloop()