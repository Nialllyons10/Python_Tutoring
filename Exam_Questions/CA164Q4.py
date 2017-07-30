def main(): 
	loanPayment = 0 
	insurance = 0 
	gas = 0 
	oil = 0 
	tires = 0 
	maintenance = 0 
	
	print("Enter monthly costs please!")
	
	loanPayment = int(input("Enter loan payment: "))
	annLoan = loanPayment * 12
	
	insurance = int(input("Enter insurance payment: "))
	annInsurance = insurance * 12
	
	gas = int(input("Enter gas payment: "))
	annGas = gas * 12
	
	oil = int(input("Enter oil payment: "))
	annOil = oil * 12 
	
	tires = int(input("Enter tires payment: "))
	annTires = tires * 12
	
	maintenance = int(input("Enter maintenance payment: "))
	annMain = maintenance * 12
	
	print("Loan payment monthly is: " , loanPayment, "  Loan payment per year is: " , annLoan)
	print()
	print("insurance payment monthly is: " , insurance, "  insurance payment per year is: " , annInsurance)
	print()
	print("gas payment monthly is: " , gas, "  gas payment per year is: " , annGas)
	print()
	print("oil payment monthly is: " , oil, "  oil payment per year is: " , annOil)
	print()
	print("tires payment monthly is: " , tires, "  tires payment per year is: " , annTires)
	print()
	print("Maintenance payment monthly is: " , maintenance, "  Loan payment per year is: " , annMain)
	
main()