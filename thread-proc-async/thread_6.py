from time import sleep
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

account_balance = 1000


# def update_money(transaction, amount):
#     global account_balance
#     print(f"Transaction: {transaction}, Amount: {amount}")
#     account_balance_copy = account_balance
#     account_balance_copy += amount
#     sleep(2)
#     account_balance += amount
#     print(f"Updated account balance: {account_balance}")


def update_money(lock, transaction, amount):
    global account_balance
    print(f"Transaction: {transaction}, Amount: {amount}")
    with lock:
        account_balance_copy = account_balance
        account_balance_copy += amount
        sleep(2)
        account_balance = account_balance_copy


# update_money("Deposit", 500)
# update_money("Withdrawal", -200)

if __name__ == "__main__":
    lock = Lock()
    transactions = [("Deposit", 500), ("Withdrawal", -200)]
    with ThreadPoolExecutor(max_workers=2) as executor:
        for transaction, money in transactions:
            executor.submit(update_money, lock, transaction, money)
    print(f"Final account balance: {account_balance}")
