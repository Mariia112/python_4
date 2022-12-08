#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
#Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

from random import randint

list = []

k = int(input('Введите натуральную степень К= '))
equation = 0

for i in range(1, k + 2):
    i = randint(1, 100)
    list.append(i)

print(list)

for i in range(1, k + 1):
    equation = (f' ({list[i - 1]}x^{k - i + 1}) + {equation}')

    if i == k:
        equation = (f' {equation} + {list[-1]} = {0}')

print(equation)

data = open('task4_file.txt', 'w')
data.write(equation)
data.close