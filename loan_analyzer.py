# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations."""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
print(f"The total number of loans is: {len(loan_costs)}")

# What is the total of all loans?
# Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
print(f"The sum of all loans is: ${sum(loan_costs)}")

# What is the average loan amount from the list?
# Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount.

print(
    f"The average loan amount is: ${(sum(loan_costs)/len(loan_costs))}")


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.


future_value = loan.get("future_value")
print(f"The future value of the loan is: ${future_value}")
remaining_months = loan.get("remaining_months")
loan_price = loan.get("loan_price")
print(f"The loan price is equal to: ${loan_price}")

# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

present_value = future_value / (1 + .20/12)**remaining_months
print(f"The fair or present value of the loan is: ${present_value: .2f}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

if present_value >= loan_price:
    print(f"Because the present value is greater than or equal to the loan price, the loan is worth at least the cost to buy it")
else:
    print(f"The present value of the loan is less than the loan cost, the loan is too expensive and not worth the price.")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.


# Given the following loan data, I will need to calculate the present value for the loan"""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.


def present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / \
        (1 + annual_discount_rate/12)**remaining_months
    # print(present_value)
    return present_value

# Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.


present_value(1000, 12, 0.2)

"""Part 4: Conditionally filter lists of loans.

In this section, I will use a loop to iterate through a series of loans and select only the inexpensive loans.

"""
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`

inexpensive_loans = []


# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list

for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)
# Print the `inexpensive_loans` list

print(f"The inexpensive loans are as follows: {inexpensive_loans}")

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    
"""

# Set the output header
header = ["loan_price", "remaining_months",
          "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())
