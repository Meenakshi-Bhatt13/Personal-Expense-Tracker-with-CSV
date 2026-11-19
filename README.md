# Personal Expense Tracker with CSV

## Project Overview
The Personal Expense Tracker is a Python-based command-line application that helps users record, manage, filter, and analyze their daily expenses.

All expenses are stored in a CSV file, so the data remains available even after the program is closed.

## Features
- Add new expenses.
- View all recorded expenses.
- Filter expenses by category.
- Filter expenses by month.
- Calculate category-wise spending.
- Display total expenditure.
- Identify the biggest single expense.
- Validate dates and amounts.
- Automatically create the CSV file if it does not exist.

## Technologies Used
- Python
- CSV Module
- Datetime Module
- OS Module

## Expense Categories
1. Food
2. Travel
3. Study
4. Bills
5. Fun

## Project Structure
- expense_tracker.py – Main Python application.
- expenses.csv – Stores expense records.
- README.md – Project documentation.

## How to Run
1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute:

   `python expense_tracker.py`

## CSV Format
Each expense contains four fields:
- Date (YYYY-MM-DD)
- Category
- Description
- Amount

## Sample Scoring / Calculations
The application calculates total spending by category, the overall expenditure, and the largest individual expense.
