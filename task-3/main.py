print("Welcome to Menu driven program")

last_type = ""
last_amount = 0.0

while True:
    print("\n Menu")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Last Transaction")
    print("4. Loop Counter")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        last_type = "Income"
        last_amount = amount
        print("Income added.")

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        last_type = "Expense"
        last_amount = amount
        print("Expense added.")

    elif choice == "3":
        if last_type == "":
            print("No transaction yet.")
        else:
            print(f"Last Transaction - {last_type}: ₹{last_amount}")

    elif choice == "4":
        print("Loop Counter Example (1 to 10):")
        for i in range(1, 11):  # For loop example
            print("Count:", i)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid input. Please Try again.")
        continue
