import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"
HEADERS = ["date", "category", "description", "amount"]


def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)


def add_expense():
    category = input("Category (food/travel/bills/etc.): ")
    description = input("Description: ")
    amount = float(input("Amount: "))
    today = date.today().strftime("%Y-%m-%d")
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, category, description, amount])
    print("Expense added.")


def view_expenses():
    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        print("No expenses recorded.")
        return
    print(f"\n{'Date':<12}{'Category':<12}{'Description':<20}{'Amount':>10}")
    print("-" * 54)
    for row in rows:
        print(f"{row['date']:<12}{row['category']:<12}{row['description']:<20}{row['amount']:>10}")


def total_expense():
    total = 0
    with open(FILE_NAME, "r") as f:
        for row in csv.DictReader(f):
            total += float(row["amount"])
    print(f"Total spent: {total}")


def category_summary():
    summary = {}
    with open(FILE_NAME, "r") as f:
        for row in csv.DictReader(f):
            cat = row["category"]
            summary[cat] = summary.get(cat, 0) + float(row["amount"])
    if not summary:
        print("No expenses recorded.")
        return
    print("\n--- Spending by Category ---")
    for cat, amt in summary.items():
        print(f"{cat}: {amt}")


def main():
    init_file()
    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
