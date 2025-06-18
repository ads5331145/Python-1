def view_transactions(transactions):
    if not transactions:
        print(" No transactions found.")
        return

    print("All Transactions:")
    for idx, txn in enumerate(transactions):
        print(f"{idx + 1}. Type: {txn[0]} | Amount: ₹{txn[1]} | Description: {txn[2]}")

def delete_transaction(transactions):
    if not transactions:
        print("No transactions to delete.")
        return

    view_transactions(transactions)
    index = int(input("Enter transaction number to delete: ")) - 1

    if 0 <= index < len(transactions):
        removed = transactions.pop(index)
        print(f"Deleted transaction: {removed}")
    else:
        print(" Invalid transaction number.")

