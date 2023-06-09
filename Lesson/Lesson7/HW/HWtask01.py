# Задача 34:  Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “
# Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


s = input().split() # считываем стихи и разделяем по словам
syllables = [] # список для количества слогов в каждой фразе
for phrase in s:
    count = 0 # счетчик гласных в фразе
for letter in phrase:
    if letter in "аеёиоуыэюя": # если буква гласная
        count += 1
    syllables.append(count) # добавляем количество слогов в список
if len(set(syllables)) == 1: # если все элементы списка одинаковые
    print("Парам пам-пам")
else:
    print("Пам парам")