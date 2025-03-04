#1
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @staticmethod
    def _check_positive(amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом.")

    def deposit(self, amount):
        self._check_positive(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self._check_positive(amount)
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счёте.")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    @classmethod
    def create_empty_account(cls, account_number):
        return cls(account_number)  # Создание нового объекта с нулевым балансом
    
# Пример использования
if __name__ == "__main__":
    account = BankAccount.create_account("123456789")  # Создание счёта
    account.deposit(100)
    account.withdraw(50)
    print(f"Текущий баланс: {account.get_balance()}")


#2
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @staticmethod
    def is_password_complex(password):
        # Проверка сложности пароля (длина не менее 6 символов)
        return len(password) >= 6

    @classmethod
    def create_default_user(cls, username):
        # Создание пользователя с безопасным паролем по умолчанию
        default_password = "defaultPass"
        return cls(username, default_password)

    def set_password(self, new_password):
        # Метод для смены пароля
        if not self.is_password_complex(new_password):
            raise ValueError("Пароль слишком короткий")
        self.__password = new_password
        print("Пароль успешно изменён")

    def get_username(self):
        return self.__username

# Пример использования
user = User.create_default_user("Alice")
print(user.get_username())  # Вывод: Alice
try:
    user.set_password("12345")  # Ошибка: пароль слишком короткий
except ValueError as e:
    print(e)
user.set_password("securePass")  # Пароль успешно изменён


#3
class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    @staticmethod
    def is_year_valid(year):
        # год издания является корректным (int и не в будущем)?
        return isinstance(year, int) and year <= 2024  # 2024 - текущий год для примера

    @classmethod
    def create_default_year(cls, title, author):
        # без года (год по умолчанию 2024)
        return cls(title, author, 2024)

    def get_info(self):
        # инфа о книге
        return f"{self.__title}, автор: {self.__author}, год: {self.__year}"

# Пример использования
book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())  # Вывод: "1984, автор: George Orwell, год: 1949"
book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info())  # Вывод: "Brave New World, автор: Aldous Huxley, год: 2024"

# Проверка корректности года
year_to_check = 2025
if not Book.is_year_valid(year_to_check):
    print(f"Год {year_to_check} недопустим")  # Вывод: Год 2025 недопустим
