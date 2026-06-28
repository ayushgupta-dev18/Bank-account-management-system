class Account:

    def __init__(self, name, balance):
        self.name    = name
        self.balance = balance

    def account_debit(self, amount):
        if amount <= self.balance:
            print(f"₹{amount} debited from {self.name} account")
            self.balance -= amount
        else:
            print("Insufficient balance")

    def account_credit(self, amount):
        print(f"₹{amount} credited to {self.name} account")
        self.balance += amount

    def show_balance(self):
       print(f"{self.name} has ₹{self.balance} remaining in account")

    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"₹{amount} transferred from {self.name} to {other_account.name}")
        else:
            print("Insufficient balance.")
    
    # Mini statement 
    
    def mini(self):
        print(f"=====Mini Statement=====\n Account holder : {self.name }\n Current balanc:{self.balance}\n ======================")
    
#savings account:
class SavingAccounts(Account):
    
    
    def interest(self, add_interest):
        interest= self.balance*add_interest/100
        self.account_credit(interest)
    
    
    
# Creating two account:
a1 = Account("Ayush", 10000)
a2 = Account("Ashish", 5000)

a1.account_credit(4000)
a1.account_debit(1000)

a1.show_balance()
a2.show_balance()

a1.transfer(a2, 3000)

print("\nAfter Transfer:")
a1.show_balance()
a2.show_balance()
print("\n")

a1.mini()


a3= SavingAccounts("Akash",10000)

a3.interest(5)
a3.show_balance()
