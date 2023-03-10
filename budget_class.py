class Budget:
    """
    The Budget class is used to keep track of a person's income and expenses.

    Attributes:
    - income (float): the total income of the person
    - expenses ( Dict): a dictionary containing the expenses and their amounts
    """

    def __init__(self, income, expenses=None):
        if expenses is None:
            expenses = {}
        self.income = int(income) # consider income to be float
        self.expenses = expenses

    def show_income(self):
        ''' calculates the gross income (income minus expenses)
            and returns a string representation of it.
        Returns:
            - str: the string that shows the person's current income after
            subtracting the expenses from their income
        '''
        total_expenses = sum((self.expenses.values()))
        return f'Your current income is {self.income - total_expenses}'

    def add_expense(self, expense_name, expense_amount):
        ''' adds a new expense to the expenses dictionary and updates the gross income.
            If the gross income becomes negative,
            it prompts the user to confirm the expense before adding it.
        Parameters:
            - expense_name (str): the name of the expense to be added
            - expense_amount (float): the amount of the expense to be added

        Returns:
            - str: a string indicating the success of the operation
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
        Parameters:
            - expense_name (str): the name of the expense to be removed
        Returns:
            - Union[Dict, str]: a dictionary containing the remaining
            expenses or a string indicating that the expense does not exist
        '''
        if expense_name in self.expenses:
            del self.expenses[expense_name]
            return self.expenses
        return "You don't have that as an expense!"

    def show_expenses(self):
        ''' displays all expenses and the total expenses.
        #TODO: add a detailed documentation following the above format.
        '''
        expense_tup = self.expenses.items()
        for key, value in expense_tup:
            print(key, ':', value)
        return f'total expenses = {sum(self.expenses.values())}'

    def update_income(self, new_income):
        ''' updates the income. 
        #TODO: add a detailed documentation following the above format.
        '''
        self.income = new_income
