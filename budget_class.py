class Budget:

    def __init__(self, income, expenses=None):
        if expenses is None:
            expenses = {}
        self.income = int(income)
        self.expenses = expenses

    def show_income(self):
        total_expenses = sum((self.expenses.values()))
        return f'Your current income is {self.income - total_expenses}'

    def add_expense(self, expense_name, expense_amount):
        self.expenses[expense_name] = int(expense_amount)
        total_expenses = sum((self.expenses.values()))
        gross_income = self.income - total_expenses
        if gross_income < 0:
            answer = input('This expense makes your income negative.\
                Are you sure you want to add this expense? Y/N').lower()
            if answer == 'y':
                return f'Your income less expenses is {gross_income}'
            if answer == 'n':
                self.expenses.popitem()
                return 'That expense was not added.'

    def remove_expense(self, expense_name):
        if expense_name in self.expenses:
            del self.expenses[expense_name]
            return self.expenses
        else:
            return "You don't have that as an expense!"

    def show_expenses(self):
        expense_tup = self.expenses.items()
        for key, value in expense_tup:
            print(key, ':', value)
        print(f'total expenses = {sum(self.expenses.values())}')

    def update_income(self, new_income):
        self.income = new_income

