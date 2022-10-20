#Задача 1 Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


def randlist(x):
    from random import randint
    array = []
    for i in range (x):
        array.append (randint (1, 10))
    return array

def sum_oddnum (array):
    sum = 0
    for i in range (len(array)):
        if i%2 != 0:
            sum += array [i]
    return sum
try:
    n = int (input ('Введите необходимое количество чисел в списке: '))
    list_var = randlist (n)
    print (list_var)
    print (sum_oddnum (list_var))
except:
    print ('Ошибка!! Введите число!')

