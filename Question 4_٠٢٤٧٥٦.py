
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        return interest_amount

    def print(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate}%")

# Create an instance of BankAccount
bank_acc = BankAccount("123456", "John Doe")
print("Bank Account Details:")
print(f"Initial Balance: ${bank_acc.get_balance()}")
bank_acc.deposit(1000)
print(f"Balance after depositing $1000: ${bank_acc.get_balance()}")
bank_acc.withdraw(500)
print(f"Balance after withdrawing $500: ${bank_acc.get_balance()}")

# Create an instance of SavingsAccount
savings_acc = SavingsAccount("789012", "Jane Smith", 2.5)
print("\nSavings Account Details:")
print(f"Initial Balance: ${savings_acc.get_balance()}")
savings_acc.deposit(1500)
savings_acc.apply_interest()
print("Balance after applying interest:")
savings_acc.print()
