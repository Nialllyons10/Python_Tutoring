'''Write a program that calculates the total amount of a meal purchased at a restaurant. 
The program should ask the user to enter the charge for the food, and then calculate the amount of a 18 percent 
tip and 7 percent sales tax. Display each of these amounts and the total.''' 

def getAmount():
	# Declare variables for food charges, tip, tax, and total. 
	food = 0.0 
	tip = 0.0 
	tax = 0.0 
	total = 0.0 
	 
	# Constants for the tax rate and tip rate. 
	TAX_RATE = 0.07 
	TIP_RATE = 0.18 
	 
	# Get the food charges. 
	food = float(input("Enter the charge for food: ")) 
	 
	# Calculate the tip. 
	tip = food * TIP_RATE 
	 
	# Calculate the tax. 
	tax = food * TAX_RATE 
	 
	# Calculate the total. 
	total = food + tip + tax 
	 
	# Print the tip, tax, and total. 
	print ("Tip: $", tip) 
	print ("Tax: $", tax) 
	print ("Total: $" , total)
	
def main():
	print(getAmount())
	
main()