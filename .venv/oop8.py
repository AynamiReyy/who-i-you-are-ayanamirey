class BankAccount:
    def __init__(self, balance = None, interest_rate = None, transactions = []):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = transactions
    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f'Внесение наличных на счет: {amount}')
    def withdraw(self, amount):
        self.__balance -= amount
        self.__transactions.append(f'Снятие наличных: {amount}')
    def add_interest(self):
        self.__balance += (self.__balance * self.__interest_rate)
        self.__transactions.append(f'Начислены проценты по вкладу: {self.__balance * self.__interest_rate}')
    def history(self):
        for i in self.__transactions:
            print(i)
account = BankAccount(100000, 0.05)

account.deposit(15000)

account.withdraw(7500)

account.add_interest()

account.history()
