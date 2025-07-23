from csv_handler import write_transaction_to_csv

def add_income(transactions):
    """
    Prompt user to add income and update both memory and CSV.

    Args:
        transactions (list): List of transaction dictionaries.
    """
    amount_input = input("Enter income amount: ")
    if amount_input.replace('.', '', 1).isdigit():
        amount = float(amount_input)
        category = input("Enter income category: ")
        transaction = {"type": "income", "amount": amount, "category": category}
        transactions.append(transaction)
        write_transaction_to_csv(transaction)
        print("Income added successfully!")
    else:
        print("Invalid amount. Must be a number.")

