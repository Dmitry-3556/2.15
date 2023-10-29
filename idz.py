#!/usr/bin/env python 3
# –*– coding: utf–8 –*–

# Функция для проверки, является ли буква гласной
def is_vowel(letter):
    vowels = "AEIOUaeiou"
    return letter in vowels

# Функция для замены первой буквы слова на прописную, если слово начинается с гласной
def capitalize_vowels(word):
    if len(word) > 0 and is_vowel(word[0]):
        return word[0].upper() + word[1:]
    else:
        return word

# Считываем текст из файла
file_name = "file.txt"  # Замените "your_text_file.txt" на путь к вашему файлу

with open(file_name, "r") as file:
    text = file.read()

# Разбиваем текст на слова, заменяем первую букву на прописную при необходимости
words = text.split()
capitalized_words = [capitalize_vowels(word) for word in words]

# Выводим текст с изменениями на экран
capitalized_text = " ".join(capitalized_words)
print(capitalized_text)