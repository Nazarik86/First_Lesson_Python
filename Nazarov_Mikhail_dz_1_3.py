# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

# Просим ввести число, которое нужно будет вывести со склонёным словом "процент"
i = int(input('Введите число от 1 до 20: '))

# Заводим переменные для первой реализации склонения
for_one = "процент"
for_two_to_four = "процента"
for_else = "процентов"

# Заводим переменную для второй реализации склонения
procents = "процент"

# С помощью цикла проверим введённое число и выведем: число и склонённое слово
print('Вывод для введённого числа: ')
while True:
    if i == 1:
        print(i, for_one)
        break
    elif 1 < i <= 4:
        print(i, for_two_to_four)
        break
    else:
        print(i, for_else)
        break

# Первая реализация вывода всех склонений слова "процент" от 1 до 20 с выводом сообщения какой способ использовался
print('')
print('Первая реализация вывода всех склонений слова "процент" от 1 до 20: ')
for number in range(1, 21):
    if number == 1:
        print(number, for_one)
    elif 1 < number <= 4:
        print(number, for_two_to_four)
    else:
        print(number, for_else)

# Вторая реализация вывода всех склонений слова "процент" от 1 до 20 с выводом сообщения какой способ использовался

print('')
print('Вторая реализация вывода всех склонений слова "процент" от 1 до 20: ')
for number in range(1, 21):
    if number == 1:
        print(number, procents)
    elif 1 < number <= 4:
        print(number, procents + "а")
    else:
        print(number, procents + "ов")
