# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример: Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

list = []
new_list = []

numbers = int(input('Укажите длину списка: '))

while True:
    for i in range(numbers):
        list.append(int(input('Последовательно введите элементы списка: ')))
    break


for i in range(numbers):

    if list.count(list[i]) == 1:
        new_list.append(list[i])


print(list)
print(new_list)
#если нужно вывести все элементы списка, но без дублирующих, то можно использовать set (множество)