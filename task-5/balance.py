from transactions_data import transactions

def view_balance():
    income = sum(txn["amount"] for txn in transactions if txn["type"] == "income")
    expense = sum(txn["amount"] for txn in transactions if txn["type"] == "expense")
    balance = income - expense
    print(f"\n Balance Summary:\nIncome: ₹{income} | Expense: ₹{expense} | Balance: ₹{balance}")
