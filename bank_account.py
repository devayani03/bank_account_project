# bank_account.py

class BankAccount:
    def __init__(self, owner, balance=0.0):
        """Initialize a bank account with an owner and balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit a positive amount."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw if sufficient balance is available."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Return current balance."""
        return self.balance
