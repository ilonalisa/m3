# birthday.py

def determine_season(month):
    """
    Визначає пору року на основі номера місяця.
    """
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if month in spring:
        return "Весна"
    elif month in summer:
        return "Літо"
    elif month in autumn:
        return "Осінь"
    else:
        return "Зима"

def determine_day_of_week(day):
    """
    Визначає день тижня на основі номера дня.
    """
    days_of_week = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    return days_of_week[day % 7]

if __name__ == "__main__":
    # Приклад використання модуля
    birth_month = int(input("Введіть номер місяця, в якому ви народилися: "))
    birth_day = int(input("Введіть номер дня місяця, в якому ви народилися: "))

    season = determine_season(birth_month)
    day_of_week = determine_day_of_week(birth_day)

    print(f"Ви народились в {season} у {day_of_week}.")
