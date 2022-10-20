# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def randlist(x):
    from random import randint
    array = []
    for i in range (x):
        array.append (randint (1, 10))
    return array

def mylt_2 (array):
    mylt2 = []
    i = 0
    
    while i < len (array) / 2:
        mylt2.append (array[i]*array [len (array)-1-i])
        i += 1
    return mylt2

try:
    n = int (input ('Введите необходимое количество чисел в списке: '))
    list_var = randlist (n)
    print (list_var)
    print (mylt_2 (list_var))
except:
    print ('Ошибка!! Введите целое число!')