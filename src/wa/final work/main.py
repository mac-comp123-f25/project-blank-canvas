import tkinter as tk
import math
import os

# --- 文本和翻译库 (无变动) ---
TEXTS = {
    'title': {'en': "pomodoro", 'zh': "番茄钟", 'es': "pomodoro"},
    'start': {'en': "start", 'zh': "开始", 'es': "iniciar"},
    'reset': {'en': "reset", 'zh': "重置", 'es': "reiniciar"},
    'work': {'en': "work", 'zh': "工作", 'es': "trabajo"},
    'short_break': {'en': "short break", 'zh': "短暂休息", 'es': "descanso corto"},
    'long_break': {'en': "long break", 'zh': "长时间休息", 'es': "descanso largo"}
}

current_language = 'en'

# --- 代码常量 (无变动) ---
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# --- 函数定义 ---
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text=TEXTS['long_break'][current_language], fg="#0077ff")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text=TEXTS['short_break'][current_language], fg="#00bb77")
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text=TEXTS['work'][current_language], fg="#ff5555")


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    # --- 修改: 更新 timer_label 的文本 ---
    timer_label.config(text=f"{minutes}:{seconds}")

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
    if timer:
        window.after_cancel(timer)

    # --- 修改: 重置 timer_label 的文本 ---
    timer_label.config(text="00:00")

    title_label.config(text=TEXTS['title'][current_language])
    checkmark_label.config(text="")
    reps = 0


def set_language(lang_code):
    global current_language
    current_language = lang_code

    window.title(TEXTS['title'][current_language])
    start_button.config(text=TEXTS['start'][current_language])
    reset_button.config(text=TEXTS['reset'][current_language])

    if reps == 0:
        title_label.config(text=TEXTS['title'][current_language])


# --- UI 界面设置 ---
window = tk.Tk()
window.title(TEXTS['title'][current_language])
window.config(padx=50, pady=25)

# --- 设置背景图片 (无变动) ---
script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, "background.GIF")

background_image = tk.PhotoImage(file=image_path)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = background_image
background_label.lower()

# --- UI 控件 ---
title_label = tk.Label(text=TEXTS['title'][current_language], fg="#d13a30", font=("Helvetica", 35))
title_label.pack()

# --- 关键修改: 使用 Label 代替 Canvas 来显示时间 ---
# Label 会自动调整大小以适应文本, 从而最大限度地减少 "遮挡"
timer_label = tk.Label(text="00:00", fg="#333333", font=("Helvetica", 35, "bold"))
timer_label.pack()

# (原有的 Canvas 代码已被完全删除)

start_button = tk.Button(text=TEXTS['start'][current_language], command=start_timer, font=("Helvetica", 14))
start_button.pack(pady=5)

reset_button = tk.Button(text=TEXTS['reset'][current_language], command=reset_timer, font=("Helvetica", 14))
reset_button.pack(pady=5)

checkmark_label = tk.Label(fg="#00aa55", font=("Helvetica", 20))
checkmark_label.pack(pady=5)

lang_frame = tk.Frame(window)
lang_frame.pack(pady=10)

english_button = tk.Button(lang_frame, text="English", font=("Helvetica", 10), command=lambda: set_language('en'))
english_button.pack(side="left", padx=5)

chinese_button = tk.Button(lang_frame, text="中文", font=("Helvetica", 10), command=lambda: set_language('zh'))
chinese_button.pack(side="left", padx=5)

spanish_button = tk.Button(lang_frame, text="Español", font=("Helvetica", 10), command=lambda: set_language('es'))
spanish_button.pack(side="left", padx=5)

window.mainloop()