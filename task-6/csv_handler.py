import csv
import os

CSV_FILE = "transactions.csv"

def load_transactions_from_csv():
    """
    Load transactions from a CSV file.

    Returns:
        list: List of transactions as dictionaries.
    """

    transactions = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert amount to float while reading
                transactions.append({
                    "type": row["type"],
                    "amount": float(row["amount"]),
                    "category": row["category"]
                })
    return transactions

def write_transaction_to_csv(transaction):
    """
    Append a single transaction to the CSV file.

    Args:
        transaction (dict): A single transaction dictionary.
    """
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        fieldnames = ["type", "amount", "category"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(transaction)

def overwrite_csv(transactions):
    """
    Overwrite the CSV file with the updated list of transactions.

    Args:
        transactions (list): All current transactions to write to file.
    """

    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ["type", "amount", "category"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for t in transactions:
            writer.writerow(t)
