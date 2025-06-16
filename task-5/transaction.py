from transactions_data import transactions

def view_transactions():
    if not transactions:
        print(" No transactions to show.")
        return
    for i, txn in enumerate(transactions, 1):
        print(f"{i}. {txn['type'].capitalize()} - ₹{txn['amount']}")

def delete_transaction():
    view_transactions()
    try:
        index = int(input("Enter transaction number to delete: "))
        if 1 <= index <= len(transactions):
            removed = transactions.pop(index - 1)
            print(" Deleted: {removed['type']} ₹{removed['amount']}")
        else:
            print("Invalid transaction number.")
    except ValueError:
        print("Please enter a valid number.")
