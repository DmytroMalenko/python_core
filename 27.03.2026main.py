from console_ui import draw_header, draw_menu, draw_warning

draw_header("СУПЕР ГРА 2026")

menu = ["Нова гра", "Завантажити", "Вихід"]
draw_menu(menu)

print("-" * 40)
choice = input("Введи номер: ")

if choice not in ["1", "2", "3"]:
    draw_warning("Помилка!")



























