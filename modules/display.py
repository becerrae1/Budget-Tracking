def display_transactions(transactions):
    if not transactions:  # Check if the transactions list is empty
        print("No transactions to display.")
        return

    for index, transaction in enumerate(transactions, 1):
        print(f"Transaction {index}:")
        print(f"  Date: {transaction['Date']}")
        print(f"  Amount: {transaction['Amount']}")
        print(f"  Category: {transaction['Category']}\n")