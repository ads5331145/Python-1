# Prompt user for basic info
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # int type
balance = float(input("Enter your current balance: "))  # float type

# Prompt for boolean preference
alerts_input = input("Do you want to receive transaction alerts? (yes/no): ")
receive_alerts = alerts_input.lower() == "yes"  # bool type

# Prompt for first transaction
t1_amount = float(input("Enter amount for transaction 1: "))
t1_type = input("Enter type for transaction 1 (credit/debit): ")

# Prompt for second transaction
t2_amount = float(input("Enter amount for transaction 2: "))
t2_type = input("Enter type for transaction 2 (credit/debit): ")

# Print summary
print("\n Summary")
print("Name:", name)
print("Age:", age)
print("Current Balance:", balance)
print("Wants Transaction Alerts:", receive_alerts)
print("Transaction 1 - Amount:", t1_amount, ", Type:", t1_type)
print("Transaction 2 - Amount:", t2_amount, ", Type:", t2_type)

