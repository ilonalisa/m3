def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temperature = float(input("Введіть температуру в Цельсіях: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"Температура в Фаренгейтах: {fahrenheit_temperature}")
