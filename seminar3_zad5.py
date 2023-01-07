# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def negafib (x):
    array = [0, 1]
    s = 0
    array2 = []
    for i in range (2,x+1):
        array.append (array[i-2]+array[i-1])
    for i in range (1,x+1):
        s = (array[i]) * ((-1)**(i-1))
        array2.insert (0, s)
    array = array2+array
    return array

n = 8
print (negafib(n))
