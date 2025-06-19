from income import add_income
from expense import add_expense
from balance import calculate_balance
from transaction import view_transactions, save_transactions_to_file, load_transactions_from_file

def main():
    transactions = load_transactions_from_file("transactions.csv")

    while True:
        print("\n--- Finance Tracker Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Enter income amount: "))
                source = input("Enter income source: ")
                add_income(transactions, amount, source)
            except ValueError:
                print("Invalid input: Please enter a numeric value for amount.")

        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                add_expense(transactions, amount, category)
            except ValueError:
                print("Invalid input: Please enter a numeric value for amount.")

        elif choice == "3":
            view_transactions(transactions)

        elif choice == "4":
            balance = calculate_balance(transactions)
            print(f"Current Balance: ₹{balance:.2f}")

        elif choice == "5":
            save_transactions_to_file(transactions, "transactions.csv")
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
