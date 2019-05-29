# Написать класс Треугольник с вычисляемым атрибутом square и perimeter
class treugolnik:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    @property # преобразование из действия в свойтво
    def perimetr(self):
        return self.a + self.b + self.c
    @property
    def square(self):
        return (self.a + self.h)/2
tr1 = treugolnik(4,4,6,7)
print(tr1.perimetr)
print(tr1.square)
print("_"*20)
# Написать класс Distance с приватным атрибута _distance (в метрах).
# Объявить для этого атрибута setter, getter, deleter, который будет показывать дистанцию в метрах.
# Создать вычисляемый атрибут для перевода дистанции в шаги (in_feet, 1м = 0.67 шагов)

class Distance:
    def __init__(self, distance):
        self._distance = distance

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value1):
        print("change...")
        self._distance = value1

    @distance.deleter
    def distance(self):
        print("remove...")
        del self._distance

    @property # преобразование
    def in_feet(self):
        return self.distance * 0.67
# rast = Distance(123) # rast - экземляр класса
# print(rast.distance) # .distance -атрибут
# print(rast.in_feet)  # .in_feet -атрибут
# del rast.distance

# Написать класс Wallet с приватными атрибутами класса: dollars, cents.
# Написать setter, deleter, getter для cents и вычисляемый атрибут для общего количества денег.

