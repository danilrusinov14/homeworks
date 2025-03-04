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