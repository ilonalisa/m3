# olympic.py

def run(distance, time):
    """
    Функція для розрахунку швидкості спортсмена.
    Приймає відстань (у кілометрах) та час (у годинах).
    Повертає швидкість (у км/год).
    """
    if time == 0:
        return "Час не може бути рівним нулю. Визначте коректний час."
    
    speed = distance / time
    return speed

if __name__ == "__main__":
    # Приклад використання модуля
    input_distance = float(input("Введіть відстань у кілометрах: "))
    input_time = float(input("Введіть час у годинах: "))

    result_speed = run(input_distance, input_time)
    print(f"Швидкість спортсмена: {result_speed:.2f} км/год.")
