from transactions import transactions
from csv_handler import write_transaction_to_csv

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    transaction = {"type": "expense", "amount": amount, "category": category}
    transactions.append(transaction)
    write_transaction_to_csv(transaction)

    print("Expense added successfully!")
