def calculate_balance(transactions):
    """
    Calculates and returns the balance from all transactions.
    Handles empty or invalid input gracefully.
    """
    if not isinstance(transactions, list) or not transactions:
        return 0.0  # empty or invalid input

    income = sum(txn["amount"] for txn in transactions if txn.get("type") == "income")
    expense = sum(txn["amount"] for txn in transactions if txn.get("type") == "expense")
    return income - expense
