from csv_handler import overwrite_csv

def view_transactions(transactions):
    """
    Display all transactions in a formatted list.

    Args:
        transactions (list): List of transaction dictionaries.
    """
    if not transactions:
        print("No transactions found.")
        return

    print("\nTransactions:")
    for i, t in enumerate(transactions):
        print(f"{i+1}. {t['type'].capitalize()} - ₹{t['amount']} ({t['category']})")

def delete_transaction(transactions):
    """
    Delete a transaction by its index from the list and update CSV.

    Args:
        transactions (list): List of transaction dictionaries.
    """
    view_transactions(transactions)
    if not transactions:
        return

    index_input = input("Enter the transaction number to delete: ")

    if index_input.isdigit():
        index = int(index_input) - 1

        if 0 <= index < len(transactions):
            removed = transactions.pop(index)
            overwrite_csv(transactions)
            print(f"Deleted: {removed['type']} - ₹{removed['amount']} ({removed['category']})")
        else:
            print("Invalid index. No transaction at that number.")
    else:
        print("Please enter a valid numeric index.")
