class Account:
    def __init__(self, account_number:str, account_balance: float, account_holder:str):
        self.account_number = account_number
        self.account_balance = account_balance 
        self.account_holder = account_holder

    def deposit(self, amount: float):
        self.account_balance += amount
        print(f"{amount} added to the account_balance")
    
    def withdraw(self, amount: float):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} is substracted from the account balance")
        else:
            print("the substraction failed")
    
    def check_balance(self):
        return f"Your current account balance is : {self.account_balance} DZD"
    
my_account = Account("A30", 25000.00,"Ali")
print (my_account)

my_account.deposit(1000)
my_account.withdraw(500)
print(my_account.check_balance())

account1 =Account("B52", 30000.00, "Ahmed")
account2 =Account("D20", 45000.00, "Amina")
account3 = Account("C02", 6000.00, "Nadia")

account2.deposit(2000)
account2.withdraw(250)
print(account2.check_balance())

account3.deposit(1000)
account3.withdraw(8000) #the substraction failed
print(account3.check_balance()) 
 
