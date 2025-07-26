from math import floor
import pytest


class BankAccount:
    owner: str
    __balance: int

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if (self.__balance + amount > 0):
            self.__balance += amount
        else:
            raise ValueError

    def withdraw(self, amount):
        if (self.__balance - amount > 0):
            self.__balance -= amount
        else:
            raise ValueError

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    interest_rate: float

    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        balance = self.get_balance()
        interest = floor(balance * self.interest_rate)
        self.deposit(interest)


class CheckingAccount(SavingsAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance, interest_rate)

    def withdraw(self, amount):
        self._BankAccount__balance -= amount

    def test_balance(self):
        balance = self.get_balance()
        assert balance > 0, 'Баланс не положительный'
