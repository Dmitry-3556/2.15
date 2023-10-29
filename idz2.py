#!/usr/bin/env python 3
# –*– coding: utf–8 –*–

import sys

# Функция для чтения слов из словаря
def load_dictionary(dictionary_file):
    with open(dictionary_file, "r", encoding="utf-8") as file:
        dictionary = set(word.strip().lower() for word in file)
    return dictionary

# Функция для проверки орфографии
def spell_check(text, dictionary):
    incorrect_words = []
    words = text.split()
    for word in words:
        word = word.strip(".,!?\"':;-").lower()
        if word and word not in dictionary:
            incorrect_words.append(word)
    return incorrect_words

# Проверяем наличие аргумента командной строки (пути к файлу)
if len(sys.argv) != 2:
    print("Пожалуйста, укажите имя файла для проверки орфографии.")
else:
    file_name = sys.argv[1]
    try:
        # Загружаем словарь и текст из файла
        dictionary = load_dictionary("slovar.txt")
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()

        # Выполняем проверку орфографии и выводим результат
        incorrect_words = spell_check(text, dictionary)
        if incorrect_words:
            print("Неправильно написанные слова:")
            for word in incorrect_words:
                print(word)
        else:
            print("Орфографические ошибки не найдены.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")