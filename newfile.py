import tkinter as tk
from tkinter import messagebox

def activate_product():
  
  key = key_entry.get()
  if key == "12345":
    messagebox.showinfo("Активация успешна", "Продукт успешно активирован!")
  else:
    messagebox.showerror("Ошибка активации", "Неверный ключ продукта, попробуйте еще раз.")

def show_activation_window():
  
  
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

root = tk.Tk()
root.geometry("300x200")
root.title("Windows ")

menu_bar = tk.Menu(root)

start_menu = tk.Menu(menu_bar, tearoff=0)
start_menu.add_command(label="Завершение работы", command=root.quit)

start_menu.add_command(label="Файлы")
start_menu.add_command(label="Настройки")
start_menu.add_command(label="Активация", command=show_activation_window) 

menu_bar.add_cascade(label="Пуск", menu=start_menu) 

root.config(menu=menu_bar) 

label = tk.Label(root, text="Привет, Юзер")
label.pack(pady=50)

root.mainloop()