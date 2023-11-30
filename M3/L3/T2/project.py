import random

def welcome():
    print("Ласкаво просимо до гри 'Вгадай число'!")
    print("Я загадаю число від 1 до 100. Ваше завдання - вгадати його.")

def generate_number():
    return random.randint(1, 100)

def play_game(secret_number):
    attempts = 0
    
    while True:
        guess = int(input("Введіть ваш варіант відповіді: "))
        attempts += 1

        if guess == secret_number:
            print(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб.")
            break
        elif guess < secret_number:
            print("Загадане число більше. Спробуйте ще раз.")
        else:
            print("Загадане число менше. Спробуйте ще раз.")

if __name__ == "__main__":
    welcome()
    secret_number = generate_number()
    play_game(secret_number)
