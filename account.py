from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    @abstractmethod
    def statement(self):
        pass

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)  
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Added ${interest:.2f} interest to {self.owner}'s savings.")

    def statement(self):
        return f"Savings Account - {self.owner}: ${self._balance:.2f}"

class CurrentAccount(Account):
    def __init__(self, owner, balance, overdraft):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if 0 < amount <= (self._balance + self.overdraft):
            self._balance -= amount
            return True
        else:
            print(f"{self.owner}: Overdraft limit exceeded.")
            return False
        
    def statement(self):
        return f"Current Account - {self.owner}: ${self._balance:.2f}"


if __name__ == "__main__":
    acc1 = SavingsAccount("Alice", 1000.0, 0.05)
    acc2 = CurrentAccount("Bob", 500.0, 300.0)

    acc1.deposit(200)
    acc1.add_interest()

    acc2.deposit(100)
    acc2.withdraw(700)

    accounts = [acc1, acc2]

    for account in accounts:
        print(account.statement())