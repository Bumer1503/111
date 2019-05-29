#1 Сгенерировать случайное число с помощью randint и вывести его на экран
from random import randint, randrange
print(randrange(60))

#2 Дан список чисел [1,2,3,4,5,6].
# Перемешать список с помощью функции random.shuffle и вывести случайное число с помощью random.choice
from random import shuffle, choice
var1 = [1,2,3,4,5,6]
shuffle(var1)
print(choice(var1))

#3 Сгенерировать случайное число с плавающей точкой с помощью random.random() и вывести его на экран
from random import random
print(random())

#4 Сгенерировать случайное число с плавающей точкой в диапазоне от 0 до 25 с помощью random.uniform и вывести его на экран
from random import uniform
print(uniform(0, 25))



