# time_conversion.py

def convert_to_seconds(hours, minutes):
    """
    Перетворює години і хвилини в секунди.
    """
    total_seconds = hours * 3600 + minutes * 60
    return total_seconds

if __name__ == "__main__":
    # Приклад використання модуля
    input_hours = int(input("Введіть кількість годин: "))
    input_minutes = int(input("Введіть кількість хвилин: "))

    seconds = convert_to_seconds(input_hours, input_minutes)
    print(f"{input_hours} годин і {input_minutes} хвилин - це {seconds} секунд.")
