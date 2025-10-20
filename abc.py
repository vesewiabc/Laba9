import tkinter as tk
from tkinter import messagebox
import os
import sys

class Calculator:
    def __init__(self):
        # Создание главного окна
        self.window = tk.Tk()
        self.window.title("Кроссплатформенный калькулятор")  # Заголовок окна
        self.window.geometry("300x400")  # Размер окна
        self.window.resizable(False, False)  # Запрет изменения размера
        
        # Переменная для хранения текущего выражения
        self.expression = ""
        
        # Создание элементов интерфейса
        self.create_widgets()
        
        # Логирование информации о платформе (для отладки)
        self.log_platform_info()
    
    def log_platform_info(self):
        """Логирование информации о платформе для отладки"""
        log_dir = os.path.join(os.path.expanduser("~"), "calculator_logs")
        os.makedirs(log_dir, exist_ok=True)  # Создание директории если не существует
        
        log_file = os.path.join(log_dir, "platform_info.txt")
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"Платформа: {sys.platform}\n")
            f.write(f"Версия Python: {sys.version}\n")
            f.write(f"Путь к исполняемому файлу: {sys.executable}\n")
    
    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Поле для отображения выражения
        self.display = tk.Entry(
            self.window, 
            font=("Arial", 18), 
            justify="right", 
            state="readonly",
            width=15
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)
        
        # Кнопки калькулятора
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        
        # Расположение кнопок на сетке
        row = 1
        col = 0
        for button in buttons:
            # Определение специальных стилей для разных типов кнопок
            if button == '=':
                bg_color = "orange"
            elif button == 'C':
                bg_color = "red"
            elif button in ['/', '*', '-', '+']:
                bg_color = "blue"
            else:
                bg_color = "gray"
            
            # Создание кнопки
            tk.Button(
                self.window, 
                text=button, 
                font=("Arial", 14),
                bg=bg_color,
                command=lambda b=button: self.button_click(b),
                width=5, 
                height=2
            ).grid(row=row, column=col, padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def button_click(self, value):
        """Обработка нажатия кнопок"""
        try:
            if value == '=':
                # Вычисление результата
                result = str(eval(self.expression))
                self.expression = result
            elif value == 'C':
                # Очистка
                self.expression = ""
            else:
                # Добавление символа к выражению
                self.expression += str(value)
            
            # Обновление дисплея
            self.update_display()
            
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
            self.expression = ""
            self.update_display()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Некорректное выражение: {e}")
            self.expression = ""
            self.update_display()
    
    def update_display(self):
        """Обновление текста на дисплее"""
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        self.display.config(state="readonly")
    
    def run(self):
        """Запуск приложения"""
        self.window.mainloop()

# Точка входа в приложение
if __name__ == "__main__":
    # Создание и запуск калькулятора
    app = Calculator()
    app.run()
