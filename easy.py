# Подключение функционала в языке Питон
import os
import psutil
import sys
import shutil
# Задание 1
# Вариант 1
n = '10'
for n in range(10):
	print(n)

print("easy")

# Вариант 2
n = ''
for n in range(20):
	print(n)

# Задание 2
c1 = input("Напишите первое целое число: ")
print("Спасибо за:", c1)
c2 = input("Напишите второе целое число: ")
print("Спасибо за:", c2)
c3 = c1
c1 = c2
c2 = c3


print(c1,c2)



old = input("Сколько тебе лет?: ")
if old >= '18':
	print("Доступ открыт")
else:
	print("Давай по позже друг")


# Хард
# Задание 1

a = input("напишите любое число: ")
s = str(a)
ls = list(map(int, s))
r = max(ls)
print(r)

# Задание 2

import math
ab = input("Напишите первое целое число: ")
#print("Спасибо за:", c)
bc = input("Напишите второе целое число: ")
#print("Спасибо за:", b)
ab = int(ab) + int(bc) 
bc = int(ab) - int(bc) 
ab = int(ab) - int(bc)
print(ab,bc)


# Задание 3
a = int(input("a = введите число: "))
x = int(input("x = введите число: "))
b = int(input("b = введите число: "))
c = int(input("c = введите число: "))
#ax + bx + c = 0
print("math")
#a = int(2)
#x = int(5)
#b = int(4)
#c = int(5)
h = 0
h = int(a*math.sqrt(x)) + (b*x) + c
print(h)
#




