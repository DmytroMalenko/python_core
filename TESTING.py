
def is_palindrome(number) -> bool:
    # Зберігаємо оригінал
    original = number
    
    # Робимо додатним
    if number < 0:
        number = -number
    
    # Перевертаємо число
    reversed_num = 0
    while number > 0:
        digit = number % 10           # Остання цифра
        reversed_num = reversed_num * 10 + digit  # Додаємо спереду
        number = number // 10         # Видаляємо останню цифру
    
    # Порівнюємо
    return original == reversed_num

# Тестуємо твої приклади:
print(is_palindrome(123321))  # True
print(is_palindrome(546645))  # True
print(is_palindrome(421987))  # False
