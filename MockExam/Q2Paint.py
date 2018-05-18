def main():

    # Ask for the square footage of wall space to be painted.
    square_footage = int(input('Enter the number of square feet to be painted: '))
    
    # Ask for the price of the paint per gallon.
    price_gallon = int(input('Enter the price of the paint per gallon: '))

    estimate(square_footage, price_gallon)

def estimate(square_footage, price_gallon):
    # 112 sq ft = 1 gallon + 8 hrs of labor (labor is $35 per hour)
	
    num_gallons = square_footage/112
	
    hours_labor = num_gallons * 8
	
    total_price_gallon = num_gallons * price_gallon
	
    total_labor = hours_labor * 35
	
    final_total = total_price_gallon + total_labor
	
    print('Num of gallons: ' , num_gallons)
    print('Total_labour: ' , total_labor)
    print('The total estimated price for this paint job is $', final_total)

# Call the main function.
main()