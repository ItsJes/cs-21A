# -----------------------------------------------------------------------------
# Name:        Tax
# Purpose:     Calculate Tax
#
# Author:      Jessica Sendejo
# Date:        04/16/2017
# -----------------------------------------------------------------------------
"""
California Tax Calculator

This calculates the tax of California that is 8.75 of any given number.
First asked for the amount.
Then calculates the amount and rounds to the nearest two decimal places.

and a more detailed description here.
"""
# Enter your code here

price = input('Please enter the price in $: ') # Asks the user for price before tax
new_price = float(price) # Converts string to float
tax = round(.0875 * new_price, 2)  # Amount of tax rounded to the nearest teo decimal places
print('Sales tax: $', tax) # Prints the sales tax amount
price_after_taxes = tax + new_price # Calculates price with tax
print('Total Cost: $', price_after_taxes) # Total amount after tax