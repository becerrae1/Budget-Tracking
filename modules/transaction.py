#store = input("What are you inputting?")

#This is list of dictionaries set up
#Want to add to this list by asking the user the key values and them inputting the values accordingly
#Then update the list with the transaction
#transactions = [{"Date": "2024-05-29", "Amount": 45.37, "Category": "Needs"},
#               {"Date": "2024-05-30", "Amount": 21.34, "Category": "Wants"},
#               {"Date": "2024-05-30", "Amount": 10.34, "Category": "Savings"}
               
#            ]

#Write a function that asks the user for transaction details (amount, category, date) and stores this data in a structured format.
def get_new_transaction():
    #Ask user for transaction amount
    amount = float(input('How much was it?'))
    # Ask user for transaction category
    category = input("Was it a want, need, or savings? ")

    # Validate category input
    while category not in ["want", "need", "savings"]:
        print("Invalid category. Please enter 'want', 'need', or 'savings'.")
        category = input("Was it a want, need, or savings? ")

    # Ask user for transaction date
    # Add functionality to check if its a valid number format
    date = input("What is today's date (e.g., YYYY-MM-DD)? ")

    while date not :
        print("Invalid date format please ensure it is in YYYY-MM-DD")
        date = input("What is today's date?")

    # Return a dictionary containing the transaction details
    return {
        "Amount": amount,
        "Category": category,
        "Date": date
    }

get_new_transaction()



#print(transaction["Date"])
#print(transactions[0]["Amount"], transactions[2]["Amount"])