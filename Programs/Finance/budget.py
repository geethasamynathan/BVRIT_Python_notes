def budget_calculator(income, expenses):
    """
    Calculate the budget balance.

    Parameters:
    income (float): Total income for the period.
    expenses (float): Total expenses for the period.

    Returns:
    float: The budget balance (income - expenses).
    """
    if not isinstance(income, (int, float)) or not isinstance(expenses, (int, float)):
        raise ValueError("Income and expenses must be numeric values.")
    
    return income - expenses