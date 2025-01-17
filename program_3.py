# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
def sales():
    total_sales = float(input("Please input the total sales for the month: $"))
    county_sales_tax = total_sales * float(0.025)
    state_sales_tax = total_sales * float(0.05)
    total_sales_tax = county_sales_tax + state_sales_tax
    print("Total Sales: $", total_sales, " County Tax: $", county_sales_tax, " State Tax: $", state_sales_tax, " Total Sales Tax: $", total_sales_tax)
sales()
