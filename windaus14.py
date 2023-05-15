#Конечно, вот код без использования файла json:

#```python
import tkinter as tk
from tkinter import messagebox

settings = {}

def activate_product():
  # Функция, которую вызывает кнопка "Активировать"
  key = key_entry.get()
  if key == "12345":
    messagebox.showinfo("Активация успешна", "Продукт успешно активирован!")
    settings["product_key"] = key
    save_settings()
  else:
    messagebox.showerror("Ошибка активации", "Неверный ключ продукта, попробуйте еще раз.")

def show_activation_window():
  # Функция для отображения окна активации
  activation_window = tk.Toplevel()
  activation_window.geometry("300x200")
  activation_window.title("Активация")

  key_label = tk.Label(activation_window, text="Введите ключ:")
  key_label.pack(pady=10)

  global key_entry
  key_entry = tk.Entry(activation_window)
  key_entry.pack(pady=10)

  activate_button = tk.Button(activation_window, text="Активировать", command=activate_product)
  activate_button.pack(pady=10)

  activation_window.mainloop()

def show_settings_window():
  # Функция для отображения окна настроек
  settings_window = tk.Toplevel()
  settings_window.geometry("300x200")
  settings_window.title("Настройки")

  product_activated_label = tk.Label(settings_window, text="Активация: ")
  product_activated_label.pack(pady=10)

  global product_activated_var
  product_activated_var = tk.StringVar(value="Нет")
  if "product_key" in settings:
    product_activated_var.set("Да")
  product_activated_entry = tk.Entry(settings_window, textvariable=product_activated_var, state="disabled")
  product_activated_entry.pack(pady=10)

  settings_window.mainloop()

def save_settings():
  # Функция для сохранения настроек
  with open("settings.txt", "w") as f:
    if "product_key" in settings:
      f.write(settings["product_key"])

def load_settings():
  # Функция для загрузки настроек
  global settings
  try:
    with open("settings.txt", "r") as f:
      settings["product_key"] = f.read().strip()
  except FileNotFoundError:
    pass

# Загружаем настройки
load_settings()

# Создание главного окна
root = tk.Tk()
root.geometry("300x200")
root.title("Windows ")

# Создание меню "Пуск"
menu_bar = tk.Menu(root)

start_menu = tk.Menu(menu_bar, tearoff=0)
start_menu.add_command(label="Завершение работы", command=root.quit)
start_menu.add_command(label="Файлы")
start_menu.add_command(label="Настройки", command=show_settings_window)
start_menu.add_command(label="Активация", command=show_activation_window)

menu_bar.add_cascade(label="Пуск", menu=start_menu)

root.config(menu=menu_bar)

label = tk.Label(root, text="Привет, пользователь!")
label.pack(pady=50)

root.mainloop()