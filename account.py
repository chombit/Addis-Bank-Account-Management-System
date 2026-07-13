class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance  # Protected attribute

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

    def statement(self):
        return f"Account - {self.owner}: ${self._balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # e.g., 0.05 for 5%

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Added ${interest:.2f} interest to {self.owner}'s savings.")

    # Step 4: Override statement()
    def statement(self):
        return f"Savings Account - {self.owner}: ${self._balance:.2f}"


class CurrentAccount(Account):
    def __init__(self, owner, balance, overdraft):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    # Step 3: Override withdraw() to check balance + overdraft limit
    def withdraw(self, amount):
        if 0 < amount <= (self._balance + self.overdraft):
            self._balance -= amount
            return True
        else:
            print(f"{self.owner}: Overdraft limit exceeded.")
            return False

    # Step 4: Override statement()
    def statement(self):
        return f"Current Account - {self.owner}: ${self._balance:.2f}"
if __name__ == "__main__":
    # Create the instances
    acc1 = SavingsAccount("Alice", 1000.0, 0.05)
    acc2 = CurrentAccount("Bob", 500.0, 300.0)

    # Perform typical transactions
    acc1.deposit(200)       
    acc1.add_interest()     
    acc1.withdraw(400)      

    acc2.deposit(100)       
    acc2.withdraw(700)      

    accounts = [acc1, acc2]

    # Drive them dynamically through one loop
    for account in accounts:
        print(account.statement())