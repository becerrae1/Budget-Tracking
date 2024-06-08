from enum import Enum
import json

class Category(Enum):
    WANT = 'want'
    NEED = 'need'
    SAVINGS = 'savings'


#Save the transaction to JSON to have memory to draw on
#it is creating the JSON, but i should add a functionality to print current JSON file (current budget)
def save_transactions(transactions):
    with open('transactions.json', 'w') as f:
        json.dump(transactions, f, indent=4)

def load_transactions():
    try:
        with open('transactions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def display_transactions(transactions):
    if not transactions:  # Check if the transactions list is empty
        print("No transactions to display.")
        return

    for index, transaction in enumerate(transactions, 1):
        print(f"Transaction {index}:")
        print(f"  Date: {transaction['Date']}")
        print(f"  Amount: {transaction['Amount']}")
        print(f"  Category: {transaction['Category']}\n")

#Write a function that asks the user for transaction details (amount, category, date) and stores this data in a structured format.
def get_new_transaction():
    print("Enter transaction details: ")
    #Ask user for transaction amount
    amount = float(input('How much was it?'))
    # Ask user for transaction date
    # Add functionality to check if its a valid number format - still haven't done
    date = input("What is today's date (e.g., YYYY-MM-DD)? ")

    # Validate category input
    while True: 
        category_input = input("Was it a want, need, or savings?").lower()
        try:
            category = Category(category_input)
            break
        except ValueError:
            print("Invalid Category. Please enter 'want', 'need' or 'savings'. ")


    # Return a dictionary containing the transaction details
    return {
        "Amount": amount,
        "Category": category.value,
        "Date": date
    }

#holds the separate transactions
transactions = load_transactions()

#Function to add a transaction and append to the list
def add_transaction():
    new_trans = get_new_transaction()
    transactions.append(new_trans)
    print("Transaction added successfully")

#While loop to continuosly ask the user to add a transaction or not
while True:
    choice = input("What would you like view current budget list (a) or add a new transaction (b)")
    
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


#print(transaction["Date"])
#print(transactions[0]["Amount"], transactions[2]["Amount"])