def add_expense(transactions):
    amount = float(input("Enter expense amount: ₹"))
    description = input("Enter description for expense: ")
    transactions.append(("expense", amount, description))
    print(f"Expense of ₹{amount} added.")
