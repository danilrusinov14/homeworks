#1
class Person:
    def __init__(self, name, age):
        self.__setattr__('name', name)  # Установка имени с проверкой
        self.__setattr__('age', age)      # Установка возраста с проверкой
    def __setattr__(self, key, value):
        if key == 'name':
            if not value:  # Проверка, что имя не пустое
                raise ValueError("Имя не может быть пустым!")
            self.__dict__[key] = value  # Установка имени
        elif key == 'age':
            if not isinstance(value, (int, float)) or value <= 0:  # Проверка возраста
                raise ValueError("Возраст должен быть положительным числом!")
            self.__dict__[key] = value  # Установка возраста
        else:
            self.__dict__[key] = value  # Установка других атрибутов
    def __str__(self): #Отображение инфы о человеке
        return f"Person(name={self.name}, age={self.age})"
# Пример использования
if __name__ == "__main__":
    p = Person("John", 25)
    print(p)
    p.name = "Alice"
    p.age = 30
    print(p)
    try:
        p.name = ""  # ValueError: Имя не может быть пустым!
    except ValueError as e:
        print(e)
    try:
        p.age = -5  # ValueError: Возраст должен быть положительным числом!
    except ValueError as e:
        print(e)


#2
class Counter:
    def __init__(self):
        self._attributes = {} #Словарь для атрибутов
    def __setattr__(self, name, value):
        if name != "_attributes":  # Исключаем внутр атрибут
            print(f"Установка атрибута {name} → {value}")
        self._attributes[name] = value
        super().__setattr__(name, value)
    def __getattribute__(self, name):
        if name in self._attributes:
            value = self._attributes[name]
            print(f"Доступ к атрибуту {name} → {value}")
        else:
            print(f"Доступ к атрибуту {name} → None")
            value = None  # Если атрибут не существует, возвращаем None
        return value
# Пример использования
c = Counter()
c.value = 5         # Атрибут value будет добавлен
print(c.value)      # Доступ к атрибуту value → 5
print(c.name)       # Доступ к атрибуту name → None
