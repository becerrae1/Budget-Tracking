from enum import Enum
import json
from data_manager import load_transactions 

class Category(Enum):
    WANT = 'want'
    NEED = 'need'
    SAVINGS = 'savings'


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

transactions = load_transactions()

#Function to add a transaction and append to the list
def add_transaction():
    new_trans = get_new_transaction()
    transactions.append(new_trans)
    print("Transaction added successfully")


#print(transaction["Date"])
#print(transactions[0]["Amount"], transactions[2]["Amount"])