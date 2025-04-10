#1
import math

#класс Shape
class Shape:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределён в подклассе")
    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть переопределён в подклассе")

#подкласс Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

#подкласс Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

#пример использования
if __name__ == "__main__":
    #экземпляр класса Circle
    circle = Circle(5)
    print("Circle area:", circle.area())          #площадь круга
    print("Circle perimeter:", circle.perimeter())  #периметр круга

    #экземпляр класса Rectangle
    rectangle = Rectangle(4, 6)
    print("Rectangle area:", rectangle.area())          #площадь прямоугольника
    print("Rectangle perimeter:", rectangle.perimeter())  #периметр прямоугольника


#2
#базовый класс Animal
class Animal:
    def sound(self):
        return "Животное издает звук"
#подкласс Dog
class Dog(Animal):
    def sound(self):
        return "Гав-гав"
#подкласс Cat
class Cat(Animal):
    def sound(self):
        return "Мяу"
#подкласс Cow
class Cow(Animal):
    def sound(self):
        return "Муу"

# пример задачи
if __name__ == "__main__":
    #список из разных животных
    animals = [Dog(), Cat(), Cow()]
    for animal in animals:
        print(animal.sound())