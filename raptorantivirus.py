import customtkinter as ctk
import psutil
import os
import subprocess
import random
from datetime import datetime
import tkinter as tk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class TetrisGame(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Tetris - @markgod Edition")
        self.geometry("300x600")
        self.canvas = tk.Canvas(self, width=300, height=600, bg="black")
        self.canvas.pack()
        self.label = ctk.CTkLabel(self, text="Управление: Стрелки", font=("Arial", 12))
        self.label.pack()
        # Простая имитация игры: рисуем падающий квадрат
        self.y = 0
        self.draw_block()

    def draw_block(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(120, self.y, 180, self.y + 60, fill="red")
        self.y += 20
        if self.y > 540: self.y = 0
        self.after(100, self.draw_block)

class AnalysisWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("System Guard Pro")
        self.geometry("500x800")
        
        self.status_label = ctk.CTkLabel(self, text="ВЫПОЛНЯЕТСЯ АНАЛИЗ...", font=("Arial", 20, "bold"))
        self.status_label.pack(pady=10)
        
        self.info_label = ctk.CTkLabel(self, text="", font=("Consolas", 14))
        self.info_label.pack(pady=10)

        ctk.CTkButton(self, text="ЗАЩИТА ОТ ВИРУСОВ", fg_color="red", command=self.activate_defense).pack(pady=5)
        ctk.CTkButton(self, text="ОБОЙТИ ВИРУС (TaskMgr)", fg_color="green", command=lambda: os.system("start taskmgr")).pack(pady=5)
        ctk.CTkButton(self, text="СИСТЕМА", command=lambda: os.system("start ms-settings:about")).pack(pady=5)
        ctk.CTkButton(self, text="ИГРА (ТЕТРИС)", fg_color="purple", command=lambda: TetrisGame()).pack(pady=5)
        ctk.CTkButton(self, text="ДОПОЛНИТЕЛЬНО", command=lambda: self.info_label.configure(text="Для выхода: Enter + F10")).pack(pady=5)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=400, height=250)
        self.scrollable_frame.pack(pady=10, fill="both", expand=True)

        ctk.CTkLabel(self, text="Автор: @markgod", font=("Arial", 10), text_color="gray").pack(side="bottom", pady=5)
        self.update_all()

    def update_all(self):
        text = f"CPU: {psutil.cpu_percent()}% | RAM: {psutil.virtual_memory().percent}% | GPU: {random.randint(15, 30)}%"
        self.info_label.configure(text=text)
        for widget in self.scrollable_frame.winfo_children(): widget.destroy()
        for proc in list(psutil.process_iter(['name', 'pid']))[-20:]:
            ctk.CTkButton(self.scrollable_frame, text=f"{proc.info['name']} (PID: {proc.info['pid']})", 
                          fg_color="#333333", height=25, command=lambda p=proc: p.terminate()).pack(fill="x", pady=2)
        self.after(3000, self.update_all)

    def activate_defense(self):
        subprocess.Popen('start cmd /k "echo Сканирование... && ping 127.0.0.1 -n 3 && exit"', shell=True)

if __name__ == "__main__":
    app = ctk.CTk()
    app.withdraw()
    AnalysisWindow().mainloop()