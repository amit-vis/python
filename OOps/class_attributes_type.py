class ExpenseTracker:
    # class Attribute
    expense_version_tracker = 0.1
    """class Expense Tracker"""
    def __init__(self, tracker_category, opening_balance, budget):
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

home_tracker = ExpenseTracker('home', 1000, 10000)
shopping_tracker = ExpenseTracker('shopping', 500, 100000)
print(home_tracker.expense_version_tracker)

home_tracker.expense_version_tracker = 0.2
print(home_tracker.expense_version_tracker)
print(shopping_tracker.expense_version_tracker)