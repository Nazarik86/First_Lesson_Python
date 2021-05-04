## 2 Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
## a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – #
## делится нацело на 7. Внимание: использовать только арифметические операции!
## b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
## c. * Решить задачу под пунктом b, не создавая новый список.

# выглядит заумно и мы этого не проходили, нашёл в Интернете такой способ.
# "len(cube_list)" - это индекс последнего элемента списка,
# "sum(map(int,str(LIST])))" - нашёл в похожей задаче в интернете и эта операция вычисляет сумму цифр числа.
# map - указывает, что обработать нужно весь список, sum - сумма списка
# можно проверить раскомментировав три строки ниже
# num = 27365478
# sum(map(int,str(num)))
# print(sum(map(int,str(num))))


cube_list = []

for i in range(1, 1000, 2):
    cube_list.append(i ** 3)
print('список кубов нечётных чисел от 1 до 1000: ', cube_list)
print('индекс последнего элемента списка: ', len(cube_list))
# print(type(len(cube_list)))

sum_list = []
seven_list = []
seven_item_list = []
sum_seven = 0


for ind in range(len(cube_list)):
    sum_list.append(sum(map(int, str(cube_list[ind]))))  # map - указывает, что обработать нужно весь список, sum - сумма списка

    if sum_list[ind] % 7 == 0:  # проверяем, что сумма цифр элемента списка делится нацело на 7
        seven_list.append(cube_list[ind])  # записываем в список "seven_list" значение числа из "cube_list"
        seven_item_list.append(sum_list[ind])  # для проверки, что индексируется правильно

for x in seven_list:  # считаем сумму всех элементов списка, в которых сумма всех цифр кратна 7
    sum_seven = sum_seven + x

print('сумма цифр числа: sum_list ', sum_list)
print('seven_item_list: ', seven_item_list)

print('Список чисел, которые без остатка делятся на 7: ', seven_list)

print('Сумма всех элементов: ', sum_seven)

cube_plus_seventeen = []
seventeen_list = []
sum_seventeen_list = []
seventeen_item_list = []
sum_seventeen = 0


# Прибавляем по 17 к списку чисел, которые без остатка делятся на 7

for numbers in range(len(cube_list)):
    cube_plus_seventeen.append(cube_list[numbers] + 17)
print('cube_plus_seventeen прибавляем к каждому элементу списка по 17 : ', cube_plus_seventeen)
print('индекс последнего элемента списка: ', len(cube_plus_seventeen))

for ind in range(len(cube_plus_seventeen)):
    sum_seventeen_list.append(sum(map(int, str(cube_plus_seventeen[ind]))))  # map - указывает, что обработать нужно весь список, sum - сумма списка
print('индекс последнего элемента списка sum_seventeen_list: ', len(sum_seventeen_list))

for numbers in range(len(sum_seventeen_list)):
    if sum_seventeen_list[numbers] % 7 == 0:  # проверяем, что сумма цифр элемента списка делится нацело на 7
        seventeen_item_list.append(sum_seventeen_list[numbers])  # записываем в список "seventeen_list" значение числа из "sum_seventeen_list"
        seventeen_list.append(cube_plus_seventeen[numbers])

for y in seventeen_list:  # считаем сумму всех элементов списка, в которых сумма всех цифр кратна 7
    sum_seventeen = sum_seventeen + y

print('seventeen_list: ', seventeen_list)
print('sum_seventeen_list', sum_seventeen_list)
print('seventeen_item_list ', seventeen_item_list)
print('sum_seventeen', sum_seventeen)

