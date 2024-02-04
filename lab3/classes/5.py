class BankAccount:
    def __init__(self):
        self.owner = "Maksat Ergen"
        self.balance = 20000

    def deposit(self):
        amount = int(input())
        return amount + self.balance
    
    def withdraw(self):
        amount = int(input())
        if amount > self.balance:
            return "Not sufficient"
        else:
            return self.balance - amount

value = BankAccount()
print(value.deposit())
print(value.withdraw())