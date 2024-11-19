import tkinter as tk
from tkinter import messagebox

def check_triangle():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        if a <= 0 or b <= 0 or c <= 0:
            messagebox.showerror("Ошибка", "Стороны должны быть положительными целыми числами.")
            return

        # Проверка на существование треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            messagebox.showerror("Ошибка", "С указанными сторонами треугольник не может существовать.")
            return

        triangle_type = ""
        if a == b == c:
            triangle_type = "равносторонний"
        elif a == b or b == c or a == c:
            triangle_type = "равнобедренный"
        else:
            triangle_type = "разносторонний"

        # Проверка на прямоугольный треугольник
        sides = [a, b, c]
        sides.sort()
        if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
            triangle_type = "прямоугольный"
        elif sides[2] ** 2 > sides[0] ** 2 + sides[1] ** 2:
            triangle_type = "тупоугольный"
        elif sides[2] ** 2 < sides[0] ** 2 + sides[1] ** 2:
            triangle_type = "остроугольный"

        messagebox.showinfo("Результат", f"Треугольник является {triangle_type}.")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа.")

#Создание основного окна
root = tk.Tk()
root.title("Определение типа треугольника")
root.geometry("1920x1080")
root.configure(bg="#FFFFFF")

#Создание рамки для ввода данных
frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
frame.pack(padx=20, pady=20)
#Заголовок
label_title = tk.Label(frame, text="Введите стороны треугольника", font=("Times New Roman", 14), bg="#6A5ACD")
label_title.pack(pady=10)

#Создание полей ввода
label_a = tk.Label(frame, text="Сторона A:", font=("Times New Roman", 14), bg="#ffffff")
label_a.pack(anchor='w')
entry_a = tk.Entry(frame, font=("Times New Roman", 14))
entry_a.pack(pady=5)

label_b = tk.Label(frame, text="Сторона B:", font=("Times New Roman", 14), bg="#ffffff")
label_b.pack(anchor='w')
entry_b = tk.Entry(frame, font=("Times New Roman", 14))
entry_b.pack(pady=5)

label_c = tk.Label(frame, text="Сторона C:", font=("Times New Roman", 14), bg="#ffffff")
label_c.pack(anchor='w')
entry_c = tk.Entry(frame, font=("Arial", 14))
entry_c.pack(pady=5)

#Кнопка проверки
check_button = tk.Button(root, text="Проверить", command=check_triangle, font=("Arial", 12), bg="#4B0082", fg="white")
check_button.pack(pady=10)

#Запуск основного цикла
root.mainloop()

