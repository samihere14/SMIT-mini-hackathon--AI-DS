## Banking System Mini Project Documentation

### Overview

This Python-based Bank Management System allows users to perform various banking operations, including:

* **Account Management:** Open and retrieve account details.
* **Transaction Operations:** Deposit, withdraw, and transfer funds.
* **Transaction Logging:** Log all transactions to a file.
* **Account Information:** Check account balances and view transaction history.
* **Administrative Features:** View total deposits and the number of accounts.

### Features

1. **Account Management:**
    - Open new accounts with unique account numbers and holder names.
    - Retrieve existing account details using account numbers.
2. **Transaction Operations:**
    - Deposit money into an account.
    - Withdraw money from an account (checks for sufficient balance).
    - Transfer money between accounts.
3. **Transaction Logging:**
    - Every deposit and withdrawal is logged into a file named `transaction.txt`.
    - Log entries include transaction type, amount, and the current balance.
4. **Account Information:**
    - Check account balances.
    - Print a detailed transaction statement.
5. **Administrative Features:**
    - View the total amount of deposits across all accounts.
    - View the total number of accounts in the bank.
6. **User-Friendly Interface:**
    - A menu-driven system to navigate through various options.

### Files

1. **`main.py`**: Contains the implementation of the banking system.
2. **`transaction.txt`**: Stores logs of all deposit and withdrawal transactions.

### Classes and Methods

#### Class: `BankAccount`

Represents an individual bank account.

##### Methods:

- `__init__(self, account_number, account_holder)`: Initializes the account with a unique number, holder name, and zero balance.
- `deposit(self, amount)`: Deposits a specified amount and logs the transaction in `transaction.txt`.
- `withdraw(self, amount)`: Withdraws a specified amount (if sufficient balance) and logs the transaction in `transaction.txt`.
- `check_balance(self)`: Returns the current balance of the account.
- `print_statement(self)`: Prints the transaction history of the account.

#### Class: `Bank`

Manages multiple accounts in the bank.

##### Methods:

- `__init__(self)`: Initializes the bank with an empty dictionary to store accounts.
- `open_account(self, account_number, account_holder)`: Opens a new account.
- `get_account(self, account_number)`: Retrieves an account using its account number.
- `transfer(self, sender_account_number, receiver_account_number, amount)`: Transfers funds between two accounts.
- `admin_check_total_deposit(self)`: Returns the total deposits in the bank.
- `admin_check_total_accounts(self)`: Returns the total number of accounts in the bank.

### How to Use

1. Run the `main.py` file.
2. Use the menu to navigate through options:
   - Open an account by providing a unique account number and the account holder's name.
   - Deposit money by specifying the account number and amount.
   - Withdraw money by specifying the account number and amount.
   - Transfer money between two accounts by specifying sender and receiver account numbers and the amount.
   - View account balance or transaction statement by providing the account number.
   - Use administrative options to check the total deposits or the total number of accounts.
   - Exit the program when finished.

### Transaction Logging

- All deposits and withdrawals are logged in `transaction.txt` in the following format:
  ```
  $<amount> is deposited successfully. Current balance: $<balance>
  *****
  $<amount> is withdrawn successfully. Current balance: $<balance>
  *****
  ```

### Notes

- Ensure `transaction.txt` exists or can be created in the working directory.
- All amounts must be positive values.
- Unique account numbers are required to open an account.
- The program includes error handling for invalid inputs and insufficient balance.

### Hackathon Participation

This project was developed as part of Saylani's Mini Hackathon for AI-DS.

## Comparison with the Original Code

This documentation is similar to the original code, but it is more detailed and organized. It includes additional information about the project, such as the files, classes, methods, and how to use the system. It also provides more context about the transaction logging and the hackathon participation.
