# First Challenge Project at Columbia Engineering Fintech Program: Valuing Microcredit Loans for a Lending Startup

In this project, I will do the following:

Part 1: Automate the Calculations.

Firstly, I will start some calculations on a list of prices for 5 loans.

1. Use the `len` function to calculate the total number of loans in the list.
2. Use the `sum` function to calculate the total of all loans in the list.
3. Using the sum of all loans and the total number of loans, calculate the average loan price. 4. Print all calculations with descriptive messages.

"""Part 2: Analyze Loan Data.

Secondly, I will analyze the loan to determine the investment evaluation.

1. I will use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
   a. Save these values as variables called `future_value` and `remaining_months`.
   b. Print each variable.
   **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
   **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
   a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
   b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

@NOTE:
If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
   a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
   b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
   a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.

"""

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
   a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
   b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.

"""

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file 1. Use `with open` to open a new CSV file.
a. Create a `csvwriter` using the `csv` library.
b. Use the new csvwriter to write the header variable as the first row.
c. Use a for loop to iterate through each loan in `inexpensive_loans`.
i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

Refer to the official documentation for the csv library.https://docs.python.org/3/library/csv.html#writer-objects

---

## Technologies

I have a dev environment activated on my system with the Python 3.7.13 version.

---

## Installation Guide

Git clone the repo, and run it, pursuant to the following:

```
git clone https://github.com/JeffSmith-ok/Module_1_Challenge.git

cd Module_1_Challenge

python loan_analyzer.py

```

---

## Usage

## ![Screenshot of the loan_analyzer.py and the gitbash terminal](<images/Screenshot(5).jpg>)

## Contributors

This is the first of the individual learning challenges.

My contact information is:

Linkedin: https://www.linkedin.com/in/jeffsmith77/ </br>
Personal email: jmstranslate@gmail.com </br>
Phone: 332 238 5209

---

## License

MIT License

Copyright (c) 2022 Jeffrey M. Smith
