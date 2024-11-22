def deposit(account: tuple, amount: float):
    account_number, balance = account
    balance += amount
    return account_number, balance

def withdraw(account: tuple, amount: float):
    account_number, balance = account
    balance -= amount
    return account_number, balance

account = (123456, 1000.0)
updated_account = deposit(account, 200.0)
print(updated_account)
updated_account = withdraw(account, 150.0)
print(updated_account)