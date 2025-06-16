from transactions import transactions
from csv_handler import write_transaction_to_csv

def add_income():
    amount = float(input("Enter income amount: "))
    category = input("Enter income category: ")

    transaction = {"type": "income", "amount": amount, "category": category}
    transactions.append(transaction)
    write_transaction_to_csv(transaction)

    print("Income added successfully!")
