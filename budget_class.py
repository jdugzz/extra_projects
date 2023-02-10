class Budget:

    def __init__(self, income, expenses=None):
        if expenses is None:
            expenses = {}
        self.income = int(income) # consider income to be float
        self.expenses = expenses

    def show_income(self):
        ''' calculates the gross income (income minus expenses)
            and returns a string representation of it.
        '''
        total_expenses = sum((self.expenses.values()))
        return f'Your current income is {self.income - total_expenses}'

    def add_expense(self, expense_name, expense_amount):
        ''' adds a new expense to the expenses dictionary and updates the gross income.
            If the gross income becomes negative,
            it prompts the user to confirm the expense before adding it.
        '''
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
        ''' removes an expense from the expenses dictionary,
            and returns the updated expenses.
            If the specified expense does not exist, it returns an error message.
        '''
        if expense_name in self.expenses:
            del self.expenses[expense_name]
            return self.expenses
        return "You don't have that as an expense!"

    def show_expenses(self):
        ''' displays all expenses and the total expenses. '''
        expense_tup = self.expenses.items()
        for key, value in expense_tup:
            print(key, ':', value)
        return f'total expenses = {sum(self.expenses.values())}'

    def update_income(self, new_income):
        ''' updates the income. '''
        self.income = new_income
