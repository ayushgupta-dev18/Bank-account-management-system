class Account:
    next_account_number = 1000

    def __init__(self, name, balance):
        self.name    = name
        self.balance = balance
        self.account_number = Account.next_account_number
        Account.next_account_number += 1
    
    # Credit in the bank account
    def account_credit(self,amount):
        print(f"₹{amount} is successfully credited to the {self.name} account")
        self.balance += amount
    
    # Withdrawal from the account
    def account_debit(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully from {self.name}'s account.")
            return True
        else:
            print("Insufficient Balance!")
            return False
        
    #show balance 
    def show_balance(self):
        print(f"₹{self.balance}\nBalance check successful✅")

    #mini statement
    def mini(self):
        print("\n========================================")
        print("         🏦 MINI STATEMENT")
        print("========================================")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")
        print("========================================")


accounts = {}


# Load accounts from file

try:
    file = open("accounts.txt", "r")

    lines = file.readlines()

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        data = line.split(",")

        account_number = int(data[0])
        name = data[1]
        balance = int(data[2])

        account = Account(name, balance)

        account.account_number = account_number

        accounts[account_number] = account

        Account.next_account_number = account_number + 1

    file.close()

except FileNotFoundError:
    print("No previous accounts found. Starting fresh...")


def save_accounts():

    file = open("accounts.txt", "w")

    for account in accounts.values():
        file.write(f"{account.account_number},{account.name},{account.balance}\n")

    file.close()


while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Show Balance")
    print("6. Mini Statement")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        balance = int(input("Enter initial balance: "))
        new_account = Account(name, balance)
        accounts[new_account.account_number] = new_account
        print("\n✅ Account Created Successfully!")
        print(f"Account Holder : {new_account.name}")
        print(f"Account Number : {new_account.account_number}")
        print(f"Current Balance: ₹{new_account.balance}")
        
       #file Handling
        file = open("accounts.txt", "a")
        file.write(f"{new_account.account_number},{new_account.name},{new_account.balance}\n")

        file.close()


    #deposit menu
    elif choice == 2:
        account_number = int(input("Enter account number : "))
        if account_number in accounts:
            deposit_amount = int(input("Enter Deposit Amount : "))
            accounts[account_number].account_credit(deposit_amount)   
            save_accounts()  
        else:
            print("Account does not exits!")

    #withdrawal menu
    elif choice == 3:
        account_number= int(input("Enter Account Number : "))
        if account_number in accounts:
            withdrawal_amount = int(input("Enter Withdrawal Amount : "))
            accounts[account_number].account_debit(withdrawal_amount)
            save_accounts()
        else:
            print("Account does not exist!")
    
    #trasfer menu
    elif choice == 4:
        sender_account = int(input("Enter Sender Account Number : "))
        reciever_account = int(input("Enter Reciever Account Number : "))

        if sender_account in accounts and reciever_account in accounts :
            amount = int(input("Enter Transfer Amount : "))
            if  accounts[sender_account].account_debit(amount):
                 
                 accounts[reciever_account].account_credit(amount)
                 save_accounts()
                 print(f"₹{amount} transferred successfully "
                       f"from {accounts[sender_account].name} "
                       f"to {accounts[reciever_account].name}.")
        else: 
           print("Either one or both the accounts are Invalid !!")


    #show balance
    elif choice == 5:
        account_number=int(input("Enter Account Number : "))   
        if account_number in accounts:
            accounts[account_number].show_balance()
        else:
            print("Account does not exist")


    #Mini statement
    elif choice == 6:
        account_number = int(input("Enter Account Number: "))
        if account_number in accounts:
            accounts[account_number].mini()
        else:
            print("Account does not exist!")

    #Exit
    elif choice == 7:
        print("Thank you for using Bank Management System!")
        break

    else:
        print("This feature is not implemented yet.")