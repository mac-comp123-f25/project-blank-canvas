import tkinter as tk
import math

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

reps = 0
timer = None

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="long break", fg="#0077ff")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="short break", fg="#00bb77")
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="work", fg="#ff5555")


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="pomodoro")
    checkmark_label.config(text="")
    reps = 0


window = tk.Tk()
window.title("pomodoro")
window.config(padx=50, pady=25, bg="#f7f5dd")

title_label = tk.Label(text="pomodoro", fg="#d13a30", bg="#f7f5dd", font=("Helvetica", 35))
title_label.pack()

canvas = tk.Canvas(width=200, height=120, bg="#f7f5dd", highlightthickness=0)
timer_text = canvas.create_text(100, 60, text="00:00", fill="#333333", font=("Helvetica", 35, "bold"))
canvas.pack()

start_button = tk.Button(text="start", command=start_timer, font=("Helvetica", 14))
start_button.pack(pady=5)

reset_button = tk.Button(text="reset", command=reset_timer, font=("Helvetica", 14))
reset_button.pack(pady=5)

checkmark_label = tk.Label(fg="#00aa55", bg="#f7f5dd", font=("Helvetica", 20))
checkmark_label.pack(pady=5)

window.mainloop()