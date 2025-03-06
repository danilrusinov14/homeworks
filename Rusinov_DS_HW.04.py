class Fraction:
    def __init__(self, numm, denom):
        # должны быть целые числа
        if not isinstance(numm, int) or not isinstance(denom, int):
            raise ValueError("Числитель и знаменатель должны быть целыми ЧИСЛАМИ.")
        # деление на 0
        if denom == 0:
            raise ValueError("Знаменатель не может быть равен нулю.") 
         
        self.numm = numm
        self.denom = denom
        self.simplify() #упрощаем дробь
    def simplify(self):
        # упрощаем с помощью наибольшего общего делителя
        from math import gcd
        NOD = gcd(self.numm, self.denom)
        self.numm //= NOD
        self.denom //= NOD
    @property
    def value(self):
        # Возвращаем точное значение дроби, округленное до 3 знаков
        return round(self.numm / self.denom, 3)
    def __str__(self):
        # Красивый вывод дроби
        return f"{self.numm}/{self.denom}"
    def __add__(self, other):
        # сложение
        if not isinstance(other, Fraction):
            return NotImplemented
        n_numm = self.numm * other.denom + other.numm * self.denom
        n_denom = self.denom * other.denom
        return Fraction(n_numm, n_denom)
    def __sub__(self, other):
        # вычитание
        if not isinstance(other, Fraction):
            return NotImplemented
        n_numm = self.numm * other.denom - other.numm * self.denom
        n_denom = self.denom * other.denom
        return Fraction(n_numm, n_denom)
    def __mul__(self, other):
        # умножение
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numm * other.numm
        new_denominator = self.denom * other.denom
        return Fraction(new_numerator, new_denominator)
    def __truediv__(self, other):
        # деление
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numm == 0:
            raise ValueError("деление на ноль!")
        n_numm = self.numm * other.denom
        n_denom = self.denom * other.numm
        return Fraction(n_numm, n_denom)
# пример
try:
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print(f1 + f2)  # 5/4
    print(f1 - f2)  # -1/4
    print(f1 * f2)  # 3/8
    print(f1 / f2)  # 2/3
    print(f1.value) # 0.5
except ValueError as e:
    print(f"Ошибка: {e}")