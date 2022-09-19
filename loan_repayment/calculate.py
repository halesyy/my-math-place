
from math import floor
# from numba import jit

"""
As I've looked into purchasing property, I've noticed
something I'd like to understand more: mortgage repayments.
By building my own algorithm to calculating the monthly
cost for a mortgage/loan, I'll be able to find the perfect
config for a loan for my situation with the lowest interest
amount vs upfront capital.
"""

# Inputs.
interest_rate = 0.06 # 6% APY
principal = 150_000 # $100,000
pay_per_week = 500

# A list of all days in month.
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
assert sum(month_days) == 365, "Sum of month days incorrect."

# Our running balance.
running_balance = principal
total_paid = 0
pay_per_day = pay_per_week / 7

# Each month simulated.
months = 1
while running_balance > 0:
      for days in month_days:
            # First, calculate interest to add.
            interest_to_add = (running_balance * interest_rate / 365) * days
            
            # How much we plan to pay after this month.
            total_payment = pay_per_day * days
            
            # Running balance delta.
            running_balance += interest_to_add
            running_balance -= total_payment

            # Add to total paid
            total_paid += total_payment

            months += 1 # add month 

# Calculate after-the-fact.
total_interest_paid = total_paid - principal
delta = total_paid / principal

print(f"> This loan took:")
print(f"> {floor(months/12)} years and {months%12} months")
print(f"> Total interest paid was {total_interest_paid}")
print(f"> Total paid {total_paid}")
print(f"> Delta: {delta}")