def main(): 
	# declare constant
	MONTHS = 12

	# declarce variables
	monthly_rainfall = []
	years = int(input("How many years of rainfall data do you want to input?  "))
	print(years)

	# define nested loop to gather rainfall data
	for time in range(1, years + 1):
		for month in range(1, 13):
			rain = float(input("Enter total inches of rain for month {}:  ".format(month)))
			monthly_rainfall.append(rain)
			print(rain)

	total_months = years * MONTHS

	# calculate and print results
	print("Total months of rainfall: " + str(total_months))    
	print("Total inches of rainfall: " + str(sum(monthly_rainfall)))
	print("Average inches of rainfall per month: " + str(sum(monthly_rainfall) / total_months))
	
main()