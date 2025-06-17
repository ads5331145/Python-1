# Store all transactions in a list
transactions = []

# Store unique descriptions using a set
descriptions_set = set()

while True:
    print("\n Transaction Menu")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        # Take user input
        amount = float(input("Enter amount: "))
        t_type = input("Enter type (Income or Expense): ")
        desc = input("Enter description: ")

        # Create a transaction dictionary
        transaction = {
            "amount": amount,
            "type": t_type,
            "description": desc
        }

        # Add transaction to list
        transactions.append(transaction)

        # Add description to set
        descriptions_set.add(desc)

        print("Transaction added.")

    elif choice == "2":
        print("\n All Transactions")

        if not transactions:
            print("No transactions yet.")
        else:
            for t in transactions:
                # Using tuple to display
                txn_tuple = (t['amount'], t['type'], t['description'])
                print("Amount: ₹", txn_tuple[0], "| Type:", txn_tuple[1], "| Description:", txn_tuple[2])

    elif choice == "3":
        print("Exiting..")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
