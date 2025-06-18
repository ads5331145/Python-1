def view_balance(transactions):
    income_total = sum(txn[1] for txn in transactions if txn[0] == "income")
    expense_total = sum(txn[1] for txn in transactions if txn[0] == "expense")
    balance = income_total - expense_total
    print(f"Total Income: ₹{income_total}")
    print(f"Total Expense: ₹{expense_total}")
    print(f"Balance: ₹{balance}")
