# class ExpenseTracker:
# #     """This is a class to do expense tracking"""
# #     def __init__(self):
# #         pass


# # obj1 = ExpenseTracker()

# class ExpenseTracker:
#     """This is a class to do expense tracking"""
#     def __init__(self, date, description, transaction_type, amount):
#         self.date = date
#         self.description = description
#         self.transaction_type = transaction_type
#         self.amount = amount


# obj2 = ExpenseTracker('12jan', 'Dinner with Friends', 'Debit', '500')
# print(obj2.date)
# obj3 = ExpenseTracker('1May', 'Salary Credited', 'credited', '30000')
# print(obj3.description)

# Attribute

class ExpenseTracker:

    #class Attribute
    expense_tracker_version = 0.1

    def __init__(self, tracker_category, opening_balance, budget):
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

home_tracker = ExpenseTracker('home', 3000, 10000)
# print(home_tracker.tracker_category)
# shopping_category = ExpenseTracker('shopping', 1000, 10000)
# print(shopping_category.opening_balance)
# print(home_tracker.__dict__)
# print(shopping_category.__dict__)
# print(home_tracker.__dir__)
print(getattr(home_tracker,'opening_balance'))
print(hasattr(home_tracker,'opening_balance'))
print(home_tracker.__dict__)
print(delattr(home_tracker,'opening_balance'))
print(home_tracker.__dict__)
