class BankAccount:
    def __init__(self):
        self.balance = 0

    def Deposit(self, amount):
        self.balance += amount
        print("Deposit amount:", amount)

    def Withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn Amount:", amount)
        else:
            print("Insufficient Balance")

    def GetBalance(self):
        print("Current Balance:", self.balance)

class SavingAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__()
        self.interest_rate = interest_rate

    def AddInterest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Added interest amount:", interest)

ch = 1
while ch:
    if ch != 1:
        break
    account_type = input("Enter account type:\n 1. Bank Account \n 2. Saving account:")
    if account_type == "1":
        account = BankAccount()
    elif account_type == "2":
        interest_rate = float(input("Enter interest rate: "))
        account = SavingAccount(interest_rate)
    else:
        print("Invalid account type")
        exit()
    while True:
        print("\nChoose an operation ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Get Balance")
        if isinstance(account, SavingAccount):
            print("4. Add interest")
            print("5. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            amount = float(input("Enter the deposit amount: "))
            account.Deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the withdrawal amount: "))
            account.Withdraw(amount)
        elif choice == 3:
            account.GetBalance()
        elif choice == 4 and isinstance(account, SavingAccount):
            account.AddInterest()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
    ch = int(input("Do you want to continue? Press 1 for yes, 0 for no: "))
