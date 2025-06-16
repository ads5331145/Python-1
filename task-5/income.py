from transactions_data import transactions

def add_income():
    amount = float(input("Enter income amount: ₹"))
    transactions.append({"type": "income", "amount": amount})
    print(" Income of {amount} added.")
