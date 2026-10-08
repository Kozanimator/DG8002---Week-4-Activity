# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Stephan kozak
# Date: 2026 10 08

# SCENARIO
# You are wanting to save money for a particular purchase.
# Write a program that estimates how long it will take to grow your money to your desired amount.
# Consider 


# TODO 1: Create inputs for the following information 
#         - Your desired savings goal
#         - The amount of money as your base investment
#         - The annual interest rate
#         - The amount of money you want to deposit into the account every month (if any)
savings_goal = float(input("Desired savings goal ($): "))
base_investment = float(input("Base investment ($): "))
annual_interest_rate = float(input("Annual interest rate (enter 4 for 4%): "))
monthly_deposit = float(input("Monthly deposit ($, enter 0 for none): "))

# TODO 2: Create variables to hold number of months and current balance of the account
months = 0
current_balance = base_investment
monthly_interest_rate = annual_interest_rate / 100 / 12

# TODO 3: Create a loop that will run until you have made at least your desired savings goal
if savings_goal <= 0 or base_investment < 0 or annual_interest_rate < 0 or monthly_deposit < 0:
    print("Enter a positive savings goal and non-negative investment, rate, and deposit.")
elif current_balance < savings_goal and monthly_deposit == 0 and ( annual_interest_rate == 0 or base_investment == 0):
    print("The goal cannot be reached without a deposit or an investment earning interest.")
else:
    while current_balance < savings_goal:

    # TODO 4: Calculate amount of money earned that month through interest on your base investment and monthly deposit
   current_balance += monthly_deposit
   monthly_interest = current_balance * monthly_interest_rate
   current_balance += monthly_interest

    # TODO 5: Increment the number of times the loop has run so you can track how many months it takes to hit your goal
    months += 1

# TODO 6:  Print how long it will take for your investment to mature.  
#          If the duration is longer than 12 months, print your result in years.  Otherwise, print the result in months.
 if months > 12:
        years = months / 12
        print(f"Time to reach your goal: {years:.2f} years ({months} months)")
 else:
        print(f"Time to reach your goal: {months} months")
    print(f"Final balance: ${current_balance:,.2f}")

# EXPECTED OUTPUT
# GOAL: $1,000,000
# INTEREST: 4%
# BASE: $1,000
# MONTHLY DEPOSIT: $100
#
# Number of Months: 177
# Number of Years: 87.75
# Total Investment: $1,034,906.36

