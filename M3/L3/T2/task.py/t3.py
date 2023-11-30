import random

secret_number = random.randint(1, 99)

while True:
    guess = int(input("Введіть свою догадку (від 1 до 99): "))

    if guess == secret_number:
        print("Добре вгадано!")
        break
    else:
        print("Неправильно. Спробуйте знову.")
