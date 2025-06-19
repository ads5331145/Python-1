def calculate_balance(transactions):
    """
    Calculates and returns the balance from all transactions.
    """
    income = sum(txn["amount"] for txn in transactions if txn["type"] == "income")
    expense = sum(txn["amount"] for txn in transactions if txn["type"] == "expense")
    return income - expense
