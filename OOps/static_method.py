class ExpenseTracker:
    expense_tracker_version = 0.1
    def __init__(self, tracker_category, opening_balance, budget):
        # Instance/Object Attributes


        # public Attribute
        self.tracking_category = tracker_category

        # private Attribute
        self.__opening_balance = opening_balance
        self.__budget = budget

    # instance method
    # private method
    def __get_tracker_category(self):
        return self.__budget
    
    def check_balance(self, limit=1000):
        if self.__opening_balance >= limit:
            return True
        else:
            return False
    
    @staticmethod
    def convert_balance(amount):
        return float(amount)
    
    # Factory method
    @classmethod
    def get_attribute_fromstring(cls,diary_entry:str):
        tracking_category, opening_balance, tracker_budget = diary_entry.split(" ")

        return ExpenseTracker(tracking_category.capitalize(), 
                              cls.convert_balance(opening_balance),
                              cls.convert_balance(tracker_budget)
                              )

# obj1 = ExpenseTracker('home', 5000, 10000)
# print(obj1.get_tracker_category()) # Output: home
# print(obj1.check_balance()) # Output: True
# print(obj1.convert_balance(1000)) # Output: 1000.0

# ClassObject = ExpenseTracker.get_attribute_fromstring("shopping 100 5000")

# print(ClassObject.__dict__)
# ClassObject.tracking_category = 'Homing'
# print(ClassObject.tracking_category)
# print(ClassObject.__dict__)

home = ExpenseTracker('home', 1000, 5400)

print(home.tracking_category)
# print(home.__budget)
# print(home.__get_tracker_category())
print(home.__dict__)
print(home._ExpenseTracker__opening_balance)
print(home._ExpenseTracker__budget)
print(home._ExpenseTracker__get_tracker_category())
