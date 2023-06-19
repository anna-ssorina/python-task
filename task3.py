#Ссорина Анна сергеевна 44-22-119 Вариант 20

import math
import tkinter as tk
from tkinter import messagebox

def calculate_expression(x):
    if isinstance(x, (int, float)):
        if x < 0.5:
            return math.sqrt(math.sin(x) + math.cos(x)**2)
        else:
            return math.exp(x**3) * math.sin(3*x)
    else:
        raise ValueError("Введенное значение не является числом")

def calculate_button_clicked():
    try:
        x = float(entry.get())
        result = calculate_expression(x)
        messagebox.showinfo("Результат", f"Результат вычисления: {result}")
    except ValueError as ve:
        messagebox.showerror("Ошибка", str(ve))

window = tk.Tk()
window.title("Вычисление выражения")
window.geometry("300x150")  # Установка размеров окна

label = tk.Label(window, text="Введите значение x:")
label.pack()

entry = tk.Entry(window)
entry.pack()

calculate_button = tk.Button(window, text="Вычислить", command=calculate_button_clicked)
calculate_button.pack()

window.mainloop()

