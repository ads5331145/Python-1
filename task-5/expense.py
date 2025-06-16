from transactions import transactions

def add_expense():
    amount = float(input("Enter expense amount: ₹"))
    transactions.append({"type": "expense", "amount": amount})
    print(" Expense of ₹{amount} added.")
