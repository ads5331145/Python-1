def view_balance(transactions):
    """
    Calculate and display the total income, expenses, and current balance.

    Args:
        transactions (list): List of transaction dictionaries.
    """

    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense

    print(f"\nTotal Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Current Balance: ₹{balance}")
