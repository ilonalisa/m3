'''
Давайте допоможемо фізикам перевести час в секунди!

Коли вчені-фізики виконують експеримент, 
витрачений на нього час вимірюється в секундах, 
навіть якщо дослід тривав більше декількох годин. 
Давайте полегшимо життя фізикам і напишемо програму, 
яка буде переводити витрачені години та хвилини в секунди.

Користувач вводить два числа: 
h - кількість годин і m - кількість хвилин.

Підключіть модуль my_time з попереднього завдання,
використовуйте функції переведення часу в секунди.

Виведіть витрачений час в секундах.
'''
import my_time
# Підключи модуль з попереднього завдання

h = int(input("Введіть кількість годин: "))
m = int(input("Введіть кількість хвилин: "))

minutes = int(my_time.seconds_in_min(m))
hours = int(my_time.seconds_in_hour(h))
seconds = minutes + hours
print(seconds)