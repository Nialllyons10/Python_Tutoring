def main():

	num = int(input("Enter a number: "))
	 
	fac = 1
	 
	for i in range(1, num + 1):
		fac = fac * i
	 
	print("The Factorial of ", num, " is ", fac)
	
main()

