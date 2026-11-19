
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

CATEGORIES = ["Food", "Travel", "Study", "Bills", "Fun"]



# 1. CREATE CSV FILE IF IT DOES NOT EXIST

def create_file():

    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:

        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:

            fieldnames = ["date", "category", "description", "amount"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()



# 2. LOAD EXPENSES FROM CSV FILE


def load_expenses():

    create_file()

    expenses = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8-sig") as file:

            reader = csv.DictReader(file, skipinitialspace=True)

            for row in reader:

                # Ignore empty rows
                if not row or not row.get("date"):
                    continue

                try:
                    datetime.strptime(row["date"].strip(), "%Y-%m-%d")

                    amount = float(row["amount"])

                    if amount < 0:
                        continue

                    expenses.append({
                        "date": row["date"].strip(),
                        "category": row["category"].strip(),
                        "description": row["description"].strip(),
                        "amount": amount
                    })

                except (ValueError, TypeError, KeyError):
                    continue

    except OSError:
        print("Error reading expense file.")

    return expenses




# 3. SAVE AN EXPENSE TO CSV FILE

def save_expense(expense):

    create_file()

    fieldnames = ["date", "category", "description", "amount"]

    try:
        with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writerow(expense)

        print("\nExpense saved successfully!")

    except OSError:
        print("Error! Unable to save expense.")



# 4. ADD A NEW EXPENSE

def add_expense():

    print("\n========== ADD EXPENSE ==========")

    # Validate date
    while True:

        date_input = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date! Use YYYY-MM-DD format.")

    # Display available categories
    print("\nAvailable Categories:")

    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")

    # Validate category
    while True:

        try:
            choice = int(input("Select category (1-5): "))

            if 1 <= choice <= len(CATEGORIES):
                category = CATEGORIES[choice - 1]
                break

            else:
                print("Please select a number between 1 and 5.")

        except ValueError:
            print("Invalid input! Enter a number.")

    # Get description
    while True:

        description = input("Enter expense description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    # Validate amount
    while True:

        try:
            amount = float(input("Enter amount: "))

            if amount < 0:
                print("Amount cannot be negative.")

            elif amount == float("inf") or amount != amount:
                print("Please enter a valid amount.")

            else:
                break

        except ValueError:
            print("Invalid amount! Enter a numeric value.")

    # Create expense dictionary
    expense = {
        "date": date_input,
        "category": category,
        "description": description,
        "amount": amount
    }

    save_expense(expense)


# ==========================================
# 5. DISPLAY ALL EXPENSES
# ==========================================

def view_expenses(expenses):

    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses found.")
        return

    print("-" * 75)

    print(f"{'Date':<14}{'Category':<12}{'Description':<25}{'Amount':>12}")

    print("-" * 75)

    for expense in expenses:

        print(
            f"{expense['date']:<14}"
            f"{expense['category']:<12}"
            f"{expense['description'][:24]:<25}"
            f"{expense['amount']:>12.2f}"
        )

    print("-" * 75)


# ==========================================
# 6. FILTER EXPENSES
# ==========================================

def filter_expenses(expenses):

    print("\n========== FILTER EXPENSES ==========")

    print("1. Filter by Category")
    print("2. Filter by Month")

    choice = input("Enter your choice: ")

    filtered = []

    if choice == "1":

        category = input("Enter category name: ").strip().lower()

        filtered = [
            expense for expense in expenses
            if expense["category"].lower() == category
        ]

    elif choice == "2":

        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")

            filtered = [
                expense for expense in expenses
                if expense["date"][:7] == month
            ]

        except ValueError:
            print("Invalid month format! Use YYYY-MM.")
            return

    else:
        print("Invalid choice!")
        return

    print("\nFiltered Results:")

    view_expenses(filtered)

    if filtered:
        total = sum(expense["amount"] for expense in filtered)
        print(f"Filtered total: Rs. {total:.2f}")


# ==========================================
# 7. EXPENSE SUMMARY
# ==========================================

def expense_summary(expenses):

    print("\n========== EXPENSE SUMMARY ==========")

    if not expenses:
        print("No expenses available for summary.")
        return

    category_totals = {}

    grand_total = 0

    # Calculate category-wise totals
    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount

        else:
            category_totals[category] = amount

        grand_total += amount

    print("\nCategory-wise Spending:")

    for category, total in category_totals.items():

        print(f"{category:<15} Rs. {total:.2f}")

    print("\nGrand Total: Rs.", f"{grand_total:.2f}")

    # Find biggest expense
    biggest = max(expenses, key=lambda expense: expense["amount"])

    print("\nBiggest Single Expense:")

    print("Category:", biggest["category"])
    print("Description:", biggest["description"])
    print("Amount: Rs.", f"{biggest['amount']:.2f}")
    print("Date:", biggest["date"])


# ==========================================
# 8. MAIN MENU
# ==========================================

def main():

    create_file()

    while True:

        print("\n======================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("======================================")

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Expense Summary")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ")

        # Reload data to include saved expenses
        expenses = load_expenses()

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses(expenses)

        elif choice == "3":

            filter_expenses(expenses)

        elif choice == "4":

            expense_summary(expenses)

        elif choice == "5":

            print("\nThank you for using Personal Expense Tracker!")
            print("Your expenses have been saved.")
            break

        else:

            print("Invalid choice! Please select between 1 and 5.")




if __name__ == "__main__":
    main()
