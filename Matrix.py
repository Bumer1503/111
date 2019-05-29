# Дано нечетное число n.
# Создайте вложеный список из n×n элементов, заполнив его символами "."(каждый элемент массива является строкой из одного символа).
# Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ.
# В результате должны образовывать изображение снежинки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
n = int(input("Razmer "))
matrix = []
for i in range(n):
    matrix.append(list())
    for j in range(n):
        matrix[i].append(0)

for i in range(n):
    for j in range(n):
        matrix[i][i] = '#'
        matrix[i][n - 1 - i] = '#'
        matrix[n//2][i] = '#'
        matrix[i][n//2] = '#'

print("Result: \n")
for i in range(n):
    print(matrix[i], '\n')


# Случайная матрица
import random
M,N = 3,3
matrix = [[random.randrange(0,10) for y in range(M)] for x in range(N)]
for im in range(N):
 print(matrix[im])


# Разворот строки
word = input ("Type a word which you want to reverse: ")
def reverse(word):
  word = word[::-1]
  return word
print (reverse(word))