#1
class Sauce:
    def __init__(self, flavor, addition=None):
        self.flavor = flavor  # Сохраняем вкус соуса
        self.addition = addition  # Сохраняем добавку, если она есть

    def show_my_sauce(self):
        if self.addition:  # Проверяем, есть ли добавка
            print(f"Соус и {self.addition}")  # Выводим соус с добавкой
        else:
            print("Майонез")  # Выводим 'Майонез', если добавки нет

sauce1 = Sauce("сырный", "перец")  # Создаем соус с добавкой
sauce1.show_my_sauce()  # Вывод: Соус и перец

sauce2 = Sauce("чесночный")  # Создаем соус без добавки
sauce2.show_my_sauce()  # Вывод: Майонез

#2
class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_salary(self):
        return self.__salary
    def set_bonus(self, bonus):
        self.__bonus = bonus
    def get_bonus(self):
        return self.__bonus
    def get_total_salary(self):
        return self.__salary + self.__bonus

if __name__ == "__main__":
    employee1 = Employee("Дядя Петя", 40, 150000)
    employee1.set_bonus(27000)
    # Выводим информацию о сотруднике
    print(f"Имя: {employee1.get_name()}")
    print(f"Возраст: {employee1.get_age()}")
    print(f"Оклад: {employee1.get_salary()} руб.")
    print(f"Бонус: {employee1.get_bonus()} руб.")
    print(f"Общая зарплата: {employee1.get_total_salary()} руб.")

#3
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def print_ingredients(self):
        print(f"Ингредиенты для '{self.name}':")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")  # Выводим каждый ингредиент
    def cook(self):
        print(f"Приготовление '{self.name}' завершено! Блюдо готово к подаче.")

if __name__ == "__main__":
    # Создаем экземпляр класса Recipe с названием и ингредиентами
    recipe1 = Recipe("Паста с соусом", ["паста", "томатный соус", "чеснок", "базилик", "сыр"])
    # Выводим список ингредиентов
    recipe1.print_ingredients()
    # Сообщаем о готовности блюда
    recipe1.cook()