'''
Напишіть модуль, який допоможе Вам у математичних задачах, 
де потрібно знайти площу і периметр прямокутника.

На олімпіаді з математики виграє той, хто швидше за всіх вирішить завдання.
В одному із завдань потрібно знайти площу і периметр прямокутника. 
Давайте напишемо програму, яка буде містити дві функції: 
area () - повертає площу прямокутника, 
perimeter () - повертає периметр прямокутника.
Напишіть програму і збережіть її як модуль, 
який допоможе Вам у наступному завданні.
'''

# Напиши функцію perimeter () для обчислення периметра

def perimeter(length, width):
    return 2 * (length + width)
# Напиши функцію area () для обчислення площі
def area(length, width):
    return length * width