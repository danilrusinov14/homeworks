#1
import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self, func):
        self.func = func
        self.h = 1e-5
    def __call__(self, x):
        return (self.func(x + self.h) - self.func(x - self.h)) / (2 * self.h)
    def __get__(self, instance, owner):
        return self.__call__
    
class ExponentialFunction:
    def __init__(self, a):
        self.a = a  #коэфф
        self.derivative = Derivative(self)
    def __call__(self, x):
        #возвращаем значение функции f(x) = a * e^x
        return self.a * np.exp(x)
    def plot(self, x_range=(-2, 2), num_points=100):
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        #производная ф-и
        y_values = self(x_values)
        dy_values = self.derivative(x_values)

        #графики
        plt.figure(figsize=(10, 5))
        plt.plot(x_values, y_values, label=f'f(x) = {self.a} * e^x', color='blue')
        plt.plot(x_values, dy_values, label="f'(x)", color='red', linestyle='--')
        plt.title('График функции и её производной')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Ось X
        plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Ось Y
        plt.grid()
        plt.legend()
        plt.show()

# Пример использования
if __name__ == "__main__":
    exp_func = ExponentialFunction(a=2)
    print(exp_func(0))          # 2.0
    print(exp_func.derivative(0))  # 2.0 (производная 2e^x в x=0)

    exp_func.plot()