#1. Вычислить число c заданной точностью d
# Пример: при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10


import math

new_pi = math.pi
num = input('Ввести число d в указанном интервале (10^-1 ≤ d ≤10^-10): ')

count = 0

num = num.replace('0.', '')
for i in num:
    count+=1
print(f' {new_pi:.{count}f}')