# 🧾 Expense Tracker

A terminal program to record daily expenses and see your total spending and spending by category. Data is stored in a CSV file you can open in Excel or Google Sheets.

## Concepts Used
CSV • Functions • File handling

## Requirements
- Python 3.7+
- No external libraries (uses built-in `csv`, `os` and `datetime`)

## How to Run
```bash
python expense_tracker.py
```
On Mac/Linux use `python3`.

## Menu
```
1. Add Expense
2. View Expenses
3. Total Expense
4. Category Summary
5. Exit
```

## How It Works
- On first run, `expenses.csv` is created automatically with the headers: `date, category, description, amount`.
- **Add Expense:** asks for category, description and amount. Today's date is added automatically.
- **View Expenses:** reads the CSV with `csv.DictReader` and prints a formatted table.
- **Total Expense:** loops through every row and adds up the amounts.
- **Category Summary:** uses a dictionary to add up spending per category.
- Every expense is saved immediately, so nothing is lost if you close the program.

## Example
```
Category (food/travel/bills/etc.): food
Description: Lunch
Amount: 150
Expense added.
```

## Tips
- Keep category names consistent (`food`, not sometimes `Food`), so the summary groups correctly.
- Enter numbers only for the amount.
- Open `expenses.csv` in Excel or Google Sheets for charts and filters.
- To start fresh, delete `expenses.csv`.

## Ideas to Extend
- Filter expenses by month
- Set a monthly budget with an alert
- Delete or edit an expense
