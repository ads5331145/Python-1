import csv  # Imported at the top

def view_transactions(transactions):
    """
    Displays all transactions.
    """
    if not transactions:
        print("No transactions found.")
        return

    print("All Transactions:")
    for idx, txn in enumerate(transactions, 1):
        print(f"{idx}. {txn}")


def save_transactions_to_file(transactions, filename):
    """
    Saves transactions to a file in CSV format.
    """
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["type", "amount", "source", "category"])
            writer.writeheader()
            for txn in transactions:
                writer.writerow(txn)
        print("Transactions saved successfully.")
    except IOError:
        print(f"Error: Could not write to file {filename}.")


def load_transactions_from_file(filename):
    """
    Loads transactions from a CSV file.

    Returns:
        List of transactions or empty list if file fails to load.
    """
    transactions = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                txn = {
                    "type": row["type"],
                    "amount": float(row["amount"]),
                    "source": row.get("source", ""),
                    "category": row.get("category", "")
                }
                transactions.append(txn)
    except FileNotFoundError:
        print(f"Warning: File {filename} not found. Starting with an empty transaction list.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return transactions
