'''A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state and 
county sales tax collected. The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent. Write a program that asks the
user to enter the total sales for the month. From this figure, the application should calculate and display the following:

	• The amount of county sales tax 
	• The amount of state sales tax 
	• The total sales tax (county plus state) '''
	
	
def getTax(): 	
	# Variable declarations 
	sales = 0.0 
	stateTax = 0.0 
	countyTax = 0.0 
	totalTax = 0.0 
	 
	# Constants for the state and county tax rates 
	STATE_TAX_RATE = 0.05 
	COUNTY_TAX_RATE = 0.025 
	 
	# Get the total sales for the month. 
	sales = float(input('Enter the total sales for the month: ')) 
	 
	# Calculate the state sales tax. 
	stateTax = sales * STATE_TAX_RATE 
	 
	# Calculate the county sales tax. 
	countyTax = sales * COUNTY_TAX_RATE 
	 
	# Calculate the total tax. 
	totalTax = stateTax + countyTax 
	 
	# Print the tax information. 
	print('State Tax: $' ,stateTax) 
	print('County Tax: $' ,countyTax) 
	print('Total Tax: $',totalTax) 

def main():
	print(getTax())
	
main()