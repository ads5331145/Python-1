def add_income(transactions):
    amount = float(input("Enter income amount: ₹"))
    description = input("Enter description for income: ")
    transactions.append(("income", amount, description))
    print(f" Income of ₹{amount} added.")
