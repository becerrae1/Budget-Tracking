from transaction import get_new_transaction, add_transaction
from display import display_transactions
from data_manager import save_transactions, load_transactions
import json


transactions = load_transactions()

#While loop to continuosly ask the user to add a transaction or not
while True:
    choice = input("What would you like view current budget list (a) or add a new transaction (v)")
    
    if choice == "a":
        add_transaction()
        continue_input = input("Do you want to add another transaction? (y/n): ")
        if continue_input != "y":
            save_transactions(transactions)
            break
    if choice == "v":
        display_transactions(transactions)
#Prints final list after breaking the while loop
print("Final list of Transactions: ")
for trans in transactions:
    print(trans)
