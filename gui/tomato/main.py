
import tkinter as tk
from _curses import window
from tabnanny import filename_only

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECS_PER_MIN = 1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_clicked():
    global reps
    reps += 1
    if reps % 8 == 0:
        label_timer.config(text="Long break...", fg=RED)
        count_down(LONG_BREAK_MIN * SECS_PER_MIN)
    elif (reps % 8) % 2 == 1:
        label_tick = tk.Label(tick_frame, text="🗹", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        label_tick.pack(side="left")
        label_timer.config(text="Work session...", fg=GREEN)
        count_down(WORK_MIN * SECS_PER_MIN)
    else:
        label_timer.config(text="Short break...", fg=PINK)
        count_down(SHORT_BREAK_MIN * SECS_PER_MIN)


def reset_clicked():
    global reps, timer
    reps = 0
    if timer is not None:
        main_window.after_cancel(timer)
    for tick in tick_frame.winfo_children():
        tick.destroy()
    label_timer.config(text="Timer", fg=GREEN)
    # start_clicked()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #




# ---------------------------- UI SETUP ------------------------------- #

import math

main_window = tk.Tk()
main_window.title("Pomodoro timer")

# main_window.config(padx=100, pady=50, bg=YELLOW)
main_window.config(padx=100, pady=50, bg=YELLOW)


def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        #wait for an amount of time after that call a function with parameters as *args
        timer = main_window.after(500, count_down, count - 1)
    else:
        start_clicked()

### Canvas widget ###
#Layer elements one on top of the other
canvas_width=400
canvas_height=424
center_x = (canvas_width / 2)
center_y = (canvas_height / 2)
#add image
#highlightthickness removes a border around the image
canvas = tk.Canvas(width=canvas_width, height=canvas_height, bg=YELLOW, highlightthickness=0)
tomato_pi=tk.PhotoImage(file="tomato.png")
#x,y to the center of the window
canvas.create_image(center_x, center_y, image=tomato_pi)
timer_text = canvas.create_text(center_x, center_y+20, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)
label_timer=tk.Label(main_window,fg=GREEN, text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW)
label_timer.grid(row=0, column=1)


## Other elements


button_start = tk.Button(main_window, text="Start", command=start_clicked)
button_start.grid(row=2, column=0)

button_reset = tk.Button(main_window, text="Reset", command=reset_clicked)
button_reset.grid(row=2, column=2)



tick_frame = tk.Frame(main_window)
tick_frame.grid(row=3, column=1)
# label_tick = tk.Label(tick_frame, text="🗹", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
# label_tick.pack(side="left")
# label_tick2 = tk.Label(tick_frame, text="🗹", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
# label_tick2.pack(side="left")
# label_tick3 = tk.Label(tick_frame, text="🗹", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
# label_tick3.pack(side="left")



main_window.mainloop()

