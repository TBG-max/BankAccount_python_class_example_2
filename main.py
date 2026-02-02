# main.py
import os
os.system("clear")
# Do not modify code above this line.

from module import BankAccount

# TODO 1: Account holder names are not being printed correctly in Section 1.
# TODO 2: Balances are not updating correctly after deposits in Section 3.
# TODO 3: Withdrawals allow the balance to go negative in Section 2.
# TODO 4: The greeting method is not displaying anything in Section 1.

# Create account instances
a1 = BankAccount("Jordan", 250)
a2 = BankAccount("Casey", 100)

print("SECTION 1\n")
print("Account Holder:", a1.owner)
print("Balance:", a1.balance)
a1.greet()

print()

print("Account Holder:", a2.owner)
print("Balance:", a2.balance)
a2.greet()

print("-----------------------------------\n")

print("SECTION 2\n")
print("Jordan withdraws 300...")
a1.withdraw(300)
print("Jordan's Balance After Withdrawal:", a1.balance)

print()

print("Casey withdraws 50...")
a2.withdraw(50)
print("Casey's Balance After Withdrawal:", a2.balance)

print("-----------------------------------\n")

print("SECTION 3\n")
a1.deposit(100)
print("Jordan's Balance After Deposit:", a1.balance)

a2.deposit(25)
print("Casey's Balance After Deposit:", a2.balance)
