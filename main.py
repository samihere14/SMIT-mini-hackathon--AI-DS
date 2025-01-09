class BankAccount:
    def __init__(self, Account_number, Account_holder):
        #Initilize a new Bank Account with unique Account number, Holder's name, and Balance.
        self.Account_number = Account_number
        self.Account_holder = Account_holder
        self.balance = 0
        self.transactions = []  #This function is store transaction history.

    def deposit(self, amount):
        #This function is adds the specified amount to the account balance. 
        if amount <= 0:
            print("Deposit Amount must should be greater than Zero(0).")
        else:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount}")
            print(f"${amount} Deposited Successfully!")

    def withdraw(self, amount):
        #This function is Deducts the specified amount from the account Balance if funds are available.
        if amount <= 0:
            print("Withdrawal amount must be greater than Zero(0).")
        elif amount > self.balance:
            print("Your Balance is Insufficient!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
            print(f"${amount} Withdrawn Successfully!")

    def check_balance(self):
        #This function is returns the Current Account Balance.
        return self.balance

    def print_statement(self):
        #Prints the transaction history in a formatted way.
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)


class Bank:
    def __init__(self):
        #This function is initializes the Bank with an empty dictionary to store Accounts.
        self.accounts = {}

    def open_account(self, account_number, account_holder):
        #This function is creates a new Account for the user with a unique Account Number.
        if account_number in self.accounts:
            print("This Account number already exists!")
        else:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            print("Account opened successfully!")

    def get_account(self, account_number):
        #Retrieves an account object using its account number.
        return self.accounts.get(account_number, None)

    def transfer(self, sender_account_number, receiver_account_number, amount):
        #This function is transfers money from one Account to another if sufficient funds are available.
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)

        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Transferred ${amount} from {sender_account_number} to {receiver_account_number}")
            else:
                print("Insufficient balance in sender's account!")
        else:
            print("Invalid account number(s)!")

    def admin_check_total_deposit(self):
        #Calculates and returns the total deposits in the bank.
        total = sum(account.balance for account in self.accounts.values())
        return total

    def admin_check_total_accounts(self):
        #Returns the total number of accounts in the bank.
        return len(self.accounts)


def main():
    bank = Bank()
    while True:
        print("\n1. Open Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Print Statement")
        print("7. Admin: View Total Deposits")
        print("8. Admin: View Total Accounts")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_number = input("Enter a unique account number: ")
            account_holder = input("Enter account holder's name: ")
            bank.open_account(account_number, account_holder)

        elif choice == 2:
            account_number = input("Enter your account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found!")

        elif choice == 3:
            account_number = input("Enter your account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found!")

        elif choice == 4:
            account_number = input("Enter your account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Your current balance is: ${account.check_balance()}")
            else:
                print("Account not found!")

        elif choice == 5:
            sender = input("Enter sender's account number: ")
            receiver = input("Enter receiver's account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(sender, receiver, amount)

        elif choice == 6:
            account_number = input("Enter your account number: ")
            account = bank.get_account(account_number)
            if account:
                account.print_statement()
            else:
                print("Account not found!")

        elif choice == 7:
            print(f"Total deposits in the bank: ${bank.admin_check_total_deposit()}")

        elif choice == 8:
            print(f"Total number of accounts: {bank.admin_check_total_accounts()}")

        elif choice == 9:
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()