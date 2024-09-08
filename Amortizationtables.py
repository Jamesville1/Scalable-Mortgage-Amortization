import pandas as pd
import numpy as np
import numpy_financial as npf

def create_amortization_table(principal, annual_rate, years, payments_per_year):
    # Calculate constants
    n_periods = int(years * payments_per_year)
    rate_per_period = annual_rate / payments_per_year

    # Calculate payment per period
    payment = npf.pmt(rate_per_period, n_periods, -principal)

    # Initialize DataFrame to store amortization schedule
    amortization_table = pd.DataFrame(index=range(1, n_periods + 1),
                                      columns=['Payment', 'Principal Payment', 'Interest Payment', 'Ending Balance'])
    
    # Initial balance is the principal
    balance = principal

    # Calculate the amortization schedule
    for period in range(1, n_periods + 1):
        # Interest payment for the current period
        interest_payment = npf.ipmt(rate_per_period, period, n_periods, -principal)
        
        # Principal payment for the current period
        principal_payment = npf.ppmt(rate_per_period, period, n_periods, -principal)
        
        # Ending balance after the payment. Made a change hereeeeeeee
        balance -= principal_payment
        
        # Fill the DataFrame with the computed values
        amortization_table.loc[period] = [payment, principal_payment, interest_payment, balance]
    
    return amortization_table