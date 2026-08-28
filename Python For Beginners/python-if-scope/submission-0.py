def pay_bill(balance: int, bill: int) -> int:
    if balance >= bill:
        new_balance = balance - bill
        return new_balance
    return balance


# do not modify below this line
print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))
