#store = input("What are you inputting?")

#This is list of dictionaries set up
#Want to add to this list by asking the user the key values and them inputting the values accordingly
#Then update the list with the transaction
#transactions = [{"Date": "2024-05-29", "Amount": 45.37, "Category": "Needs"},
#               {"Date": "2024-05-30", "Amount": 21.34, "Category": "Wants"},
#               {"Date": "2024-05-30", "Amount": 10.34, "Category": "Savings"}
               
#            ]

from enum import Enum

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
    # Add functionality to check if its a valid number format
    date = input("What is today's date (e.g., YYYY-MM-DD)? ")

    # Validate category input
    while True: 
        category_input = input("Was it a want, need, or savings?").lower()
        try:
            category = Category(category_input)
            break
        except ValueError:
            print("Invalid Category. Please enter 'want', 'need' or 'savings'. ")



    #while date not :
    #    print("Invalid date format please ensure it is in YYYY-MM-DD")
    #    date = input("What is today's date?")

    # Return a dictionary containing the transaction details
    return {
        "Amount": amount,
        "Category": category.value,
        "Date": date
    }

transactions = []

def add_transaction():
    new_trans = get_new_transaction()
    transactions.append(new_trans)
    print("Transaction added successfully")

#Example of invoking the function and storing it in a list for future use
add_transaction()
print(transactions)


#print(transaction["Date"])
#print(transactions[0]["Amount"], transactions[2]["Amount"])