from csv_handler import write_transaction_to_csv

def add_expense(transactions):
    """
    Prompt user to add an expense and update both memory and CSV.

    Args:
        transactions (list): List of transaction dictionaries.
    """
    amount_input = input("Enter expense amount: ")
    if amount_input.replace('.', '', 1).isdigit():
        amount = float(amount_input)
        category = input("Enter expense category: ")
        transaction = {"type": "expense", "amount": amount, "category": category}
        transactions.append(transaction)
        write_transaction_to_csv(transaction)
        print("Expense added successfully!")
    else:
        print("Invalid amount. Must be a number.")