import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Project Presentations")
root.geometry("400x200")

def open_english():
    webbrowser.open("https://www.youtube.com/watch?v=w-N68J6E938")

def open_mandarin():
    webbrowser.open("https://www.youtube.com/watch?v=1_kMT7EsG4g")

tk.Label(root, text="Presentation Recordings", font=("Arial", 18)).pack(pady=20)

tk.Button(root, text="🔵 English Version", font=("Arial", 14),
          command=open_english, width=25).pack(pady=10)

tk.Button(root, text="🟠 Mandarin Version", font=("Arial", 14),
          command=open_mandarin, width=25).pack(pady=10)

root.mainloop()
