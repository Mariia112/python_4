#Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*

import re

path = 'task4_file.txt'
data = open(path, 'r')
for polynom_1 in data:
    print(polynom_1)
data.close()
string1 = str(polynom_1)

path = 'task5_file.txt'
data = open(path, 'r')
for polynom_2 in data:
    print(polynom_2)
data.close()
string2 = str(polynom_2)

result1 = re.findall('[0-9]+', string1)

result1.pop(1)
result1.pop(-1)
result1.pop(2)
result1.pop(-2)
result1.pop(3)
result1.pop(4)
result1.pop(5)
print(result1)

result2 = re.findall('[0-9]+', string2)

result2.pop(1)
result2.pop(-1)
result2.pop(2)
result2.pop(-2)
result2.pop(3)
result2.pop(4)
result2.pop(5)
print(result2)

new_list = []
for i in range(len(result1)):
    new_list.append((int(result1[i])) + (int(result2[i])))

print(new_list)

equation = 0
for i in range(1, len(new_list) + 1):
    equation = (f' ({new_list[i - 1]}x^{i - 1}) + {equation} ')

    if i == len(new_list):
        equation = (f' {equation} + {new_list[-1]} = {0}')

print(equation)
data = open('task5_result.txt', 'w')
data.write(equation)
data.close

#Очень сомневаюсь в корректности данного решения...((((