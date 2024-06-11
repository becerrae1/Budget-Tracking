#Save the transaction to JSON to have memory to draw on
#it is creating the JSON, but i should add a functionality to print current JSON file (current budget)
import json
def save_transactions(transactions):
    with open('transactions.json', 'w') as f:
        json.dump(transactions, f, indent=4)

def load_transactions():
    try:
        with open('transactions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
#holds the separate transactions
transactions = load_transactions()