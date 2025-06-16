from transactions import transactions
from csv_handler import overwrite_csv

def view_transactions():
    if not transactions:
        print("No transactions found.")
        return

    print("\n Transactions")
    for i, t in enumerate(transactions):
        print(f"{i+1}. {t['type'].capitalize()} - ₹{t['amount']} ({t['category']})")

def delete_transaction():
    view_transactions()
    if not transactions:
        return

    try:
        index = int(input("Enter the transaction number to delete: ")) - 1
        if 0 <= index < len(transactions):
            removed = transactions.pop(index)
            overwrite_csv(transactions)
            print(f"Deleted: {removed['type']} - ₹{removed['amount']} ({removed['category']})")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")
