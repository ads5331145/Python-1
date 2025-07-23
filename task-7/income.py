def add_income(transactions, amount, source):
    """
    Adds a new income transaction.

    Args:
        transactions (list): List of all transactions.
        amount (float): Income amount.
        source (str): Source of income.
    """
    if amount <= 0:
        print("Error: Income amount must be positive.")
        return

    transactions.append({
        "type": "income",
        "amount": amount,
        "source": source
    })
    print("Income added successfully.")
