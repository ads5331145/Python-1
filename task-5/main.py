from income import add_income
from expense import add_expense
from transaction import view_transactions, delete_transaction
from balance import view_balance

def main():
    transactions = []

    while True:
        print("\nFinance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Delete Transaction")
        print("5. View Balance")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_income(transactions)
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            view_transactions(transactions)
        elif choice == "4":
            delete_transaction(transactions)
        elif choice == "5":
            view_balance(transactions)
        elif choice == "6":
            print("Exiting Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
