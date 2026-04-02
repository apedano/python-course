import tkinter as tk

root = tk.Tk()

root.title("Geometry Managers Example")

root.geometry("400x300") # Width x Height

label1 = tk.Label(root, text="Label 1")

label1.place(x=50, y=50) # 50 pixels from the left and 50 pixels from the top

label2 = tk.Label(root, text="Label 2")

label2.place(x=150, y=50) # Positioned next to Label 1

button = tk.Button(root, text="Click Me")

button.place(x=100, y=100) # Placed at specific coordinates

root.mainloop()