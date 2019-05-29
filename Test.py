# Создать класс Фигура. Наследовать от него классы Треугольник, Прямоугольник, Квадрат.
# У каждого класса создать метод для подсчета периметра и площади.
class figura:
    def __init__(self):
        self.perimetr = 0
        self.ploshad = 0
    class treugolnik(figura):
        def __init__(self):
           self.perimetr = a + b + c
           self.ploshad = int((a*b)/2)

    class kvadrat(figura):
        def __init__(self):
           self.perimetr = a * 4
           self.ploshad = a * a

    class pryamoygolnik(figura):
        def __init__(self):
           self.perimetr = (a + b)*2
           self.ploshad = a * b

a = 5
b = 4
c = 9
print(figura)
