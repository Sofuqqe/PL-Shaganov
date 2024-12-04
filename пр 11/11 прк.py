import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error: Деление на ноль"
            else:
                result = num1 / num2
        else:
            result = "Error: Недопустимая операция"

        result_label.config(text=f"Результат: {result}")

    except ValueError:
        result_label.config(text="Error: Неверный ввод")

def show_checkbox_result():
    result = ""
    if var1.get():
        result += "Первый вариант, "
    if var2.get():
        result += "Второй вариант, "
    if var3.get():
        result += "Третий вариант."
    messagebox.showinfo("Результаты чекбоксов", result)


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:  # Обрабатывать кодировку для различных текстовых файлов
                text = f.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, text)

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
        except Exception as e: #Добавление универсального обработчика исключений - всегда хорошая идея.
            messagebox.showerror("Error", f"An error occurred: {e}")

# --- GUI  ---
root = tk.Tk()
root.title("Шаганов Кирилл Александрович") 
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# --- 1: калькулятор ---
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Калькулятор")

entry1 = tk.Entry(tab1)
entry1.pack()
entry2 = tk.Entry(tab1)
entry2.pack()

operation_var = tk.StringVar(tab1)
operation_var.set("+") # значение по умолчанию
options = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(tab1, operation_var, *options)
operation_menu.pack()

calculate_button = tk.Button(tab1, text="Калькулятр", command=calculate)
calculate_button.pack()
result_label = tk.Label(tab1, text="результат:")
result_label.pack()

# --- Tab 2: чексбокесы ---
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Чекбоксы")

var1 = tk.BooleanVar()
check1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
check1.pack()
var2 = tk.BooleanVar()
check2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
check2.pack()
var3 = tk.BooleanVar()
check3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
check3.pack()

checkbox_button = tk.Button(tab2, text="Показать результат", command=show_checkbox_result)
checkbox_button.pack()


# --- Tab 3: Текстовой редактор ---
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Текстовый редактор")

text_area = tk.Text(tab3)
text_area.pack(expand=True, fill="both")

open_button = tk.Button(tab3, text="Откройте файл", command=open_file)
open_button.pack()

root.mainloop()