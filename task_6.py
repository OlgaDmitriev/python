"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""

try:
    NUMBER = int(input("Введите номер символа: "))
    NUMBER = int(ord('a')) + NUMBER - 1
    B = chr(NUMBER)
    print(f'Введенному номеру соответствует символ {B}')
except ValueError:
    print('Пожалуйста, введите число.')
