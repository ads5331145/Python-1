def add_expense(transactions, amount, category):
    """
    Adds a new expense transaction.

    Args:
        transactions (list): List of all transactions.
        amount (float): Expense amount.
        category (str): Expense category.
    """
    if amount <= 0:
        print("Error: Expense amount must be positive.")
        return

    transactions.append({
        "type": "expense",
        "amount": amount,
        "category": category
    })
    print("Expense added successfully.")
