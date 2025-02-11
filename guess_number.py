# Игра: Угадай число
#
# Используя модуль `random`, напишите программу,
# которая случайным образом выбирает число от 0 до 100.
# У пользователя есть 6 попыток, чтобы угадать это число.
# Если пользователь угадывает число,
# выводится сообщение об успехе:
# "Отлично! Вы угадали число … с … попытки!".
# Если не угадывает за 6 попыток,
# выводится сообщение о неудаче:
# “К сожалению, вы не угадали число. Загаданное число было: …”.
#
# В конце программы должны выводиться
# все попытки пользователя и загаданное число.
#
# По ходу игры после каждой попытки
# пользователя компьютер выводит сообщение,
# было ли число пользователя
# больше или меньше загаданного числа:
# "Загаданное число больше.", "Загаданное число меньше."
# соответственно.
import random
def guess_number():
    secret_number = random.randint(1,100)
    attempts = 6
    user_atempts = []
    print("Начинаем игру Угадай число с шести попыток")
    print("я придумаю число от 1 до 100, а твоя задача его угадать")
    input("Готов? Нажми любую Enter ")


    for atempt in range (1, 7):
        print(f'Попытка: {atempt}')
        guess = (int(input("введите целое число от 1 до 100: ")))
        user_atempts.append(guess)
        if guess == secret_number:
            print(f"Верно, это действительно {secret_number}")
            print(f"вы угадали с {guess} попытки")
            print(f"я в шоке от твоей интуиции")
        elif guess < secret_number:
            print( f"задуманное число больше чем {guess}")
        elif guess > secret_number:
            print(f"задуманное число меньше чем {guess}")
    else:
        print(f"Среди чисел: {user_atempts} нет числа: {secret_number}")



guess_number()
