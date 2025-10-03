# bank_account.py

class BankAccount:
    """
    A simple BankAccount class demonstrating encapsulation and basic banking operations.
    """

    def __init__(self, initial_balance=0.0):
        # account_balance is an instance attribute (encapsulated state for each account)
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Add amount to the account balance.
        Returns the new balance.
        Raises ValueError for invalid (non-numeric or negative) amounts.
        """
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Invalid amount. Please provide a numeric value.")
        if amt < 0:
            raise ValueError("Amount must be non-negative.")
        self.account_balance += amt
        return self.account_balance

    def withdraw(self, amount):
        """
        Attempt to withdraw amount from account_balance.
        If funds are sufficient, deduct and return True.
        If insufficient funds, do not change balance and return False.
        Raises ValueError for invalid (non-numeric or negative) amounts.
        """
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Invalid amount. Please provide a numeric value.")
        if amt < 0:
            raise ValueError("Amount must be non-negative.")
        if amt <= self.account_balance:
            self.account_balance -= amt
            return True
        return False

    def display_balance(self):
        """
        Print the current balance in a user-friendly format.
        """
        print("Current balance: ${:.2f}".format(self.account_balance))

