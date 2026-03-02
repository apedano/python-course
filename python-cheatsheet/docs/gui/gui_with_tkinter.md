# 🐍 Develop GUIs with Tkinter

[Sample](main.py)

## Create windows and labels

```python
import tkinter as tk

window = tk.Tk()

window.mainloop() #keeps the window open on screen
```

## The `Packer`

https://docs.python.org/3/library/tkinter.html#the-packer

It is a geometry management system for the elements to be added to a window

## Set config in GUI elements

https://docs.python.org/3/library/tkinter.html#handy-reference

```python
fred = Button(self, fg="red", bg="blue")
```

```python
fred["fg"] = "red"
fred["bg"] = "blue"
```

```python
fred.config(fg="red", bg="blue")
```

## Labels

https://www.tcl-lang.org/man/tcl8.6/TkCmd/label.htm

```python
my_label = tk.Label( text="I am a label", font=("Arial", 25, "bold") )

# my_label.pack()#automatically centered
my_label.pack(side="left")

my_label["text"]="New label"
```

## Buttons

https://www.tcl-lang.org/man/tcl8.6/TkCmd/button.htm

```python
def handle_click_button():
    my_label["text"]="My button is clicked"

my_button = tk.Button(text="Click me", command=handle_click_button)
my_button.pack()
```
The command can also be a lambda expression

```python
my_button = tk.Button(text="Click me", command=lambda: print("I am clicked"))
my_button.pack()
```

## Entry

https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm

For user input

```python
input= tk.Entry(width=40)

input.pack()

#gets the text in the input
input.get()
```

Set value

```python
#the index of insertion , can be END to append to the current value
input.insert(0, "my_inserted_text")
```
Delete the content

```python
#From the start to the END of the input indexes
input.delete(0, END)
```

## Dialog boxed

https://runestone.academy/ns/books/published/thinkcspy/GUIandEventDrivenProgramming/02_standard_dialog_boxes.html

```python
from tkinter import messagebox

messagebox.showinfo("Information","Informative message")
```

```python
answer = messagebox.askokcancel("Confirm", "Do you want to save the password?")
    if answer:
        inserted_values = [input_ws.get(), input_user.get(), input_psw.get()]
        ...
    else:
        print("User cancel")
```

## Other widgets

[other_widgets.py](other_widgets.py)

## Layout

```python
import tkinter as tk

root = tk.Tk()

root.title(“Geometry Managers Example”)

root.geometry(“400x300”) # Width x Height

root.mainloop()
```

### Pack

The pack manager organizes widgets in blocks before placing them in the parent widget. 

It’s simple to use and suitable for basic layouts.

https://www.tcl-lang.org/man/tcl8.6/TkCmd/pack.htm

[pack.py](pack.py)


🎯 Golden Rule of pack()

* If you want vertical stacking, use only side="top"

* If you want horizontal layout, use side="left"

* Mixing sides changes layout behavior

#### Key Points for pack:
* Use side option to specify placement (`TOP`, `BOTTOM`, `LEFT`, `RIGHT`).
* You can add padding using `padx` and `pady`.

### Grid

The grid manager organizes widgets in a table-like structure using rows and columns. 
It’s more flexible than pack for complex layouts.

https://www.tcl-lang.org/man/tcl8.6/TkCmd/grid.htm

[grid.py](grid.py)

Key Points for grid:
* Use row and column parameters to position widgets.
* Widgets can span multiple rows and columns using rowspan and columnspan.
* You can control padding with `padx` and `pady`.

### Place

The place manager allows you to specify the exact position of a widget using `x` and `y` coordinates. 
This gives you precise control over widget placement but is less flexible for responsive layouts.

https://www.tcl-lang.org/man/tcl8.6/TkCmd/place.htm

[place.py](place.py)

Key Points for place:
* Use x and y to specify exact positions.
* Suitable for fixed layouts, but not ideal for responsive designs.

### Combining Geometry Managers using `Frame`

You can use different geometry managers in the same application but not on the same parent widget. 
For instance, you could use pack for the main window and grid for a frame within that window.

https://www.tcl-lang.org/man/tcl8.6/TkCmd/frame.htm

[combined.py](combined.py)

    `root`
      |  
      | ->  `frame` (packed into root)
             |
             | ->   label1 → row=0, column=0
             | ->   label2 → row=0, column=1
             | ->   button → row=1, columnspan=2

```
+----------------------------------+
|                                  |
|   +--------------------------+   |
|   |  Label 1   |  Label 2    |   |
|   |--------------------------|   |
|   |        Click Me          |   |
|   +--------------------------+   |
|                                  |
+----------------------------------+
```

### Pomodoro timer

* combining layouts
* show images wiht `canvas`
* use of timers
* managing element within a parent (`Frame`)\

[main.py](tomato/main.py)