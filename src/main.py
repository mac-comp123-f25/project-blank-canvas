import tkinter as tk
import math

# --- 字体和颜色常量 (新增) ---
# 将字体和颜色统一定义，方便修改
FONT_CUTE = "Comic Sans MS"
COLOR_BG = "#f7f5dd"  # 用作所有组件的背景色，形成一个面板效果

# --- 原有代码，未作修改 ---
TEXTS = {
    'title': {'en': "pomodoro", 'zh': "番茄钟", 'es': "pomodoro"},
    'start': {'en': "start", 'zh': "开始", 'es': "iniciar"},
    'reset': {'en': "reset", 'zh': "重置", 'es': "reiniciar"},
    'work': {'en': "work", 'zh': "工作", 'es': "trabajo"},
    'short_break': {'en': "short break", 'zh': "短暂休息", 'es': "descanso corto"},
    'long_break': {'en': "long break", 'zh': "长时间休息", 'es': "descanso largo"}
}

current_language = 'en'

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
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
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
# 注意：这里不再设置窗口的bg，因为会被背景图覆盖
window.config(padx=50, pady=25)

# --- 新增: 添加背景图片 ---
# 使用 try-except 块，如果找不到图片文件，程序仍能正常运行
try:
    # 加载图片
    # 将图片对象存储为窗口的一个属性，以防止它被Python的垃圾回收机制清除
    window.bg_image = tk.PhotoImage(file="background.gif")

    # 创建一个标签用于显示背景图
    background_label = tk.Label(window, image=window.bg_image)

    # 使用place将背景标签放置在窗口底层并填满整个窗口
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except tk.TclError:
    # 如果图片加载失败 (例如文件不存在), 打印提示信息并使用备用背景色
    print("Warning: 'background.gif' not found. Using solid color background.")
    window.config(bg=COLOR_BG)

# --- 修改: 更新所有组件的字体和背景色 ---
# 所有组件都使用 COLOR_BG 作为背景色，这样它们会像一个整体面板浮动在背景图上

title_label = tk.Label(text=TEXTS['title'][current_language], fg="#d13a30", bg=COLOR_BG, font=(FONT_CUTE, 40, "italic"))
title_label.pack()

# 让Canvas也使用面板背景色
canvas = tk.Canvas(width=200, height=120, bg=COLOR_BG, highlightthickness=0)
timer_text = canvas.create_text(100, 60, text="00:00", fill="#333333", font=(FONT_CUTE, 35, "bold"))
canvas.pack()

# highlightbackground 用于设置按钮边框外的颜色，使其与面板融合
start_button = tk.Button(text=TEXTS['start'][current_language], command=start_timer, font=(FONT_CUTE, 14),
                         highlightbackground=COLOR_BG)
start_button.pack(pady=5)

reset_button = tk.Button(text=TEXTS['reset'][current_language], command=reset_timer, font=(FONT_CUTE, 14),
                         highlightbackground=COLOR_BG)
reset_button.pack(pady=5)

checkmark_label = tk.Label(fg="#00aa55", bg=COLOR_BG, font=(FONT_CUTE, 20, "bold"))
checkmark_label.pack(pady=5)

lang_frame = tk.Frame(window, bg=COLOR_BG)
lang_frame.pack(pady=10)

english_button = tk.Button(lang_frame, text="English", font=(FONT_CUTE, 10), command=lambda: set_language('en'),
                           highlightbackground=COLOR_BG)
english_button.pack(side="left", padx=5)

chinese_button = tk.Button(lang_frame, text="中文", font=(FONT_CUTE, 10), command=lambda: set_language('zh'),
                           highlightbackground=COLOR_BG)
chinese_button.pack(side="left", padx=5)

spanish_button = tk.Button(lang_frame, text="Español", font=(FONT_CUTE, 10), command=lambda: set_language('es'),
                           highlightbackground=COLOR_BG)
spanish_button.pack(side="left", padx=5)

window.mainloop()
