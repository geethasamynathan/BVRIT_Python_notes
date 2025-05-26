def calculate_tax(income, tax_rate):
    """
    Calculate the tax owed based on income and tax rate.

    Parameters:
    income (float): The total income.
    tax_rate (float): The tax rate as a decimal (e.g., 0.2 for 20%).

    Returns:
    float: The amount of tax owed.
    """
    if income < 0 or tax_rate < 0:
        raise ValueError("Income and tax rate must be non-negative.")
    
    return income * tax_rate