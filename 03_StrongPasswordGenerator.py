import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

print('Привет, я генератор надежных паролей')
print('Сколько паролей тебе нужно?')
amount = int(input())  # количество паролей от пользователя
print('Какая длина пароля?')
length = int(input())  # длина пароля от пользователя
print('Включать ли цифры 0123456789?')
have_digit = int(input('Да - введи 1, Нет - введи 0'))  # нужны ли цифры
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
have_upper = int(input('Да - введи 1, Нет - введи 0'))  # нужны ли заглавные буквы
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
have_lower = int(input('Да - введи 1, Нет - введи 0'))  # нужны ли строчные буквы
print('Включать ли символы !#$%&*+-=?@^_?')
have_simbol = int(input('Да - введи 1, Нет - введи 0'))  # нужны ли символы
print('Исключать ли неоднозначные символы il1Lo0O?')
ambiguous = int(input('Да - введи 1, Нет - введи 0'))  # нужны ли необнозначные символы

if have_digit == 1:  # если в пароле нужны цифры
    chars += digits  # добавляем в строку chars цифры из строки digits
if have_upper == 1:  # если в пароле нужны заглавные буквы
    chars += uppercase_letters  # добавляем в строку chars большие буквы из строки uppercase_letters
if have_lower == 1:  # если в пароле нужны маленькие буквы
    chars += lowercase_letters  # добавляем в строку chars маленькие буквы из строки lowercase_letters
if have_simbol == 1:  # если в пароле нужны символы пунктуации
    chars += punctuation  # добавляем в строку chars символы из строки punctuation
if ambiguous == 1: # если в пароле нужно исключить неоднозначные символы
    for i in 'il1Lo0O':
        chars.replace(i, '') # удаляем их из строки chars методом замены на "пустоту"


def generate_password(length, chars): # функция для генерации пароля, принимает длину пароля и строку с символами
    for i in range(amount): # цикл для генерации необходимого количества паролей
        print(*random.sample(chars, length), sep='')


generate_password(length, chars)
