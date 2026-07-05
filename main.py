class Account:
    next_account_number = 1000

    def __init__(self, name, balance):
        self.name    = name
        self.balance = balance

        self.account_number = Account.next_account_number
        Account.next_account_number += 1

accounts = {}

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

    elif choice == 7:
        print("Thank you for using Bank Management System!")
        break

    else:
        print("This feature is not implemented yet.")