# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

def randlistfloat(x):
    from random import randint
    array = []
    for i in range (x):
        array.append (randint(100, 1000)/100)
    return array

def minmaxdiff (array):
    imax = 0
    imin = 0
    for i in range (len (array)):
        if  array [i]%1  > array [imax]%1:
            imax = i
        elif array [i]%1  < array [imin]%1:
            imin = i
    return round ((array [imax]%1 - array [imin]%1),2)
        


try:
    n = int (input ('Введите необходимое количество чисел в списке: '))
    list_var = randlistfloat (n)
    print (list_var)
    print (minmaxdiff (list_var))
except:
    print ('Ошибка!! Введите целое число!')